import { createRouter, createWebHashHistory } from 'vue-router'
import ShelfView from '../views/ShelfView.vue'

const router = createRouter({
    history: createWebHashHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "shelf",
            component: ShelfView
        }
    ]
})

export default router