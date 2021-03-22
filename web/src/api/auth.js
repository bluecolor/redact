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
  }
}
