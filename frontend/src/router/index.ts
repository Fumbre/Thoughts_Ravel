import { createRouter, createWebHistory } from 'vue-router'
import { useAuth } from '@/hooks/useAuth'
import LoginView from '@/views/auth/LoginView.vue'
import RegisterView from '@/views/auth/RegisterView.vue'
import SpaceView from '@/views/SpaceView.vue'
import InsideSpaceView from '@/views/InsideSpaceView.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/login', component: LoginView, meta: { public: true } },
        { path: '/register', component: RegisterView, meta: { public: true } },
        { path: '/', component: SpaceView },
        { path: '/space/:id', component: InsideSpaceView },
    ]
})

router.beforeEach(async (to) => {
    const { isAuthenticated, fetchMe } = useAuth()

    // check auth status on every navigation
    if (!isAuthenticated.value) await fetchMe()

    // redirect to login if not authenticated and route is not public
    if (!isAuthenticated.value && !to.meta.public) return '/login'

    // redirect to home if already logged in and hitting login/register
    if (isAuthenticated.value && to.meta.public) return '/'
})

export default router