<script setup>
import { ref, computed, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import NodeModal from '@/components/Node/NodeModal.vue'
import GraphCanvas from '@/components/Graph/GraphCanvas.vue'
import { postNodeEdge, updateNodePos } from '@/api/node/node'
import { apiBaseFetch } from '../tools/api'


const route = useRoute()
const router = useRouter()
const spaceId = computed(() => route.params.id)

const editMode = ref(false)
const selectedNode = ref(null)

const graphCanvas = ref(null)

const onNodeClick = (node) => {
    if (editMode.value) {
        // select node for editing, no navigation
        selectedNode.value = node
        // you'll fetch node name here later
        console.log(selectedNode.value)
    } else {
        console.log(node.id)
        // navigate to node page
        if (node.id)
            router.push(`/space/${node.id}`)
    }
}
const onNodeMoved = async ({ id, x, y }) => {
    console.log('node moved:', id, x, y)
    try {
        const res = await updateNodePos(id, x, y)
    } catch (error) {
        console.log(error)
    }
    // save position to DB later
}

const showModal = ref(false)

const addNode = () => {
    showModal.value = true
}

const handleConfirm = async (data) => {
    showModal.value = false
    console.log(data)


    const node = [{
        space_id: spaceId.value,
        name: data.name,
        description: data.description,
        type: '0',
        shape: 'circle',
        color: `${data.color}`,
        parent_node_id: selectedNode.value.id,

        parent_pos_x: selectedNode.value.x,
        parent_pos_y: selectedNode.value.y,
        label: data.description
    }]

    try {
        const re = await postNodeEdge(node)

        console.log(re)

        if (re.code === 200 && re.data) {
            const nodes = Array.isArray(re.data) ? re.data : [re.data]
            nodes.forEach(n => graphCanvas.value.addNode(n))
        }
        console.log("[insdie space view]", node)
    } catch (error) {
        console.log(error)
    }
}


const userInput = ref('')
const aiResponse = ref('')
const isLoading = ref(false)

// The function that handles the form submission
const handleChatSubmit = async () => {
    // Don't send empty requests
    if (!userInput.value.trim()) return

    isLoading.value = true
    try {
        // Replace this URL with your actual custom API endpoint
        const response = await apiBaseFetch(`/ai/chat/${spaceId.value}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ prompt: userInput.value }),
        })

        const data = await response.json()
        console.log(data)
        if (data.code != 200)
            throw new Error(`couldn't get AI response code: ${data.code}`);

        aiResponse.value = data.data
        console.log(aiResponse.value)

        // Clear the input field after sending
        userInput.value = ''
    } catch (error) {
        console.error('Failed to chat with AI:', error)
    } finally {
        isLoading.value = false
    }
}

const spaceName = ref('Loading...')
const loadSpaceDetails = async (id) => {
    if (!id) return
    try {
        const response = await apiBaseFetch(`/api/node/${id}`)
        const resData = await response.json()

        console.log(resData)

        if (resData && resData.data) {
            // Adjust this property path to match whatever column holds your title (e.g., resData.data.name)
            spaceName.value = resData.data.name || `Space #${id}`
        }
    } catch (error) {
        console.error('Failed to resolve space metadata name:', error)
        spaceName.value = 'Unknown Space'
    }
}

watch(
    () => route.params.id,
    (newId) => {
        loadSpaceDetails(newId)
    },
    { immediate: true }
)

</script>

<template>
    <NodeModal v-if="showModal" @confirm="handleConfirm" @cancel="showModal = false" />




    <div class="inside-space__container container">
        <h2>Inside space: {{ spaceName }}</h2>
        <div class="ai ">
            <form @submit.prevent="handleChatSubmit">
                <label>
                    <span>chat with AI asistnet: </span>
                    <input v-model="userInput" type="text" placeholder="Type your message..." :disabled="isLoading">
                </label>
                <input type="submit" :value="isLoading ? 'Sending...' : 'send'" :disabled="isLoading">
            </form>
            <br>
            <div v-if="aiResponse" class="response-box">
                <strong>AI:</strong> {{ aiResponse }}
            </div>
        </div>
        <div class="node__editor flex">
            <label class="node__editor-label flex">
                <span class="node__editor-text">Editor mode</span>
                <button :class="['node__editor-btn', 'btn-switch', { 'btn-switch--active': editMode }]"
                    @click="editMode = !editMode" />
            </label>
        </div>
    </div>

    <div class="graphic">
        <GraphCanvas ref="graphCanvas" :spaceId="spaceId" @nodeClick="onNodeClick" @nodeMoved="onNodeMoved" />
    </div>
    <div class="inside-space__container container">

        <div v-if="editMode" class="panel">
            <h3>Actions on specific node</h3>
            <ul class="panel-edit-node__list">
                <li class="panel-edit-node__item">
                    <span>selected node: {{ selectedNode?.label ?? 'Node is not selected' }}</span>
                </li>
                <li class="panel-edit-node__item">
                    <button class="btn-green-light" @click="addNode">add node</button>
                </li>
                <li class="panel-edit-node__item">
                    <button class="btn-orange">rename current node</button>
                </li>
                <li class="panel-edit-node__item">
                    <button class="btn-red">remove current node</button>
                </li>
            </ul>

            <h3>Clicker editror mode</h3>
            <p>Your clicks become an editor tool. If you want to add or remove a lot of nodes</p>
            <ul class="panel-edit-nodes__list">
                <li class="panel-edit-nodes__item">
                    <button class="btn-green-light">add al lot of nodes</button>
                </li>
                <li class="panel-edit-nodes__item">
                    <button class="btn-red">remove al lot of nodes</button>
                </li>
            </ul>
        </div>


    </div>
</template>


<style scoped>
.graphic {
    border: solid 1px black;
}

.node__editor {
    justify-content: end;
}

.node__editor-label {
    justify-content: end;
}

.node__editor-text {
    margin-right: 10px;
}

.node__eidtor-btn {
    display: block;
}
</style>