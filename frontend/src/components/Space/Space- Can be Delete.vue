<script setup>
import { ref } from 'vue'
import SpaceCreation from './SpaceCreation.vue'
import SpaceFetchView from './SpaceFetchView.vue'
import Graph from '../Graph/Graph.vue'
import { apiBaseFetch } from '../../tools/api'


// crete ref for a flag to show "add space" feature
const showCreate = ref(false)
const spaceRef = ref(null)
const SpaceShowFetchView = ref(true)

const graphId = ref(null)
const graphShow = ref(false)

const onSpaceCreated = () => {
  showCreate.value = false
  spaceRef.value?.fetchSpaces() 
}

// if clicked
const onGraphGenerete = async (id) => {
  // turn off menu view
  SpaceShowFetchView.value = false
  graphShow.value = true

  // const test = await fetchSpaceId(id)

  

  graphId.value = id;
  console.log("before child graphId: ", graphId.value)
}

const onGraphNodeClick = async (nodeId) => {
  console.log('lets see mouse event')
  
  // const test = await apiBaseFetch(`/api/node/${nodeId}`)
  
  // const test = await apiBaseFetch(`/api/node`, {
  //   method: 'POST',
  //   headers: {
  //     "Content-Type": "application/json"
  //   },
  //   body: JSON.stringify({
  //     nodeList: [{
  //       name: "Node",
  //       desc: "opt",
  //       positionX: 10,
  //       positionY: 10,
  //       color: 'blue',
  //       shape: 'circle'
  //   }]})
  // })

  // const res = await test.json()
  // console.log(res.data);

  // TODO
  // CREATE on this positions a block
  // make it follow cursor using transform css animation
}


</script>

<template>
  <SpaceFetchView v-if="SpaceShowFetchView" ref="spaceRef" @create="showCreate = true" @select="(id) => onGraphGenerete(id)" />
    <!-- add graph v-if graphshow true -->
  <Graph v-if="graphShow" :spaceId="graphId"  @nodeClick="(id) => onGraphNodeClick(id)" />


  <!-- add fuature: Possibility to open "create space" anywhere. Feture 2. to save config of add spaces to c++ config type-->
  <SpaceCreation v-if="showCreate" @close="showCreate = false" @created="onSpaceCreated" />
</template>