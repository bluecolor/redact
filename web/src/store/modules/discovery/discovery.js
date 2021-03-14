/* eslint-disable camelcase */

import api from '@/api/discovery/discovery'

const state = {
}

const getters = {
}

const actions = {
  getDiscoveriesGroupByRule ({ rootGetters }, { planId, planInstanceId }) {
    return api.getAllGroupByRule(rootGetters['app/connectionId'], planId, planInstanceId)
  },
  getDiscoveries ({ rootGetters }, { planId, planInstanceId, query }) {
    return api.getAll(rootGetters['app/connectionId'], planId, planInstanceId, query)
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
