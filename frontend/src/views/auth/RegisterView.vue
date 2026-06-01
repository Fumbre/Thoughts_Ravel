<script setup lang="ts">
import { ref } from 'vue'
import { useAuth } from '@/hooks/useAuth'
import { useRouter } from 'vue-router'

const { register } = useAuth()
const router = useRouter()
const username = ref('')
const email = ref('')
const password = ref('')
const error = ref<string | null>(null)
const loading = ref(false)

const handleSubmit = async () => {
    if (!username.value || !email.value || !password.value) return
    loading.value = true
    error.value = null
    try {
        await register(username.value, email.value, password.value)
        router.push('/login')
    } catch (err: unknown) {
        error.value = err instanceof Error ? err.message : 'Registration failed'
    } finally {
        loading.value = false
    }
}
</script>

<template>
    <div class="auth__container">
        <div class="auth__card">
            <h2 class="auth__title">Create account</h2>
            <p class="auth__sub">Start building your thought graph</p>

            <div class="auth__fields">
                <div class="auth-field">
                    <label class="auth-field__label">Username</label>
                    <input v-model="username" class="auth-field__input" type="text" placeholder="username" />
                </div>
                <div class="auth-field">
                    <label class="auth-field__label">Email</label>
                    <input v-model="email" class="auth-field__input" type="email" placeholder="you@example.com" />
                </div>
                <div class="auth-field">
                    <label class="auth-field__label">Password</label>
                    <input v-model="password" class="auth-field__input" type="password" placeholder="••••••••"
                        @keydown.enter="handleSubmit" />
                </div>
            </div>

            <p v-if="error" class="auth__error">{{ error }}</p>

            <button class="btn btn-primary btn-full" :disabled="loading" @click="handleSubmit">
                {{ loading ? 'Creating account...' : 'Create account' }}
            </button>

            <p class="auth__footer">
                Already have an account?
                <RouterLink to="/login">Sign in</RouterLink>
            </p>
        </div>
    </div>
</template>
