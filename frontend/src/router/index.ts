import { createRouter, createWebHistory } from 'vue-router'
import { useAuth } from '@/hooks/useAuth'
import LoginView from '@/views/auth/LoginView.vue'
import RegisterView from '@/views/auth/RegisterView.vue'
import SpaceView from '@/views/SpaceView.vue'
import InsideSpaceView from '@/views/InsideSpaceView.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [

        { path: '/login', component: LoginView, meta: { public: true, guestOnly: true } },
        { path: '/register', component: RegisterView, meta: { public: true, guestOnly: true } },
        { path: '/', component: SpaceView },
        { path: '/space/:id', component: InsideSpaceView },
    ]
})

router.beforeEach(async (to) => {
    const { isAuthenticated, initialized, fetchMe } = useAuth()

    if (!initialized.value) {
        await fetchMe()
    }

    const authed = isAuthenticated.value
    const isPublic = to.meta.public
    const isGuestOnly = to.meta.guestOnly

    console.log('user is', authed)

    // If not logged in and trying to access a protected route send to login
    if (!authed && !isPublic) return '/login'

    // If logged in and trying to access a GUEST-ONLY route (login/register) send to root
    if (authed && isGuestOnly) return '/'

    return true
})

export default router