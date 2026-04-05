<script setup>
import { ref } from 'vue'
import SpaceCreation from './SpaceCreation.vue'
import SpaceFetchView from './SpaceFetchView.vue'
import Graph from '../Graph/Graph.vue'

// crete ref for a flag to show "add space" feature
const showCreate = ref(false)
const spaceRef = ref(null)
const SpaceShowFetchView = ref(true)

const graphId = ref(null)
const graphShow = ref(false)

// if clicked
const onSpaceCreated = () => {
  showCreate.value = false
  spaceRef.value?.fetchSpaces() 
}

const onGraphGenerete = (id) => {
  // turn off menu view
  SpaceShowFetchView.value = false
  graphShow.value = true

  graphId.value = id;
  console.log("before child graphId: ", graphId.value)
}

const onGraphNodeClick = (nodeId) => {
  console.log('lets see mouse event')

  // TODO
  // CREATE on this positions a block
  // make it follow cursor using transform css animation
}


</script>

<template>
  <SpaceFetchView v-if="SpaceShowFetchView" ref="spaceRef" @create="showCreate = true" @select="(id) => onGraphGenerete(id)" />
    <!-- add graph v-if graphshow true -->
  <Graph v-if="graphShow" :nodeId="graphId"  @nodeClick="(id) => onGraphNodeClick(id)" />


  <!-- add fuature: Possibility to open "create space" anywhere. Feture 2. to save config of add spaces to c++ config type-->
  <SpaceCreation v-if="showCreate" @close="showCreate = false" @created="onSpaceCreated" />
</template>