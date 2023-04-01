import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000/api'
axios.defaults.headers.common['Authorization'] = 'Bearer ' + store.state.token
axios.defaults.headers.post['Content-Type'] = 'application/json'
axios.defaults.timeout = 1000


createApp(App).use(store).use(router, axios).mount('#app')
