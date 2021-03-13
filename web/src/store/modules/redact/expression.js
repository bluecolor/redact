/* eslint-disable camelcase */

import _ from 'lodash'
import api from '@/api/redact/expression'

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
  getExpressions ({ commit }, connectionId) {
    return api.getAll(connectionId).then(result => {
      commit(SET_ALL, result)
      return result
    })
  },
  createExpression ({ commit }, params) {
    return api.create(params).then(result => {
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
  getExpression ({ commit }, payload) {
    return api.getOne(payload)
  },
  updateExpression ({ commit }, params) {
    return api.update(params).then(result => {
      commit(UPDATE, result)
      return result
    })
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
