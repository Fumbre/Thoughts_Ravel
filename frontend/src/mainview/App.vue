<script setup lang="ts">
// import Graph from "../components/Graph/Graph.vue"
import Space from "../components/Space/Space.vue";
// import Node from "../components/Node/Node.vue";

// crete ref for a flag to show "add space" feature
// const graphGenereted = ref(false)
// const graphRef = ref(null)

// if clicked
// const onSpace = () => {
  // graphGenereted.value = true
  // graphRef.value?.fetchData() 
// }
</script>

<!-- <template>
  <header>
    <h1 class="title">Thoughts Ravel</h1>
  </header>
  <main>
   <Space >
    <!-- <Graph > -->
      <!-- <Node/> -->
    <!-- </Graph> -->
   <!-- </Space>
  </main>
  <footer>
    <!-- <div class="test">we have here menu</div> -->
  <!-- </footer> -->
<!-- </template> --> 


<template>
  <header><h1 class="title">Thoughts Ravel</h1></header>
  <main><RouterView /></main>
  <footer></footer>
</template>
