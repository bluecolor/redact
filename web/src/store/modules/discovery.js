/* eslint-disable camelcase */

import api from '@/api/discovery'

const SET_RULES = 'SET_RULES'
const CREATE_RULE = 'CREATE_RULE'
const SET_PLANS = 'SET_PLANS'
const CREATE_PLAN = 'CREATE_PLAN'

const state = {
  rules: [],
  plans: []
}

const getters = {
  rules: state => state.rules,
  plans: state => state.plans
}

const actions = {
  getRules ({ commit, rootGetters }) {
    return api.getRules(rootGetters['app/connectionId']).then(result => {
      commit(SET_RULES, result)
      return result
    })
  },
  createRule ({ commit, rootGetters }, payload) {
    return api.createRule(rootGetters['app/connectionId'], payload).then(result => {
      commit(CREATE_RULE, result)
      return result
    })
  },
  getPlans ({ commit, rootGetters }) {
    return api.getPlans(rootGetters['app/connectionId']).then(result => {
      commit(SET_PLANS, result)
      return result
    })
  }
}

const mutations = {
  [SET_RULES]: (state, data) => {
    state.rules = data
  },
  [CREATE_RULE]: (state, data) => {
    state.rules.push(data)
  },
  [SET_PLANS]: (state, data) => {
    state.plans = data
  },
  [CREATE_PLAN]: (state, data) => {
    state.plans.push(data)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
