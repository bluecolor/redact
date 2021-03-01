/* eslint-disable camelcase */

import _ from 'lodash'
import api from '@/api/category'

const SET_CATEGORIES = 'SET_CATEGORIES'
const CREATE = 'CREATE'
const DELETE = 'DELETE'
const UPDATE = 'UPDATE'

const state = {
  categories: []
}

const getters = {
  categories: state => state.categories,
  isCategoriesEmpty: state => state.categories.length === 0
}

const actions = {
  getCategories ({ commit, rootGetters }, connectionId) {
    const connId = connectionId ?? rootGetters['app/connectionId']
    return api.getCategories(connId).then(result => {
      commit(SET_CATEGORIES, result)
      return result
    })
  },
  createCategory ({ commit }, params) {
    return api.create(params).then(result => {
      commit(CREATE, result)
      return result
    })
  },
  deleteCategory ({ commit, rootGetters }, params) {
    const connectionId = rootGetters['app/connectionId']
    return api.delete({ connectionId, ...params }).then(result => {
      commit(DELETE, result)
      return result
    })
  },
  updateCategory ({ commit, rootGetters }, params) {
    const connectionId = rootGetters['app/connectionId']
    return api.update({ connectionId, ...params }).then(result => {
      commit(UPDATE, result)
      return result
    })
  }
}

const mutations = {
  [SET_CATEGORIES]: (state, data) => {
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
