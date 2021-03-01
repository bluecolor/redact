/* eslint-disable camelcase */

import api from '@/api/md'

const SET_OBJECT_SCHEMAS = 'SET_OBJECT_SCHEMAS'
const SET_TABLES = 'SET_TABLES'
const SET_COLUMNS = 'SET_COLUMNS'

const state = {
  objectSchemas: [],
  tables: [],
  columns: []
}

const getters = {
  objectSchemas: state => state.objectSchemas,
  tables: state => state.tables,
  columns: state => state.columns
}

const actions = {
  getObjectSchemas ({ commit, rootGetters }, connectionId) {
    const connId = connectionId ?? rootGetters['app/connectionId']
    return api.getObjectSchemas(connId).then(result => {
      commit(SET_OBJECT_SCHEMAS, result)
      return result
    })
  },
  getTables ({ commit, rootGetters }, params = {}) {
    const { connectionId, owner } = params
    const connId = connectionId ?? rootGetters['app/connectionId']
    return api.getTables(connId, owner).then(result => {
      commit(SET_TABLES, result)
      return result
    })
  },
  getColumns ({ commit, rootGetters }, params = {}) {
    const { connectionId, object_schema, object_name } = params
    const connId = connectionId ?? rootGetters['app/connectionId']
    return api.getColumns(connId, object_schema, object_name).then(result => {
      commit(SET_COLUMNS, result)
      return result
    })
  }
}

const mutations = {
  [SET_OBJECT_SCHEMAS]: (state, data) => {
    state.objectSchemas = data
  },
  [SET_TABLES]: (state, data) => {
    state.tables = data
  },
  [SET_COLUMNS]: (state, data) => {
    state.columns = data
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
