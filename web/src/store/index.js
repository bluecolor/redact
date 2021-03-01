import Vue from 'vue'
import Vuex from 'vuex'

import connection from './modules/connection'
import category from './modules/category'
import redact from './modules/redact'
import app from './modules/app'
import md from './modules/md'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    connection, category, redact, app, md
  }
})
