<script setup>
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import GraphCanvas from '@/components/Graph/GraphCanvas.vue'
import { postNodeToNode } from '../api/node/node'

const route = useRoute()
const spaceId = route.params.id

const editMode = ref(false)
const selectedNodeId = ref(null)
const selectedNodeName = ref(null)

const onNodeClick = (nodeId) => {
    if (editMode.value) {
        // select node for editing, no navigation
        selectedNodeId.value = nodeId
        // you'll fetch node name here later
        selectedNodeName.value = nodeId  // temp, replace with actual name
    } else {
        // navigate to node page
        route.push(`/node/${nodeId}`)
    }
}
const onNodeMoved = ({ id, x, y }) => {
    console.log('node moved:', id, x, y)
    // save position to DB later
}

const addNode = () => {
    const testChild = {
        name: 'my nanme',
        desc: 'string | null',
        positionX: 23,
        positionY: 23,
        color: "blue",
        shape: "circle",
        creater_id: 1,
    }

    const testParent = {
        nodeId: "7463519295578836993",
        spaceId: "7463520655892287488",
        userId: "1",
    }


    const re = postNodeToNode(testChild, testParent)
    console.log("[insdie space view]", re)
}

</script>

<template>
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
                    <span>selected node: {{ selectedNodeName ?? 'Node is not selected' }}</span>
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
            <button class="btn-accept">save your changes</button>
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