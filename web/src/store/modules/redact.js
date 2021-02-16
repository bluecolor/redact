/* eslint-disable camelcase */

import _ from 'lodash'
import api from '@/api/redact'

const SET_POLICIES = 'SET_POLICIES'
const SET_EXPRESSIONS = 'SET_EXPRESSIONS'
const CREATE_EXPRESSION = 'CREATE_EXPRESSION'
const UPDATE_EXPRESSION = 'UPDATE_EXPRESSION'

const state = {
  policies: [],
  expressions: []
}

const getters = {
  policies: state => state.policies,
  expressions: state => state.expressions,
  isExpressionsEmpty: state => state.expressions.length === 0
}

const actions = {
  getPolicies ({ commit }, connectionId) {
    return api.getPolicies(connectionId).then(result => {
      commit(SET_POLICIES, result)
      return result
    })
  },
  getExpressions ({ commit }, connectionId) {
    return api.getExpressions(connectionId).then(result => {
      commit(SET_EXPRESSIONS, result)
      return result
    })
  },
  createExpression ({ commit }, params) {
    return api.createExpression(params).then(result => {
      commit(CREATE_EXPRESSION, result)
      return result
    })
  },
  getExpression ({ commit }, payload) {
    return api.getExpression(payload)
  },
  updateExpression ({ commit }, params) {
    return api.updateExpression(params).then(result => {
      commit(UPDATE_EXPRESSION, result)
      return result
    })
  }
}

const mutations = {
  [SET_POLICIES]: (state, data) => {
    state.policies = data
  },
  [SET_EXPRESSIONS]: (state, data) => {
    state.expressions = data
  },
  [CREATE_EXPRESSION]: (state, data) => {
    state.expressions.push(data)
  },
  [UPDATE_EXPRESSION]: (state, data) => {
    const { policy_expression_name } = data
    const i = _.findIndex(state.expressions, { policy_expression_name })
    if (i !== -1) {
      state.expressions.splice(i, 1, data)
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
