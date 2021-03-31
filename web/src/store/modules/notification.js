/* eslint-disable camelcase */

import _ from 'lodash'
const ADD = 'ADD'
const REMOVE = 'REMOVE'
const CLEAR = 'CLEAR'

const state = {
  notifications: [],
  icons: {
    plan_instance_start: 'las la-shipping-fast text-blue-400',
    plan_instance_error: 'la-info-circle las la-shipping-fast text-red-400',
    plan_instance_success: 'las la-shipping-fast text-green-400',
    plan_instance_done: 'las la-shipping-fast text-green-400',
    login: 'las la-user',
    logout: 'danger las la-user'
  }
}

const withLogin = (n) => {
  if (n.type === 'login') {
    const text = `${n.data.name} logged in`
    return { ...n, text }
  }
  return n
}

const getters = {
  notifications: state => {
    return _.map(state.notifications, n => {
      const icon = state.icons[n.type] ?? 'las la-info-circle'
      return withLogin({ ...n, icon })
    })
  }
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
