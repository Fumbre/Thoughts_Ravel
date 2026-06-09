import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { apiBaseFetch } from '@/tools/api'

const user = ref<{ id: string, username: string } | null>(null)
const initialized = ref(false)

export const useAuth = () => {
    const router = useRouter()
    const isAuthenticated = computed(() => !!user.value)

    const register = async (username: string, email: string, password: string) => {
        const res = await apiBaseFetch('/auth/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, email, password })
        })
        const json = await res.json()
        if (json.error || json.code !== 200) throw new Error(json.message ?? 'Registration failed')

        user.value = json.data
        initialized.value = true
        router.push('/')
    }

    const login = async (username: string, password: string) => {
        const res = await apiBaseFetch('/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ login: username, password })
        })

        const json = await res.json()
        console.log('login response:', json)
        if (json.error || json.code !== 200) throw new Error(json.message ?? 'Login failed')

        user.value = json.data
        initialized.value = true

        router.push('/')
    }

    const logout = async () => {
        await apiBaseFetch('/auth/logout', { method: 'POST' })
        user.value = null
        router.push('/login')
    }

    const fetchMe = async () => {
        try {
            const res = await apiBaseFetch('/auth/me')
            const json = await res.json()
            if (json.code === 200) user.value = json.data
            else user.value = null
        } catch {
            user.value = null
        } finally {
            initialized.value = true
        }
    }
    return { user, isAuthenticated, initialized, register, login, logout, fetchMe }
}