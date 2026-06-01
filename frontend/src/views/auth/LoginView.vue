<script setup lang="ts">
import { ref } from 'vue'
import { useAuth } from '@/hooks/useAuth'

const { login } = useAuth()
const username = ref('')
const password = ref('')
const error = ref<string | null>(null)
const loading = ref(false)

const handleSubmit = async () => {
    if (!username.value || !password.value) return
    loading.value = true
    error.value = null
    try {
        await login(username.value, password.value)
    } catch (err: unknown) {
        error.value = err instanceof Error ? err.message : 'Login failed'
    } finally {
        loading.value = false
    }
}
</script>

<template>
    <div class="auth auth__container">
        <div class="auth__card">
            <h2 class="auth__title">Welcome back</h2>
            <p class="auth__sub">Sign in to your account</p>

            <div class="auth__fields">
                <div class="auth-field">
                    <label class="auth-field__label">Username</label>
                    <input v-model="username" class="auth-field__input" type="text" placeholder="your username"
                        @keydown.enter="handleSubmit" />
                </div>
                <div class="auth-field">
                    <label class="auth-field__label">Password</label>
                    <input v-model="password" class="auth-field__input" type="password" placeholder="••••••••"
                        @keydown.enter="handleSubmit" />
                </div>
            </div>

            <p v-if="error" class="auth__error">{{ error }}</p>

            <button class="btn btn-primary btn-full" :disabled="loading" @click="handleSubmit">
                {{ loading ? 'Signing in...' : 'Sign in' }}
            </button>

            <p class="auth__footer">
                Don't have an account?
                <RouterLink to="/register">Register</RouterLink>
            </p>
        </div>
    </div>
</template>

<style>
.auth__container {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 80vh;
}

.auth__card {
    width: 100%;
    max-width: 380px;
    padding: 2rem;
    border: 1px solid #eee;
    border-radius: 14px;
    background: white;
}

.auth__title {
    font-size: 22px;
    font-weight: 500;
    margin: 0 0 4px;
}

.auth__sub {
    font-size: 14px;
    color: #888;
    margin: 0 0 1.5rem;
}

.auth__fields {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin-bottom: 1rem;
}

.auth-field__label {
    display: block;
    font-size: 13px;
    font-weight: 500;
    color: #555;
    margin-bottom: 6px;
}

.auth-field__input {
    width: 100%;
    font-size: 14px;
    padding: 10px 12px;
    border: 1px solid #ddd;
    border-radius: 8px;
    outline: none;
    box-sizing: border-box;
    transition: border-color 0.15s;
}

.auth-field__input:focus {
    border-color: #4f7ef8;
}

.auth__footer {
    font-size: 13px;
    color: #888;
    text-align: center;
    margin-top: 1.25rem;
}

.auth__footer a {
    color: #4f7ef8;
    text-decoration: none;
}
</style>