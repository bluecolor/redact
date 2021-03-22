/* eslint-disable camelcase */
import Cookies from 'js-cookie'
import api from '@/api/auth'

const LOGIN = 'LOGIN'
const LOGOUT = 'LOGOUT'

const state = {
  access_token: undefined
}

const getters = {
  access_token: state => state.access_token
}

const actions = {
  login ({ commit }, { username, password }) {
    return api.login(username, password).then(result => {
      commit(LOGIN, result)
      return result
    })
  },
  logout ({ commit }) {
    commit(LOGOUT)
  }
}

const mutations = {
  [LOGIN]: (state, { access_token }) => {
    state.access_token = access_token
    Cookies.set('access_token', access_token)
  },
  [LOGOUT]: (state) => {
    state.access_token = undefined
    Cookies.remove('access_token')
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
