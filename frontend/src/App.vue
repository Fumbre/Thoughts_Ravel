<script setup lang="ts">
import RenderNodesRavel from './components/RenderNodesRavel.vue'
import { ref } from 'vue'
import what from './components/what.vue'
// This data usually comes from your Python backend/NetworkX
const nodes = ref([
  { id: 1, name: "Input Layer", info: "Process raw signals" },
  { id: 2, name: "Hidden Layer", info: "Weighted calculations" },
  { id: 3, name: "Output Layer", info: "Final classification" }
])

const handleExpand = (id) => {
  console.log("Expanding node logic for ID:", id)
  alert(`You clicked node ${id}!`)
}

</script>

<template>
  <div class="engine-container">
    <h1>Representation Engine</h1>
    <what />
<!-- 
    <RenderNodesRaveli
      v-for="node in nodes" 
      :key="node.id"
      :id="node.id"
      :title="node.name"
      :description="node.info"
      @expand="handleExpand"
    /> -->
  </div>
</template>