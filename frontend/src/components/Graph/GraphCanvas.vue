<script setup>
import { ref, onMounted, watch, nextTick } from 'vue'
import { Network, DataSet } from 'vis-network/standalone'
import { fetchGraph } from '@/api/graph/graph'

const props = defineProps({
    spaceId: { type: String, required: true }
})
const emit = defineEmits(['nodeClick', 'nodeMoved'])
const graphElement = ref(null)
const error = ref(null)

let network = null
let nodesDataset = null
let edgesDataset = null
let rawNodesReference = []

const initNetwork = (data) => {
    rawNodesReference = data.nodes || []
    nodesDataset = new DataSet(data.nodes || [])
    edgesDataset = new DataSet(data.edges || [])

    network = new Network(graphElement.value, {
        nodes: nodesDataset,
        edges: edgesDataset
    }, {
        nodes: {
            font: {
                color: '#ffffff'
            }
        },
        physics: { enabled: false },
        edges: {
            smooth: { enabled: true, type: 'continuous', roundness: 0.5 }
        },
        interaction: { dragView: true }
    })

    network.on('click', ({ nodes }) => {
        const clickedNodeId = nodes[0]
        const fullNodeData = rawNodesReference.find(n => String(n.id) === String(clickedNodeId))
        if (fullNodeData) {
            emit('nodeClick', fullNodeData)
        } else {
            emit('nodeClick', { id: clickedNodeId })
        }
    })

    network.on('dragEnd', ({ nodes }) => {
        if (nodes.length > 0) {
            const pos = network.getPosition(nodes[0])
            emit('nodeMoved', { id: nodes[0], ...pos })
        }
    })
}

const addNode = (node) => {
    if (!nodesDataset) return
    const visNode = {
        id: String(node.id),
        label: node.name,
        color: node.color,
        shape: node.shape,
        x: node.position_x,
        y: node.position_y,
    }
    nodesDataset.add(visNode)
    rawNodesReference.push(visNode)  // keep reference in sync

    if (node.parent_node_id && String(node.parent_node_id) !== '0') {
        edgesDataset.add({
            from: String(node.parent_node_id),
            to: String(node.id),
        })
    }
}

const loadGraph = async () => {
    try {
        const res = await fetchGraph(props.spaceId)
        if (res.error) throw new Error('Failed to load graph')
        await nextTick()
        if (graphElement.value) initNetwork(res.data)
    } catch (err) {
        error.value = err.message
    }
}

watch(() => props.spaceId, loadGraph, { immediate: true })
onMounted(() => {
    const observer = new ResizeObserver(() => network?.redraw())
    if (graphElement.value) observer.observe(graphElement.value)
})

defineExpose({ addNode })
</script>

<template>
    <div class="graph-canvas" ref="graphElement" />
    <p v-if="error" class="graph-error">{{ error }}</p>
</template>

<style scoped>
.graph-canvas {
    height: 400px;
}

.graph-error {
    color: #e24b4a;
    font-size: 13px;
}
</style>