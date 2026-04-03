<script setup>
import { ref, onMounted, nextTick } from 'vue'
import { Network } from 'vis-network/standalone'
import { apiBaseFetch } from '../../tools/api';

const backendData = ref(null)
const error = ref(null)

const graphElement = ref(null)
let network = null

const fetchData = async () => {
  try {
    const response = await apiBaseFetch('/api/graph')
    const response1 = await apiBaseFetch('/api/node/7444177008625455104') // just cheking here the get request

    if (!response.ok) throw new Error('Backend not responding')
    
    const data = await response.json()
    backendData.value = data

    const data1 = await response1.json()
    console.log(  data1)

    await nextTick()

    if (!graphElement.value) {
        console.log("Graph container not found")
        return
    }

    network = new Network(graphElement.value, data, {

        // Add your vis-network options here
        physics: { enabled: false },
        edges: { smooth: {
            enabled: true,
            type: 'continuous',
            roundness: 0.5
        } },
        interaction: {
            dragView: true,
        }
    })

    network.on('click', (params)=>{
        if (params.nodes.length > 0) {
            const nodeId = params.nodes[0]

            
            handleNodeClick(nodeId)
        }
    })

    network.on("dragEnd", function (params) {
        if (params.nodes.length > 0) {
            const nodeId = params.nodes[0];
            const { x, y } = network.getPosition(nodeId);

            console.log(`Node ${nodeId} moved to X: ${x}, Y: ${y}`);
        }

    });

    console.log("Network initialized:", network)
  } catch (err) {
    error.value = err.message
  }
}

function handleNodeClick(nodeId) {
    console.log("node clicked: ", nodeId);
}

onMounted(() => {
  fetchData()

  const resizeObserver = new ResizeObserver(() => {
    if (network) {
        network.redraw();
        // Optional: network.fit(); if you want it to auto-center on resize
    }
  });
  
  if (graphElement.value) {
      resizeObserver.observe(graphElement.value);
  }
})
</script>

<template>
    <div class="graphic" ref="graphElement"></div>
    <p v-if="error" style="color: red;">{{ error }}</p>
</template>

<style scoped>

.graphic {
    height: 700px;
}


</style>