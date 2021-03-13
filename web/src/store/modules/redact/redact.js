/* eslint-disable camelcase */

import _ from 'lodash'
import api from '@/api/redact/redact'
import { PolicyActions } from '@/utils'

const SET_POLICIES = 'SET_POLICIES'
const SET_EXPRESSIONS = 'SET_EXPRESSIONS'
const CREATE_EXPRESSION = 'CREATE_EXPRESSION'
const UPDATE_EXPRESSION = 'UPDATE_EXPRESSION'
const SET_FUNCTION_TYPES = 'SET_FUNCTION_TYPES'
const SET_FUNCTION_PARAMETERS = 'SET_FUNCTION_PARAMETERS'
const CREATE_POLICY = 'CREATE_POLICY'
const SET_COLUMNS = 'SET_COLUMNS'
const DROP_COLUMN = 'DROP_COLUMN'
const ADD_COLUMN = 'ADD_COLUMN'
const MODIFY_EXPRESSION = 'MODIFY_EXPRESSION'
const DROP_EXPRESSION = 'DROP_EXPRESSION'

const state = {
  policies: [],
  expressions: [],
  functionTypes: [],
  functionParameters: [],
  columns: []
}

const getters = {
  policies: state => state.policies,
  expressions: state => state.expressions,
  isExpressionsEmpty: state => state.expressions.length === 0,
  functionTypes: state => state.functionTypes,
  functionParameters: state => state.functionParameters,
  redactionColumns: state => state.columns
}

const actions = {
  getFunctionParameters ({ commit }) {
    return api.getFunctionParameters().then(result => {
      commit(SET_FUNCTION_PARAMETERS, result)
      return result
    })
  },
  getFunctionTypes ({ commit }) {
    return api.getFunctionTypes().then(result => {
      commit(SET_FUNCTION_TYPES, result)
      return result
    })
  },
  getPolicies ({ commit, rootGetters }, connectionId) {
    const connId = connectionId ?? rootGetters['app/connectionId']
    return api.getPolicies(connId).then(result => {
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
  dropExpression ({ commit, rootGetters }, { connectionId, ...params }) {
    const connId = connectionId ?? rootGetters['app/connectionId']
    return api.dropExpression({ connId, ...params }).then(result => {
      commit(DROP_EXPRESSION, params)
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
  },
  createPolicy ({ commit, rootGetters }, { connectionId, ...params }) {
    const connId = connectionId ?? rootGetters['app/connectionId']
    return api.createPolicy({ connId, ...params }).then(result => {
      commit(CREATE_POLICY, result)
      return result
    })
  },
  getRedactionColumns ({ commit, rootGetters }, { connectionId, ...params } = {}) {
    const connId = connectionId ?? rootGetters['app/connectionId']
    return api.getColumns({ connId, ...params }).then(result => {
      commit(SET_COLUMNS, result)
      return result
    })
  },
  alterPolicy ({ commit, rootGetters }, { connectionId, ...params } = {}) {
    const connId = connectionId ?? rootGetters['app/connectionId']
    return api.alterPolicy({ connId, ...params }).then(result => {
      switch (params.action) {
        case PolicyActions.DROP_COLUMN:
          commit(DROP_COLUMN, params)
          break
        case PolicyActions.ADD_COLUMN:
          commit(ADD_COLUMN, params)
          break
        case PolicyActions.MODIFY_EXPRESSION:
          commit(MODIFY_EXPRESSION, params)
          break
      }
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
  },
  [SET_FUNCTION_TYPES]: (state, data) => {
    state.functionTypes = data
  },
  [SET_FUNCTION_PARAMETERS]: (state, data) => {
    state.functionParameters = data
  },
  [CREATE_POLICY]: (state, data) => {
    state.policies.push(data)
  },
  [SET_COLUMNS]: (state, data) => {
    state.columns = data
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
    console.log(i)
    if (i > -1) {
      state.columns[i].expression = expression
    }
  },
  [DROP_EXPRESSION]: (state, { policy_expression_name }) => {
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
