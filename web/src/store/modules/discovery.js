/* eslint-disable camelcase */

import _ from 'lodash'
import api from '@/api/discovery'

const SET_RULES = 'SET_RULES'
const CREATE_RULE = 'CREATE_RULE'
const SET_PLANS = 'SET_PLANS'
const CREATE_PLAN = 'CREATE_PLAN'
const DELETE_PLAN = 'DELETE_PLAN'
const DELETE_RULE = 'DELETE_RULE'
const SET_PLAN_STATUS = 'SET_PLAN_STATUS'

const state = {
  rules: [],
  plans: []
}

const getters = {
  rules: state => state.rules,
  plans: state => state.plans,
  planInstances: state => state.planInstances
}

const actions = {
  getRule ({ rootGetters }, id) {
    return api.getRule(rootGetters['app/connectionId'], id)
  },
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
  deleteRule ({ commit, rootGetters }, id) {
    return api.deleteRule(rootGetters['app/connectionId'], id).then(result => {
      commit(DELETE_RULE, id)
      return result
    })
  },
  getPlans ({ commit, rootGetters }) {
    return api.getPlans(rootGetters['app/connectionId']).then(result => {
      commit(SET_PLANS, result)
      return result
    })
  },
  createPlan ({ commit, rootGetters }, payload) {
    return api.createPlan(rootGetters['app/connectionId'], payload).then(result => {
      commit(CREATE_PLAN, result)
      return result
    })
  },
  deletePlan ({ commit, rootGetters }, id) {
    return api.deletePlan(rootGetters['app/connectionId'], id).then(result => {
      commit(DELETE_PLAN, id)
      return result
    })
  },
  runPlan ({ commit, rootGetters }, id) {
    return api.runPlan(rootGetters['app/connectionId'], id).then(result => {
      commit(SET_PLAN_STATUS, result)
      return result
    })
  },
  getPlanInstances ({ commit, rootGetters }, { planId }) {
    return api.getPlanInstances(rootGetters['app/connectionId'], planId)
  },
  getPlanInstance ({ rootGetters }, id) {
    return api.getPlanInstance(rootGetters['app/connectionId'], id)
  },
  getDiscoveries ({ rootGetters }, { planInstanceId, query }) {
    return api.getDiscoveries(rootGetters['app/connectionId'], planInstanceId, query)
  },
  getDiscoveriesForRule ({ rootGetters }, { planId, planInstanceId, ruleId, query }) {
    return api.getDiscoveriesForRule(rootGetters['app/connectionId'], planId, planInstanceId, ruleId, query)
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
  },
  [DELETE_PLAN]: (state, id) => {
    const i = _.findIndex(state.plans, { id })
    if (i > -1) {
      state.plans.splice(i, 1)
    }
  },
  [DELETE_RULE]: (state, id) => {
    const i = _.findIndex(state.rules, { id })
    if (i > -1) {
      state.rules.splice(i, 1)
    }
  },
  [SET_PLAN_STATUS]: (state, { id, status }) => {
    const plan = _.find(this.plans, { id })
    plan.status = status
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
