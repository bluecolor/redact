import request from './request'

import _ from 'lodash'

export default {
  create (payload) {
    return request.post('/connections', payload)
  },
  getAll () {
    return request.get('/connections')
  },
  getOne (id) {
    return request.get(`/connections/${id}`)
  },
  delete (id) {
    return request.delete(`/connections/${id}`)
  },
  test (payload) {
    if (_.isObject(payload)) {
      return request.post('/connections/test', payload)
    } else {
      return request.get(`/connections/${payload}/test`)
    }
  },
  update (payload) {
    const { id } = payload
    return request.put(`/connections/${id}`, payload)
  }

}
