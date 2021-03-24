/* eslint-disable camelcase */

import _ from 'lodash'
import api from '@/api/discovery/plan'

const SET_PLANS = 'SET_PLANS'
const CREATE = 'CREATE'
const UPDATE = 'UPDATE'
const DELETE = 'DELETE'
const SET_STATUS = 'SET_STATUS'
const SET_PLAN = 'SET_PLAN'

const state = {
  plans: []
}

const getters = {
  plans: state => state.plans
}

const actions = {
  getPlans ({ commit, rootGetters }) {
    return api.getAll(rootGetters['app/connectionId']).then(result => {
      commit(SET_PLANS, result)
      return result
    })
  },
  getPlan ({ rootGetters }, id) {
    return api.getOne(rootGetters['app/connectionId'], id)
  },
  reloadPlan ({ commit, rootGetters }, id) {
    return api.getOne(rootGetters['app/connectionId'], id).then(result => {
      commit(SET_PLAN, result)
      return result
    })
  },
  createPlan ({ commit, rootGetters }, payload) {
    return api.create(rootGetters['app/connectionId'], payload).then(result => {
      commit(CREATE, result)
      return result
    })
  },
  updatePlan ({ commit, rootGetters }, payload) {
    const { id } = payload
    return api.update(rootGetters['app/connectionId'], id, payload).then(result => {
      commit(UPDATE, result)
      return result
    })
  },
  deletePlan ({ commit, rootGetters }, id) {
    return api.delete(rootGetters['app/connectionId'], id).then(result => {
      commit(DELETE, id)
      return result
    })
  },
  runPlan ({ commit, rootGetters }, id) {
    return api.run(rootGetters['app/connectionId'], id).then(result => {
      commit(SET_STATUS, { id, status: 'running' })
      return result
    })
  },
  getLastInstance ({ commit, rootGetters }, id) {
    return api.getLastInstance(rootGetters['app/connectionId'], id)
  }
}

const mutations = {
  [SET_PLANS]: (state, data) => {
    state.plans = data
  },
  [CREATE]: (state, data) => {
    state.plans.push(data)
  },
  [UPDATE]: (state, data) => {
    const { id } = data
    const i = _.findIndex(state.plans, { id })
    if (i > -1) {
      state.plans.splice(i, 1, data)
    }
  },
  [DELETE]: (state, id) => {
    const i = _.findIndex(state.plans, { id })
    if (i > -1) {
      state.plans.splice(i, 1)
    }
  },
  [SET_STATUS]: (state, { id, status }) => {
    const plan = _.find(state.plans, { id })
    if (plan) { plan.status = status }
  },
  [SET_PLAN]: (state, data) => {
    const { id } = data
    const i = _.findIndex(state.plans, { id })
    if (i > -1) {
      state.plans.splice(i, 1, data)
    } else {
      state.plans.push(data)
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
