import Toasted from 'vue-toasted'

export default {
  install (Vue, options) {
    Vue.use(Toasted, options)
    Vue.prototype.$toast = Vue.prototype.$toasted
  }
}
