/* eslint-disable camelcase */

import _ from 'lodash'
import api from '@/api/oracle/redact/policy'

const SET_ALL = 'SET_ALL'
const CREATE = 'CREATE'
const DELETE = 'DELETE'
const ENABLE = 'ENABLE'
const DISABLE = 'DISABLE'

const state = {
  policies: []
}

const getters = {
  policies: state => state.policies
}

const actions = {
  getPolicies ({ commit, rootGetters }) {
    return api.getAll(rootGetters['app/connectionId']).then(result => {
      commit(SET_ALL, result)
      return result
    })
  },
  getPolicy ({ rootGetters }, q) {
    return api.getOne(rootGetters['app/connectionId'], q)
  },
  getPolicyOwners ({ rootGetters }) {
    return api.getOwners(rootGetters['app/connectionId'])
  },
  getPolicyTables ({ rootGetters }, owner) {
    return api.getTables(rootGetters['app/connectionId'], owner)
  },
  createPolicy ({ commit, rootGetters }, payload) {
    return api.create(rootGetters['app/connectionId'], payload).then(result => {
      return result
    })
  },
  deletePolicy ({ commit, rootGetters }, payload) {
    return api.delete(rootGetters['app/connectionId'], payload).then(result => {
      commit(DELETE, payload)
      return result
    })
  },
  disablePolicy ({ commit, rootGetters }, payload) {
    return api.disable(rootGetters['app/connectionId'], payload).then(result => {
      commit(DISABLE, payload)
      return result
    })
  },
  enablePolicy ({ commit, rootGetters }, payload) {
    return api.enable(rootGetters['app/connectionId'], payload).then(result => {
      commit(ENABLE, payload)
      return result
    })
  },
  updatePolicy ({ commit, rootGetters }, payload) {
    return api.update(rootGetters['app/connectionId'], payload)
  },
  askPolicyTables ({ rootGetters }, payload) {
    return api.askTables(rootGetters['app/connectionId'], payload)
  }
}

const mutations = {
  [SET_ALL]: (state, data) => {
    state.policies = data
  },
  [CREATE]: (state, data) => {
    state.policies.push(data)
  },
  [DELETE]: (state, { object_owner, object_name, policy_name }) => {
    const i = _.findIndex(state.policies, { object_owner, object_name, policy_name })
    if (i > -1) {
      state.policies.splice(i, 1)
    }
  },
  [DISABLE]: (state, { object_owner, object_name, policy_name }) => {
    const p = _.find(state.policies, { object_owner, object_name, policy_name })
    if (p) {
      p.enable = 'NO'
    }
  },
  [ENABLE]: (state, { object_owner, object_name, policy_name }) => {
    const p = _.find(state.policies, { object_owner, object_name, policy_name })
    if (p) {
      p.enable = 'YES'
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
