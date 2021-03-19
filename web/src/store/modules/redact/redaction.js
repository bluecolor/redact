/* eslint-disable camelcase */

import api from '@/api/redact/redaction'

const state = {
}

const getters = {
}

const actions = {
  askRedactionColumns ({ commit, rootGetters }, payload) {
    return api.askColumns(rootGetters['app/connectionId'], payload)
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
