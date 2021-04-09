/* eslint-disable camelcase */

import _ from 'lodash'
import api from '@/api/oracle/redact/category'

const SET_ALL = 'SET_ALL'
const CREATE = 'CREATE'
const DELETE = 'DELETE'
const UPDATE = 'UPDATE'

const state = {
  categories: []
}

const getters = {
  categories: state => state.categories
}

const actions = {
  getCategories ({ commit, rootGetters }, connectionId) {
    return api.getAll(rootGetters['app/connectionId']).then(result => {
      commit(SET_ALL, result)
      return result
    })
  },
  getCategory ({ rootGetters }, id) {
    return api.getOne(rootGetters['app/connectionId'], id)
  },
  createCategory ({ commit, rootGetters }, payload) {
    return api.create(rootGetters['app/connectionId'], payload).then(result => {
      commit(CREATE, result)
      return result
    })
  },
  deleteCategory ({ commit, rootGetters }, id) {
    return api.delete(rootGetters['app/connectionId'], id).then(result => {
      commit(DELETE, result)
      return result
    })
  },
  updateCategory ({ commit, rootGetters }, payload) {
    return api.update(rootGetters['app/connectionId'], payload).then(result => {
      commit(UPDATE, result)
      return result
    })
  }
}

const mutations = {
  [SET_ALL]: (state, data) => {
    state.categories = data
  },
  [CREATE]: (state, data) => {
    state.categories.push(data)
  },
  [DELETE]: (state, { id }) => {
    const i = _.findIndex(state.categories, { id })
    if (i !== -1) {
      state.categories.splice(i, 1)
    }
  },
  [UPDATE]: (state, data) => {
    const { id } = data
    const i = _.findIndex(state.categories, { id })
    if (i !== -1) {
      state.categories.splice(i, 1, data)
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
