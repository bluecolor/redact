/* eslint-disable camelcase */

import api from '@/api/vendors/oracle/redact/redaction'

const state = {
}

const getters = {
}

const actions = {
  askRedactionColumns ({ rootGetters }, payload) {
    return api.askColumns(rootGetters['app/connectionId'], payload)
  },
  askRedactionInfo ({ rootGetters }, params) {
    return api.askInfo(rootGetters['app/connectionId'], params)
  },
  askRedactionPolicy ({ rootGetters }, params) {
    return api.askPolicy(rootGetters['app/connectionId'], params)
  },
  askRedactionExpression ({ rootGetters }, params) {
    return api.askExpression(rootGetters['app/connectionId'], params)
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
