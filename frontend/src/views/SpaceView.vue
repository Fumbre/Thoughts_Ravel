<script setup>
import { ref } from 'vue'
import SpaceCreation from '@/components/Space/SpaceCreation.vue'
import SpaceList from '@/components/Space/SpaceList.vue'
import { apiBaseFetch } from '@/tools/api'


// crete ref for a flag to show "add space" feature
const showCreate = ref(false)
const spaceRef = ref(null)
const SpaceListRef = ref(true)

const graphId = ref(null)
const graphShow = ref(false)

const onSpaceCreated = () => {
  showCreate.value = false
  spaceRef.value?.fetchSpaces() 
}

// if clicked
const onGraphGenerete = async (id) => {
  // turn off menu view
  SpaceListRef.value = false
  graphShow.value = true

  // const test = await fetchSpaceId(id)

  

  graphId.value = id;
  console.log("before child graphId: ", graphId.value)
}



</script>

<template>
  <SpaceList v-if="SpaceListRef" ref="spaceRef" @create="showCreate = true" @select="(id) => onGraphGenerete(id)" />

  <!-- add fuature: Possibility to open "create space" anywhere. Feture 2. to save config of add spaces to c++ config type-->
  <SpaceCreation v-if="showCreate" @close="showCreate = false" @created="onSpaceCreated" />
</template>