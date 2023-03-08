import { createApp } from 'vue'
import { createPinia } from 'pinia'
// import { store } from '../myStore.js'

// import App from './App.vue'
import MyLibrary from './MyLibrary.vue'
import router from './router'

import './assets/main.css'

const app = createApp(MyLibrary)

app.use(createPinia())
app.use(router)

// app.config.globalProperties.$store = store;
// app.use(store);

app.mount('#app')