/* eslint-disable camelcase */

const ADD = 'ADD'
const REMOVE = 'REMOVE'
const CLEAR = 'CLEAR'

const state = {
  notifications: []
}

const getters = {
  notifications: state => state.notifications
}

const actions = {
  addNotification ({ commit }, notification) {
    commit(ADD, notification)
  },
  removeNotification ({ commit }, index) {
    commit(REMOVE, index)
  },
  clearNotifications ({ commit }) {
    commit(CLEAR)
  }
}

const mutations = {
  [ADD]: (state, data) => {
    state.notifications.push(data)
  },
  [REMOVE]: (state, index) => {
    if (state.notifications[index]) {
      state.notifications.splice(index, 1)
    }
  },
  [CLEAR]: (state) => {
    state.notifications = []
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
