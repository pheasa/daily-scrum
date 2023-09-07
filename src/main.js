import 'bootstrap/dist/css/bootstrap.min.css'
import './assets/main.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import 'bootstrap'

const app = createApp(App)
app.config.globalProperties.$apiURL = 'https://my.api.mockaroo.com/new-task?key=b726ea10'

import 'bootstrap/dist/js/bootstrap.js'

app.use(createPinia())
app.use(router)

app.mount('#app')
