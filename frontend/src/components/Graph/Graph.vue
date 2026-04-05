<script setup>
import { ref, onMounted, nextTick, watch } from 'vue'
import { Network } from 'vis-network/standalone'
import { apiBaseFetch } from '../../tools/api';
// import { node} handleMouseEvent

const backendData = ref(null)
const error = ref(null)

const generateGraph = ref(false)
const graphElement = ref(null)
let network = null

const props = defineProps({
  nodeId: String 
})

const emit = defineEmits(['nodeClick'])

watch(
  () => props.nodeId,
  async (newId) => {
    if (!newId) return
    await fetchData(newId)
  },
  { immediate: true } // runs on first load too
)

async function fetchData (nodeId) {
  try {
    // fetch graphic generation object
    const response = await apiBaseFetch(`/api/graph/${nodeId}`)

    if (!response.ok) throw new Error('Backend not responding')
    // const response1 = await apiBaseFetch('/api/node/7444177008625455104') // just cheking here the get request
    
    const data = await response.json()
    backendData.value = data

    // const data1 = await response1.json()
    console.log(  data)

    await nextTick()

    if (!graphElement.value) {
        console.log("Graph container not found")
        return
    }


    // create it using correct x and y from database
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

    // const positions = network.getPositions()

    // set nodes position to correct database position
    // const getAllNodePositions = () => {
    //     if (!network) return {}

    //     const positions = network.getPositions()
    //     console.log("All positions:", positions)

    //     return positions
    // }

    network.on('click', (params)=>{
        if (params.nodes.length > 0) {
            const nodeId = params.nodes[0]
            emit('nodeClick', nodeId)

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

    // console.log("Network initialized:", network)

    generateGraph.value = true;
  } catch (err) {
    error.value = err.message
  }
}

function handleNodeClick(nodeId) {
    console.log("n1ode clicked: ", nodeId);
}



onMounted(() => {

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