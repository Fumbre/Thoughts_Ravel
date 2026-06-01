import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { apiBaseFetch } from '@/tools/api'

const user = ref<{ id: string, username: string } | null>(null)

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
        return json.data
    }

    const login = async (username: string, password: string) => {
        const res = await apiBaseFetch('/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            credentials: 'include',  // sends/receives cookies
            body: JSON.stringify({ username, password })
        })
        const json = await res.json()
        if (json.error || json.code !== 200) throw new Error(json.message ?? 'Login failed')
        user.value = json.data
        router.push('/')
    }

    const logout = async () => {
        await apiBaseFetch('/auth/logout', { method: 'POST', credentials: 'include' })
        user.value = null
        router.push('/login')
    }

    const fetchMe = async () => {
        try {
            const res = await apiBaseFetch('/auth/me', { credentials: 'include' })
            const json = await res.json()
            if (json.code === 200) user.value = json.data
        } catch {
            user.value = null
        }
    }

    return { user, isAuthenticated, register, login, logout, fetchMe }
}