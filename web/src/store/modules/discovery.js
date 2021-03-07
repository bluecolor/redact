/* eslint-disable camelcase */

import _ from 'lodash'
import api from '@/api/discovery'

const SET_RULES = 'SET_RULES'
const CREATE_RULE = 'CREATE_RULE'
const SET_PLANS = 'SET_PLANS'
const CREATE_PLAN = 'CREATE_PLAN'
const DELETE_PLAN = 'DELETE_PLAN'
const DELETE_RULE = 'DELETE_RULE'

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
  deletePlan ({ commit, rootGetters }, id) {
    return api.deletePlan(rootGetters['app/connectionId'], id).then(result => {
      commit(DELETE_PLAN, id)
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
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
