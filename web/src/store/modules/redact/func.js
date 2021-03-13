/* eslint-disable camelcase */

import api from '@/api/redact/func'

const SET_TYPES = 'SET_TYPES'
const SET_PARAMETERS = 'SET_PARAMETERS'
const SET_ACTIONS = 'SET_ACTIONS'

const state = {
  types: [],
  parameters: [],
  actions: []
}

const getters = {
  functionTypes: state => state.types,
  functionParameters: state => state.parameters,
  actions: state => state.actions
}

const actions = {
  getFunctionParameters ({ commit }) {
    return api.getParameters().then(result => {
      commit(SET_PARAMETERS, result)
      return result
    })
  },
  getFunctionTypes ({ commit }) {
    return api.getTypes().then(result => {
      commit(SET_TYPES, result)
      return result
    })
  },
  getActions ({ commit }) {
    return api.getActions().then(result => {
      commit(SET_ACTIONS, result)
      return result
    })
  }
}

const mutations = {
  [SET_TYPES]: (state, data) => {
    state.types = data
  },
  [SET_PARAMETERS]: (state, data) => {
    state.parameters = data
  },
  [SET_ACTIONS]: (state, data) => {
    state.actions = data
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
