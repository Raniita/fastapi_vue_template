import 'bootstrap/dist/css/bootstrap.css';
import axios from 'axios';

import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:5000/';  // Endpoint fastapi backend

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');
