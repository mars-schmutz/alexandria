import { createApp } from 'vue'
import { createPinia } from 'pinia'
// import { store } from '../myStore.js'

import App from '@/App.vue'
import MyLibrary from './MyLibrary.vue'
import router from './router'

import './assets/main.css'

const app = createApp(MyLibrary)
// const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')