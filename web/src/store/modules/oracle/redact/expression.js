/* eslint-disable camelcase */

import _ from 'lodash'
import api from '@/api/oracle/redact/expression'

const SET_ALL = 'SET_ALL'
const CREATE = 'CREATE'
const UPDATE = 'UPDATE'
const DELETE = 'DELETE'

const state = {
  expressions: []
}

const getters = {
  expressions: state => state.expressions
}

const actions = {
  getExpressions ({ commit, rootGetters }, connectionId) {
    const connId = connectionId ?? rootGetters['app/connectionId']
    return api.getAll(connId).then(result => {
      commit(SET_ALL, result)
      return result
    })
  },
  createExpression ({ commit, rootGetters }, params) {
    return api.create(rootGetters['app/connectionId'], params).then(result => {
      commit(CREATE, result)
      return result
    })
  },
  deleteExpression ({ commit, rootGetters }, { policy_expression_name }) {
    return api.delete(rootGetters['app/connectionId'], policy_expression_name).then(result => {
      commit(DELETE, policy_expression_name)
      return result
    })
  },
  getExpression ({ commit, rootGetters }, policy_expression_name) {
    return api.getOne(rootGetters['app/connectionId'], policy_expression_name)
  },
  updateExpression ({ commit, rootGetters }, payload) {
    return api.update(rootGetters['app/connectionId'], payload).then(result => {
      commit(UPDATE, result)
      return result
    })
  },
  applyExpressionToColumn ({ rootGetters }, payload) {
    return api.apply(rootGetters['app/connectionId'], payload)
  }
}

const mutations = {
  [SET_ALL]: (state, data) => {
    state.expressions = data
  },
  [CREATE]: (state, data) => {
    state.expressions.push(data)
  },
  [UPDATE]: (state, data) => {
    const { policy_expression_name } = data
    const i = _.findIndex(state.expressions, { policy_expression_name })
    if (i !== -1) {
      state.expressions.splice(i, 1, data)
    }
  },
  [DELETE]: (state, policy_expression_name) => {
    const i = _.findIndex(state.expressions, { policy_expression_name })
    if (i > -1) {
      state.expressions.splice(i, 1)
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
