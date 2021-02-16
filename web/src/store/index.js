import { createStore } from 'vuex'
import connection from './modules/connection'
import redact from './modules/redact'
import category from './modules/category'

export default createStore({
  state: {
    count: 0
  },
  mutations: {
    INC (state, val) {
      state.count = val
    }
  },
  actions: {
    inc ({ commit }, payload) {
      commit('INC', payload)
    }
  },
  modules: {
    connection, redact, category
  }
})
