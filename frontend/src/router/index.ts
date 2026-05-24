import { createRouter, createWebHistory } from 'vue-router'
import SpaceView from '@/views/SpaceView.vue'
import InsideSpaceView from '@/views/InsideSpaceView.vue'

export default createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: SpaceView },
        { path: '/space/:id', component: InsideSpaceView },
    ]
})