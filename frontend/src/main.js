import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import axios from "axios";
// import './assets/common.css'
// import { createApp } from 'vue'

Vue.prototype.$axios = axios;

Vue.config.productionTip = false

new Vue({
    router,
    axios,
    vuetify,
    render: h => h(App)
}).$mount('#app')
