/* eslint-disable camelcase */

// import _ from 'lodash'
import api from '@/api/category'

const SET_ALL_CATEGORIES = 'SET_ALL_CATEGORIES'

const state = {
  categories: []
}

const getters = {
  categories: state => state.categories
}

const actions = {
  getAllCategories ({ commit }, connectionId) {
    return api.getAllCategories(connectionId).then(result => {
      commit(SET_ALL_CATEGORIES, result)
      return result
    })
  }
}

const mutations = {
  [SET_ALL_CATEGORIES]: (state, data) => {
    state.categories = data
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
