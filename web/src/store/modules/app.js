/* eslint-disable camelcase */

import _ from 'lodash'
import api from '@/api/app'

const SET_CONNECTION = 'SET_CONNECTION'
const SET_TITLE = 'SET_TITLE'
const SET_VERSION = 'SET_VERSION'

const state = {
  connectionId: undefined,
  title: {
    isLoading: false,
    text: undefined
  },
  version: undefined
}

const getters = {
  connectionId: state => state.connectionId,
  connection: (state, getters, rootState, rootGetters) => {
    return _.find(rootGetters['connection/connections'], { id: getters.connectionId })
  },
  title: state => state.title
}

const actions = {
  setConnection ({ commit }, connectionId) {
    commit(SET_CONNECTION, connectionId)
  },
  setTitle ({ commit }, title) {
    commit(SET_TITLE, title)
  },
  getVersion ({ commit }) {
    return api.getVersion().then(result => {
      commit(SET_VERSION, result)
      return result
    })
  }
}

const mutations = {
  [SET_CONNECTION]: (state, connectionId) => {
    state.connectionId = connectionId
  },
  [SET_TITLE]: (state, title) => {
    state.title = title
  },
  [SET_VERSION]: (state, data) => {
    state.version = data
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
