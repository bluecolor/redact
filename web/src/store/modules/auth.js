/* eslint-disable camelcase */

import { v4 as uuidv4 } from 'uuid'
import Cookies from 'js-cookie'
import api from '@/api/auth'

const LOGIN = 'LOGIN'
const LOGOUT = 'LOGOUT'

const state = {
  access_token: undefined,
  current_user: {
    avatar_url: `https://avatars.dicebear.com/4.5/api/identicon/${uuidv4()}.svg?r=50&m=15`
  }
}

const getters = {
  access_token: state => state.access_token,
  current_user: state => state.current_user
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
    return Promise.resolve()
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
