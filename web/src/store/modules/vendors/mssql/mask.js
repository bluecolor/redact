/* eslint-disable camelcase */

import api from '@/api/vendors/mssql/mask'

const state = {
}

const getters = {
}

const actions = {
  getMaskedColumns ({ commit, rootGetters }, params) {
    return api.getMaskedColumns(rootGetters['app/connectionId'], params)
  },
  getMaskingFunctions ({ commit }) {
    return api.getMaskingFunctions()
  },
  addMask ({ rootGetters }, payload) {
    return api.addMask(rootGetters['app/connectionId'], payload)
  },
  dropMask ({ rootGetters }, params) {
    return api.dropMask(rootGetters['app/connectionId'], params)
  }
}

const mutations = {
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
