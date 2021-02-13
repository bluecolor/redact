import { createStore } from 'vuex'

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
  }
})
