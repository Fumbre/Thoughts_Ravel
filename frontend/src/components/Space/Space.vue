<script setup>
import { ref } from 'vue'
import SpaceCreate from './SpaceCreate.vue'
import SpaceView from './SpaceView.vue'

// crete ref for a flag to show "add space" feature
const showCreate = ref(false)
const spaceRef = ref(null)

// if clicked
const onCreated = () => {
  showCreate.value = false
  spaceRef.value?.fetchSpaces() 
}
</script>

<template>
  <SpaceView ref="spaceRef" @create="showCreate = true" @select="(id) => console.log(id)" />
  <SpaceCreate v-if="showCreate" @close="showCreate = false" @created="onCreated" />
</template>