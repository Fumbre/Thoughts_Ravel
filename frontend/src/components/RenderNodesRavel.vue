<template>
  <div class="node-card" :style="{ borderColor: color }">
    <h3>{{ title }}</h3>
    <p>{{ description }}</p>
    
    <button @click="$emit('expand', id)">Expand Node</button>
  </div>
</template>

<script setup>
// Define "Props" - these are variables passed from the parent
defineProps({
  id: Number,
  title: String,
  description: String,
  color: {
    type: String,
    default: '#42b883'
  }
})

// Define "Emits" - how the child talks back to the parent
defineEmits(['expand'])
</script>

<style scoped>
.node-card {
  border: 2px solid;
  padding: 15px;
  border-radius: 8px;
  margin: 10px;
}
</style>