<script setup>
import { ref } from 'vue'

const emit = defineEmits(['confirm', 'cancel'])

const name = ref('')
const description = ref('')
const color = ref('#000000')

const confirm = () => {
    if (!name.value.trim()) return
    emit('confirm', {
        name: name.value,
        description: description.value,
        color: color.value,
    })
}
</script>

<template>
    <div class="modal-overlay" @click.self="$emit('cancel')">
        <div class="modal">
            <h3 class="modal__title">Add Node</h3>
            <label>
                <span class="modal__label-text">Name:</span>
                <input v-model="name" placeholder="Node name" />
            </label>
            <label>
                <span class="modal__label-text">Connection name:</span>
                <input v-model="description" placeholder="ex. http, gRPC, ftp" />
            </label>
            <label>
                <span class="modal__label-text">Color</span>
                <input type="color" v-model="color" />
            </label>
            <div class="modal-actions">
                <button @click="$emit('cancel')">Cancel</button>
                <button @click="confirm">Add</button>
            </div>
        </div>
    </div>
</template>

<style scoped>
.modal__label-text {
    display: block;
    margin-bottom: 10px;
}

.modal-overlay {
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
    padding: 24px;
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    gap: 8px;
    min-width: 300px;
}

.modal h3 {
    margin: 0 0 8px;
}

.modal input {
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 14px;
}

.modal-actions {
    display: flex;
    justify-content: flex-end;
    gap: 8px;
    margin-top: 8px;
}

.modal-actions button {
    padding: 8px 16px;
    border-radius: 4px;
    border: none;
    cursor: pointer;
}

.modal-actions button:last-child {
    background: #4f46e5;
    color: white;
}
</style>