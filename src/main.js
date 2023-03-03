import { createApp } from 'vue'
import { createPinia } from 'pinia'

// import App from './App.vue'
import MyLibrary from './MyLibrary.vue'
import router from './router'

import './assets/main.css'

const app = createApp(MyLibrary)

app.use(createPinia())
app.use(router)

app.mount('#app')
