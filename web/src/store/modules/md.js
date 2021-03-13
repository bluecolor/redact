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
  getSchemas ({ commit, rootGetters }, connectionId) {
    const connId = connectionId ?? rootGetters['app/connectionId']
    return api.getObjectSchemas(connId).then(result => {
      commit(SET_OBJECT_SCHEMAS, result)
      return result
    })
  },
  getTables ({ rootGetters }, owner) {
    return api.getTables(rootGetters['app/connectionId'], owner)
  },
  getColumns ({ rootGetters }, { object_schema, object_name }) {
    return api.getColumns(rootGetters['app/connectionId'], object_schema, object_name)
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
