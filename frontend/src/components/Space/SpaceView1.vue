<script setup>
import { ref, onMounted } from 'vue'
import { apiBaseFetch } from '../../tools/api'
import { fetchSpacesList } from '../../api/user/spaceList'

const spaces = ref([])
const error = ref(null)

const emit = defineEmits(['select', 'create'])

const fetchSpaces = async () => {
  const res = await fetchSpacesList()

  if (res.error) {
    error.value = res.error
    return
  }

  spaces.value = res.data
}

onMounted(fetchSpaces)
defineExpose({ fetchSpaces })
</script>

<template>
  <div class="spaces__container container">
    <div class="spaces__top">
      <div class="spaces__header">
        <h2 class="spaces__title">Your spaces</h2>
        <p class="spaces__sub">Pick a space to explore its graph</p>
      </div>
      <button class="btn-create" @click="emit('create')">
        + New space
      </button>
    </div>

    <ul v-if="spaces.length" class="spaces__list">
      <li v-for="space in spaces" :key="space.id"
          class="space__card" @click="emit('select', space.id)">
        <div class="space__wrapper">
          <div class="space__dot"></div>
          <div>
            <p class="space__title">{{ space.title }}</p>
            <p class="space__meta">{{ space.id }}</p>
          </div>
        </div>
        <span class="space__arrow">›</span>
      </li>
    </ul>

    <div v-else class="empty">No spaces yet. Create your first one.</div>
    <p v-if="error" class="err">{{ error }}</p>
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

.spaces__list {
  list-style: none;
  margin: 0;
  padding: 0;
  border: 1px solid #eee;
  border-radius: 12px;
  overflow: hidden;
}

.space__card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 18px;
  background: white;
  cursor: pointer;
  transition: background 0.12s;
}

.space__card:hover {
  background: #fafafa;
}

.space__card + .space__card {
  border-top: 1px solid #eee;
}

.space__wrapper {
  display: flex;
  align-items: center;
  gap: 12px;
}

.space__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #4f7ef8;
  flex-shrink: 0;
}

.space__title {
  font-size: 14px;
  font-weight: 500;
  margin: 0 0 2px;
}

.space__meta {
  font-size: 12px;
  color: #aaa;
  margin: 0;
}

.space__arrow {
  font-size: 18px;
  color: #ccc;
}

.empty {
  font-size: 14px;
  color: #aaa;
  padding: 2.5rem;
  text-align: center;
  border: 1px solid #eee;
  border-radius: 12px;
}

.err {
  font-size: 13px;
  color: #e24b4a;
  margin-top: 1rem;
}
</style>