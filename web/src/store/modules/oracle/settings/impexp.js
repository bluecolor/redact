/* eslint-disable camelcase */

import api from '@/api/oracle/settings/impexp'

const state = {
}

const getters = {
}

const actions = {
  exportSettings ({ rootGetters }, payload) {
    return api.export(rootGetters['app/connectionId'], payload)
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
