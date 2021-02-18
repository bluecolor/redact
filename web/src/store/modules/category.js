/* eslint-disable camelcase */

// import _ from 'lodash'
import api from '@/api/category'

const SET_CATEGORIES = 'SET_CATEGORIES'
const CREATE = 'CREATE'

const state = {
  categories: []
}

const getters = {
  categories: state => state.categories,
  isCategoriesEmpty: state => state.categories.length === 0
}

const actions = {
  getCategories ({ commit }, connectionId) {
    return api.getCategories(connectionId).then(result => {
      commit(SET_CATEGORIES, result)
      return result
    })
  },
  createCategory ({ commit }, params) {
    return api.create(params).then(result => {
      commit(CREATE, result)
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
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
