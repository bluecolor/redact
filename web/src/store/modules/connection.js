/* eslint-disable camelcase */

import _ from 'lodash'
import api from '@/api/connection'

const CREATE = 'CREATE'
const SET_ALL = 'SET_ALL'
const DELETE = 'DELETE'

const state = {
  connections: []
}

const getters = {
  connections: state => state.connections,
  isConnectionsEmpty: state => state.connections.length === 0
}

const actions = {
  createConnection ({ commit }, payload) {
    return api.create(payload).then(result => {
      commit(CREATE, result)
      return result
    })
  },
  getConnections ({ commit }) {
    return api.getAll().then(result => {
      commit(SET_ALL, result)
      return result
    })
  },
  deleteConnection ({ commit }, id) {
    return api.delete(id).then(result => {
      commit(DELETE, id)
      return result
    })
  },
  testConnection ({ commit }, payload) {
    return api.test(payload)
  }
}

const mutations = {
  [CREATE]: (state, data) => {
    state.connections.push(data)
  },
  [SET_ALL]: (state, data) => {
    state.connections = data
  },
  [DELETE]: (state, id) => {
    const i = _.findIndex(state.connections, { id })
    if (i !== -1) {
      state.connections.splice(i, 1)
    }
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
