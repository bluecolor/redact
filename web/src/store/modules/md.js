/* eslint-disable camelcase */

import api from '@/api/md'

const SET_OBJECT_SCHEMAS = 'SET_OBJECT_SCHEMAS'

const state = {
  objectSchemas: []
}

const getters = {
  objectSchemas: state => state.objectSchemas,
  schemas: state => state.objectSchemas
}

const actions = {
  getObjectSchemas ({ commit, rootGetters }, connectionId) {
    const connId = connectionId ?? rootGetters['app/connectionId']
    return api.getObjectSchemas(connId).then(result => {
      commit(SET_OBJECT_SCHEMAS, result)
      return result
    })
  },
  getSchemas ({ rootGetters }) {
    return api.getSchemas(rootGetters['app/connectionId'])
  },
  getTables ({ rootGetters }, schema_name) {
    return api.getTables(rootGetters['app/connectionId'], schema_name)
  },
  getColumns ({ rootGetters }, { schema_name, table_name }) {
    return api.getColumns(rootGetters['app/connectionId'], schema_name, table_name)
  },
  searchMetadata ({ rootGetters }, q) {
    return api.search(rootGetters['app/connectionId'], q)
  },
  getColumnSample ({ rootGetters }, params) {
    return api.getColumnSample(rootGetters['app/connectionId'], params)
  }
}

const mutations = {
  [SET_OBJECT_SCHEMAS]: (state, data) => {
    state.objectSchemas = data
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
