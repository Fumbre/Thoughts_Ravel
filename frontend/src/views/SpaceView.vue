<script setup>
import { ref } from 'vue'
import SpaceCreationModal from '@/components/Space/SpaceCreationModal.vue'
import SpaceList from '@/components/Space/SpaceList.vue'

// space creation modal window
const showCreationModal = ref(false)

// space list
const spaceListRef = ref(null)
const sortOrder = ref('asc')

// when a new space created - update list 
// and close modal window
const onSpaceCreated = () => {
  showCreationModal.value = false
  spaceListRef.value?.loadSpaces()
}

</script>

<template>
  <div class="spaces__container container">
    <div class="spaces__top">
      <div class="spaces__header">
        <h2 class="spaces__title">Your spaces</h2>
        <p class="spaces__sub">Pick a space to explore its graph</p>
      </div>
      <button class="btn-create" @click="showCreationModal = true">
        + New space
      </button>
      <nav class="spaces__sort sort">
        <ul class="sort__list">
          <li class="sort__item">
            <button @click="sortOrder = 'asc'" :class="{ 'sort__item--active': sortOrder === 'asc' }">asc</button>
          </li>
          <li class="sort__item">
            <button @click="sortOrder = 'desc'" :class="{ 'sort__item--active': sortOrder === 'desc' }">desc</button>
          </li>
        </ul>
      </nav>
    </div>
    <SpaceCreationModal v-if="showCreationModal" @close="showCreationModal = false" @created="onSpaceCreated" />

    <SpaceList ref="spaceListRef" :sortOrder="sortOrder" />
  </div>

</template>


<style scoped>
.spaces__container {
  padding: 2rem 1.5rem;
}

.spaces__top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 1.5rem;
}

.spaces__title {
  font-size: 22px;
  font-weight: 500;
  margin: 0 0 4px;
}

.spaces__sub {
  font-size: 14px;
  color: #888;
  margin: 0;
}

.space__link {
  display: flex;
  justify-content: space-between;
  width: 100%;
  text-decoration: none;
}

.btn-create {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  font-weight: 500;
  padding: 8px 16px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background: white;
  cursor: pointer;
  white-space: nowrap;
  transition: background 0.15s, border-color 0.15s;
}

.btn-create:hover {
  background: #f5f5f5;
  border-color: #bbb;
}
</style>