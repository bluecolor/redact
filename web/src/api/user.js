/* eslint-disable camelcase */
import request from './request'

export default {
  login (username, password) {
    const data = new FormData()
    data.append('username', username)
    data.append('password', password)
    return request({
      method: 'post',
      url: '/auth/login',
      data,
      headers: { 'Content-Type': 'multipart/form-data' }
    })
  },
  getOne (id) {
    return request.get(`/users/${id}`)
  },
  getAll () {
    return request.get('/users')
  },
  create (payload) {
    return request.post('/users', payload)
  },
  update (payload) {
    const { id } = payload
    return request.put(`/users/${id}`, payload)
  },
  delete (id) {
    return request.delete(`/users/${id}`)
  },
  regenerateApiKey (id) {
    return request.put(`/users/${id}/api-key`)
  },
  getMe () {
    return request.get('/users/me')
  },
  setPreferences (payload) {
    return request.put('/users/preferences', payload)
  }
}
