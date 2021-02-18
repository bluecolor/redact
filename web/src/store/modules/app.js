/* eslint-disable camelcase */

const SET_CONNECTION = 'SET_CONNECTION'

const state = {
  connectionId: undefined
}

const getters = {
  connectionId: state => state.connectionId
}

const actions = {
  setConnection ({ commit }, connectionId) {
    commit(SET_CONNECTION, connectionId)
  }
}

const mutations = {
  [SET_CONNECTION]: (state, connectionId) => {
    state.connectionId = connectionId
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
