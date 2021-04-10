/* eslint-disable camelcase */

import _ from 'lodash'
import api from '@/api/vendors/oracle/redact/column'

const SET_ALL = 'SET_ALL'

const state = {
  columns: []
}

const getters = {
  columns: state => state.columns
}

const actions = {
  getColumns ({ commit, rootGetters }, q) {
    return api.getAll(rootGetters['app/connectionId'], q).then(result => {
      if (_.isEmpty(q)) { commit(SET_ALL, result) }
      return result
    })
  }
}

const mutations = {
  [SET_ALL]: (state, data) => {
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
