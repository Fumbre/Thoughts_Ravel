<template>
  <div id="mynetwork"></div>
</template>

<script>
import { onMounted } from "vue"

export default {
  props: ['graphData'],
  setup(props) {
    onMounted(() => {
      const nodes = new vis.DataSet(props.graphData.nodes)
      const edges = new vis.DataSet(props.graphData.edges)
      const container = document.getElementById('mynetwork')
      const data = { nodes, edges }
      const options = {} // same as PyVis options
      new vis.Network(container, data, options)
    })
  }
}
</script>