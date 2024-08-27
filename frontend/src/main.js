import './plugins/axios'
import { createApp } from 'vue'
import App from './App.vue'
import store from './store'
import router from './router';
import axiosPlugin from './plugins/axios';



createApp(App).use(router).use(store).use(axiosPlugin).mount('#app')
