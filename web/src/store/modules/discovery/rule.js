/* eslint-disable camelcase */

import _ from 'lodash'
import api from '@/api/discovery/rule'

const SET_ALL = 'SET_ALL'
const CREATE = 'CREATE'
const UPDATE = 'UPDATE'
const DELETE = 'DELETE'

const state = {
  rules: []
}

const getters = {
  rules: state => state.rules
}

const actions = {
  getRule ({ rootGetters }, id) {
    return api.getOne(rootGetters['app/connectionId'], id)
  },
  getRules ({ commit, rootGetters }) {
    return api.getAll(rootGetters['app/connectionId']).then(result => {
      commit(SET_ALL, result)
      return result
    })
  },
  createRule ({ commit, rootGetters }, payload) {
    return api.create(rootGetters['app/connectionId'], payload).then(result => {
      commit(CREATE, result)
      return result
    })
  },
  updateRule ({ commit, rootGetters }, payload) {
    return api.update(rootGetters['app/connectionId'], payload).then(result => {
      commit(UPDATE, result)
      return result
    })
  },
  deleteRule ({ commit, rootGetters }, id) {
    return api.delete(rootGetters['app/connectionId'], id).then(result => {
      commit(DELETE, id)
      return result
    })
  }
}

const mutations = {
  [SET_ALL]: (state, data) => {
    state.rules = data
  },
  [CREATE]: (state, data) => {
    state.rules.push(data)
  },
  [DELETE]: (state, id) => {
    const i = _.findIndex(state.rules, { id })
    if (i > -1) {
      state.rules.splice(i, 1)
    }
  },
  [UPDATE]: (state, data) => {
    const { id } = data
    const i = _.findIndex(state.rules, { id })
    if (i > -1) {
      state.rules.splice(i, 1, data)
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
