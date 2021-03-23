/* eslint-disable camelcase */
import _ from 'lodash'
import api from '@/api/appsetting'

const SET_ALL = 'SET_ALL'
const SET = 'SET'

const state = {
  settings: []
}

const getters = {
  settings: state => state.settings
}

const actions = {
  getAppSettings ({ commit }) {
    return api.getAll().then(result => {
      commit(SET_ALL, result)
      return result
    })
  },
  setAppSetting ({ commit }, payload) {
    return api.set(payload).then(result => {
      commit(SET, result)
      return result
    })
  },
  setAppSettings ({ commit }, payload) {
    return api.setAll(payload).then(result => {
      commit(SET_ALL, payload)
      return result
    })
  }
}

const mutations = {
  [SET_ALL]: (state, data) => {
    state.settings = data
  },
  [SET]: (state, data) => {
    const { name } = data
    let s = _.find(state.settings, { name })
    if (s) {
      s = data
    } else {
      state.settings.push(data)
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
