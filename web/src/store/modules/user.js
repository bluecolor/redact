/* eslint-disable camelcase */

import _ from 'lodash'
import api from '@/api/user'

const CREATE = 'CREATE'
const UPDATE = 'UPDATE'
const DELETE = 'DELETE'
const SET_ALL = 'SET_ALL'

const state = {
  users: []
}

const getters = {
  users: state => state.users
}

const actions = {

  createUser ({ commit }, payload) {
    return api.create(payload).then(result => {
      commit(CREATE, result)
      return result
    })
  },
  getUsers ({ commit }) {
    return api.getAll().then(result => {
      commit(SET_ALL, result)
      return result
    })
  },
  getUser ({ commit }, id) {
    return api.getOne(id)
  },
  updateUser ({ commit }, payload) {
    return api.udpate(payload).then(result => {
      commit(UPDATE, result)
      return result
    })
  },
  deleteUser ({ commit }, payload) {
    return api.delete(payload).then(result => {
      commit(DELETE, result)
      return result
    })
  }
}

const mutations = {
  [CREATE]: (state, data) => {
    state.users.push(data)
  },
  [SET_ALL]: (state, data) => {
    if (data) {
      state.users = data
    }
  },
  [UPDATE]: (state, data) => {
    const { id } = data
    const i = _.findIndex(state.users, { id })
    if (i > -1) {
      state.users.splice(i, 1, data)
    }
  },
  [DELETE]: (state, data) => {
    const { id } = data
    const i = _.findIndex(state.users, { id })
    if (i > -1) {
      state.users.splice(i, 1)
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
