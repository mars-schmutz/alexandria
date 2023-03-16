import { createRouter, createWebHashHistory } from 'vue-router'
import ShelfView from '../views/ShelfView.vue'

const router = createRouter({
    history: createWebHashHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "shelf",
            component: ShelfView
        },
        {
            path: "/add",
            name: "add",
            component: () => import('../views/AddAssetView.vue')
        },
        {
            path: "/settings",
            name: "settings",
            component: () => import('../views/SettingsView.vue')
        },
        {
            path: "/details/:id",
            name: "details",
            component: () => import('../views/DetailView.vue'),
        }
    ]
})

export default router