/* eslint-disable camelcase */

import api from '@/api/redact/func'

const SET_TYPES = 'SET_TYPES'
const SET_PARAMETERS = 'SET_PARAMETERS'

const state = {
  types: [],
  parameters: []
}

const getters = {
  functionTypes: state => state.types,
  functionParameters: state => state.parameters
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
  }
}

const mutations = {
  [SET_TYPES]: (state, data) => {
    state.types = data
  },
  [SET_PARAMETERS]: (state, data) => {
    state.parameters = data
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
