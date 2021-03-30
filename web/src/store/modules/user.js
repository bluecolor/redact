/* eslint-disable camelcase */

import { v4 as uuidv4 } from 'uuid'
import Cookies from 'js-cookie'
import _ from 'lodash'
import api from '@/api/user'

const CREATE = 'CREATE'
const UPDATE = 'UPDATE'
const DELETE = 'DELETE'
const SET_ALL = 'SET_ALL'
const SET_PROFILE = 'SET_PROFILE'
const LOGIN = 'LOGIN'
const LOGOUT = 'LOGOUT'
const SET_PREFERENCES = 'SET_PREFERENCES'

const state = {
  users: [],
  access_token: '',
  current_user: {
    avatar_url: `https://avatars.dicebear.com/4.5/api/identicon/${uuidv4()}.svg?r=50&m=15`
  }
}

const getters = {
  users: state => state.users,
  access_token: state => state.access_token,
  current_user: state => state.current_user
}

const actions = {
  getMe ({ commit }) {
    return api.getMe().then(result => {
      commit(UPDATE, result)
      commit(SET_PROFILE, result)
      return result
    })
  },
  login ({ commit }, { username, password }) {
    return api.login(username, password).then(result => {
      commit(LOGIN, result)
      return result
    })
  },
  logout ({ commit }) {
    commit(LOGOUT)
    return Promise.resolve()
  },
  createUser ({ commit }, payload) {
    return api.create(payload).then(result => {
      commit(CREATE, result)
      return result
    })
  },
  getUsers ({ commit }) {
    return api.getAll().then(result => {
      commit(SET_ALL, result)
      return result
    })
  },
  getUser ({ commit }, id) {
    return api.getOne(id)
  },
  updateUser ({ commit }, payload) {
    return api.udpate(payload).then(result => {
      commit(UPDATE, result)
      return result
    })
  },
  deleteUser ({ commit }, payload) {
    return api.delete(payload).then(result => {
      commit(DELETE, result)
      return result
    })
  },
  regenerateApiKey ({ commit }, id) {
    return api.regenerateApiKey(id).then(result => {
      commit(UPDATE, result)
      return result
    })
  },
  setPreferences ({ commit }, payload) {
    return api.setPreferences(payload).then(result => {
      commit(SET_PREFERENCES, result)
      return result
    })
  }

}

const mutations = {
  [CREATE]: (state, data) => {
    state.users.push(data)
  },
  [SET_ALL]: (state, data) => {
    if (data) {
      state.users = data
    }
  },
  [UPDATE]: (state, data) => {
    const { id } = data
    const i = _.findIndex(state.users, { id })
    if (i > -1) {
      state.users.splice(i, 1, data)
    }
  },
  [DELETE]: (state, data) => {
    const { id } = data
    const i = _.findIndex(state.users, { id })
    if (i > -1) {
      state.users.splice(i, 1)
    }
  },
  [SET_PROFILE]: (state, data) => {
    state.current_user = { ...data, ...state.current_user }
  },
  [SET_PREFERENCES]: (state, { preferences }) => {
    state.current_user = { ...state.current_user, preferences }
  },
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
