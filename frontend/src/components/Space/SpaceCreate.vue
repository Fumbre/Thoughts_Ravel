<script setup>
import { ref } from 'vue'
import { apiBaseFetch } from '../../tools/api'

const emit = defineEmits(['created', 'close'])

const title = ref('')
const loading = ref(false)
const error = ref(null)

const handleSubmit = async () => {
  if (!title.value.trim()) return
  loading.value = true
  error.value = null

  try {
    const res = await apiBaseFetch('/api/space', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        spaceList: [{ userId: 1, title: title.value.trim() }]
      })
    })
    if (!res.ok) throw new Error('Failed to create space')
    emit('created')
    title.value = ''
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="overlay" @click.self="emit('close')">
    <div class="modal">
      <div class="modal__header">
        <h3 class="modal__title">New space</h3>
        <button class="modal__close" @click="emit('close')">✕</button>
      </div>

      <div class="modal__body">
        <label class="field__label">Space name</label>
        <input
          v-model="title"
          class="field__input"
          type="text"
          placeholder="e.g. research, ideas, movies..."
          @keydown.enter="handleSubmit"
          autofocus
        />
        <p v-if="error" class="err">{{ error }}</p>
      </div>

      <div class="modal__footer">
        <button class="btn btn--ghost" @click="emit('close')">Cancel</button>
        <button class="btn btn--primary" :disabled="loading || !title.trim()" @click="handleSubmit">
          {{ loading ? 'Creating...' : 'Create space' }}
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 100;
}

.modal {
  background: white;
  border-radius: 14px;
  width: 100%;
  max-width: 420px;
  margin: 1rem;
  overflow: hidden;
}

.modal__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.25rem 1.5rem 0;
}

.modal__title {
  font-size: 16px;
  font-weight: 500;
  margin: 0;
}

.modal__close {
  background: none;
  border: none;
  font-size: 14px;
  color: #aaa;
  cursor: pointer;
  padding: 4px;
  line-height: 1;
}

.modal__close:hover {
  color: #555;
}

.modal__body {
  padding: 1.25rem 1.5rem;
}

.field__label {
  display: block;
  font-size: 13px;
  font-weight: 500;
  color: #555;
  margin-bottom: 8px;
}

.field__input {
  width: 100%;
  font-size: 14px;
  padding: 10px 12px;
  border: 1px solid #ddd;
  border-radius: 8px;
  outline: none;
  box-sizing: border-box;
  transition: border-color 0.15s;
}

.field__input:focus {
  border-color: #4f7ef8;
}

.modal__footer {
  display: flex;
  justify-content: flex-end;
  gap: 8px;
  padding: 0 1.5rem 1.25rem;
}

.btn {
  font-size: 13px;
  font-weight: 500;
  padding: 8px 16px;
  border-radius: 8px;
  cursor: pointer;
  border: 1px solid transparent;
  transition: background 0.15s, opacity 0.15s;
}

.btn--ghost {
  background: white;
  border-color: #ddd;
  color: #555;
}

.btn--ghost:hover {
  background: #f5f5f5;
}

.btn--primary {
  background: #4f7ef8;
  color: white;
  border-color: #4f7ef8;
}

.btn--primary:hover {
  background: #3a6de0;
}

.btn--primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.err {
  font-size: 13px;
  color: #e24b4a;
  margin: 8px 0 0;
}
</style>