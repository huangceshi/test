// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";
import App from "./App";
import router from "./router";
import store from "./store";
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
import axios from "axios";
import { get, post, del, put, patch } from "./util/http";
Vue.prototype.$http = axios;

Vue.prototype.$get = get;
Vue.prototype.$post = post;
Vue.prototype.$del = del;
Vue.prototype.$put = put;
Vue.prototype.$patch = patch;

Vue.config.productionTip = false;
Vue.use(ElementUI);

new Vue({
  el: "#app",
  router,
  store,
  components: { App },
  template: "<App/>"
});
