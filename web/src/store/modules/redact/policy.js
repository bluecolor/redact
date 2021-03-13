/* eslint-disable camelcase */

import _ from 'lodash'
import api from '@/api/redact/policy'
import { PolicyActions } from '@/utils'

const SET_ALL = 'SET_ALL'
const CREATE = 'CREATE'
const DELETE = 'DELETE'
const DROP_COLUMN = 'DROP_COLUMN'
const ADD_COLUMN = 'ADD_COLUMN'
const MODIFY_EXPRESSION = 'MODIFY_EXPRESSION'

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
  createPolicy ({ commit, rootGetters }, payload) {
    return api.create(rootGetters['app/connectionId'], payload).then(result => {
      commit(CREATE, result)
      return result
    })
  },
  deletePolicy ({ commit, rootGetters }, payload) {
    return api.delete(rootGetters['app/connectionId'], payload).then(result => {
      commit(DELETE, payload)
      return result
    })
  },
  updatePolicy ({ commit, rootGetters }, payload) {
    return api.update(rootGetters['app/connectionId'], payload).then(result => {
      switch (payload.action) {
        case PolicyActions.DROP_COLUMN:
          commit(DROP_COLUMN, payload)
          break
        case PolicyActions.ADD_COLUMN:
          commit(ADD_COLUMN, payload)
          break
        case PolicyActions.MODIFY_EXPRESSION:
          commit(MODIFY_EXPRESSION, payload)
          break
      }
      return result
    })
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
  [DROP_COLUMN]: (state, { object_name, object_schema, column_name }) => {
    const i = _.findIndex(state.columns, { object_name, object_schema, column_name })
    if (i > -1) {
      state.columns.splice(i, 1)
    }
  },
  [ADD_COLUMN]: (state, data) => {
    state.columns.push(data)
  },
  [MODIFY_EXPRESSION]: (state, { object_name, object_schema, column_name, expression }) => {
    const i = _.findIndex(state.columns, { object_name, object_schema, column_name })
    if (i > -1) {
      state.columns[i].expression = expression
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
