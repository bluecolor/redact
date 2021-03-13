/* eslint-disable camelcase */

import _ from 'lodash'
import api from '@/api/discovery/planInstance'

const SET_PLAN_INSTANCES = 'SET_PLAN_INSTANCES'
const DELETE = 'DELETE'
const STOP = 'STOP'

const state = {
  planInstances: []
}

const getters = {
  planInstances: state => state.planInstances
}

const actions = {
  getPlanInstancesByPlan ({ rootGetters }, { planId }) {
    return api.getAllByPlan(rootGetters['app/connectionId'], planId)
  },
  getAllPlanInstances ({ commit, rootGetters }) {
    return api.getAll(rootGetters['app/connectionId']).then(result => {
      commit(SET_PLAN_INSTANCES, result)
      return result
    })
  },
  getPlanInstance ({ rootGetters }, { planId, id }) {
    return api.getOne(rootGetters['app/connectionId'], planId, id)
  },
  deletePlanInstance ({ commit, rootGetters }, { planId, id }) {
    return api.delete(rootGetters['app/connectionId'], planId, id).then(result => {
      commit(DELETE, result)
      return result
    })
  },
  stopPlanInstance ({ commit, rootGetters }, { planId, id }) {
    return api.stop(rootGetters['app/connectionId'], planId, id).then(result => {
      commit(STOP, result)
      return result
    })
  }
}

const mutations = {
  [SET_PLAN_INSTANCES]: (state, data) => {
    state.planInstances = data
  },
  [DELETE]: (state, { id }) => {
    const i = _.findIndex(state.planInstances, { id })
    if (i > -1) {
      state.planInstances.splice(i, 1)
    }
  },
  [STOP]: (state, { id, status }) => {
    const p = _.find(state.planInstances, { id })
    if (p) {
      p.status = status
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
