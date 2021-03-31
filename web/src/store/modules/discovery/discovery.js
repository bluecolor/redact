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
  getDiscoveriesGroupBySchema ({ rootGetters }, { planId, planInstanceId }) {
    return api.getAllGroupBySchema(rootGetters['app/connectionId'], planId, planInstanceId)
  },
  getDiscoveries ({ rootGetters }, { planId, planInstanceId, query }) {
    return api.getAll(rootGetters['app/connectionId'], planId, planInstanceId, query)
  },
  getDiscoveriesByRule ({ rootGetters }, { planId, planInstanceId, ruleId, query }) {
    return api.getAllByRule(rootGetters['app/connectionId'], planId, planInstanceId, ruleId, query)
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
