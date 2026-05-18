<script setup>
import { ref, onMounted, computed } from 'vue'
import { fetchSpaceList } from '@/api/space/spaceList'


const props = defineProps({
  sortOrder: { type: String, default: 'asc' }
})

// list of spaces
const spaces = ref([])
const error = ref(null)


const loadSpaces = async () => {
  // fetch list of spaces for current user
  const res = await fetchSpaceList()

  // create a faile loader class to hangle UI for errors
  if (res.error) { error.value = res.error; return }

  spaces.value = res.data.spaceList
}

// sort spaces based on its id
const sortedSpaces = computed(() => {
  console.log("sorting spaces with order: ")
  if (props.sortOrder === 'asc') return spaces.value
  return [...spaces.value].sort((a, b) => b.id.localeCompare(a.id))
})

onMounted(loadSpaces)
defineExpose({ loadSpaces })
</script>

<template>
  <ul v-if="spaces.length" class="spaces__list">
    <li v-for="space in sortedSpaces" :key="space.id" :data-sort="space.name" class="space__card">
      <RouterLink :to="`/space/${space.id}`" class="space__link">
        <div class="space__wrapper">
          <div class="space__dot"></div>
          <div>
            <p class="space__title">{{ space.title }}</p>
            <!-- <p class="space__meta">{{ space.id }}</p> -->
          </div>
        </div>
        <span class="space__arrow">›</span>
      </RouterLink>
    </li>
  </ul>

  <div v-else class="empty">No spaces yet. Create your first one.</div>
  <p v-if="error" class="err">{{ error }}</p>
</template>

<style scoped>
.spaces__list {
  list-style: none;
  margin: 0;
  padding: 0;
  border: 1px solid #eee;
  border-radius: 12px;
  overflow: hidden;
}

.space__card {
  position: relative;
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

.space__card+.space__card {
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

.space__link {
  display: flex;
  justify-content: space-between;
  width: 100%;
  text-decoration: none;
  color: #f84fed;
}

.space__link::before {
  position: absolute;
  content: '';
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
}

.space__meta {
  font-size: 12px;
  color: #aaa;
  margin: 0;
}

.space__arrow {
  font-size: 18px;
  color: #ccc;
  justify-self: end;
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