<script setup>
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import NodeModal from '@/components/Node/NodeModal.vue'
import GraphCanvas from '@/components/Graph/GraphCanvas.vue'
import { postNodeEdge, updateNodePos } from '@/api/node/node'


const route = useRoute()
const spaceId = route.params.id

const editMode = ref(false)
const selectedNode = ref(null)

const onNodeClick = (node) => {
    if (editMode.value) {
        // select node for editing, no navigation
        selectedNode.value = node
        // you'll fetch node name here later
        console.log(selectedNode.value)
    } else {
        // navigate to node page
        // route.push(`/node/${nodeId}`)
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

    const space = window.location.pathname.replace('/space/', '')
    console.log(space)

    const node = [{
        space_id: space,
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
        console.log("[insdie space view]", node)
    } catch (error) {
        console.log(error)
    }
}

</script>

<template>
    <NodeModal v-if="showModal" @confirm="handleConfirm" @cancel="showModal = false" />

    <div class="inside-space__container container">
        <h2>inside space: {name of the space}</h2>
        <div class="node__editor flex">
            <label class="node__editor-label flex">
                <span class="node__editor-text">Editor mode</span>
                <button :class="['node__editor-btn', 'btn-switch', { 'btn-switch--active': editMode }]"
                    @click="editMode = !editMode" />
            </label>
        </div>
    </div>

    <div class="graphic">
        <GraphCanvas :spaceId="spaceId" @nodeClick="onNodeClick" @nodeMoved="onNodeMoved" />
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