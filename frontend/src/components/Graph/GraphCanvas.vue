<script setup>
import { ref, onMounted, watch, nextTick } from 'vue'
import { Network } from 'vis-network/standalone'
import { apiBaseFetch } from '@/tools/api'
import { fetchGraph } from '@/api/graph/graph'

const props = defineProps({
    spaceId: { type: String, required: true }
})

const emit = defineEmits(['nodeClick', 'nodeMoved'])

const graphElement = ref(null)
const error = ref(null)
let network = null

const initNetwork = (data) => {
    network = new Network(graphElement.value, data, {
        physics: { enabled: false },
        edges: {
            smooth: { enabled: true, type: 'continuous', roundness: 0.5 }
        },
        interaction: { dragView: true }
    })

    network.on('click', ({ nodes }) => {
        console.log(nodes)
        if (nodes.length > 0) emit('nodeClick', nodes[0])
    })

    network.on('dragEnd', ({ nodes }) => {
        if (nodes.length > 0) {
            const pos = network.getPosition(nodes[0])
            emit('nodeMoved', { id: nodes[0], ...pos })
        }
    })
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