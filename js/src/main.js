import Vue from "vue";
import Vuetify from "vuetify";
import VDateRange from "vuetify-daterange-picker";
import "vuetify-daterange-picker/dist/vuetify-daterange-picker.css";

import "vuetify/dist/vuetify.min.css";
import App from "./App.vue";

Vue.config.productionTip = false;
Vue.use(Vuetify);
Vue.use(VDateRange);

new Vue({
  render: h => h(App)
}).$mount("#app");
