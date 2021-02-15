import request from './request'

import _ from 'lodash'

export default {
  create (payload) {
    return request.post('/connections', payload)
  },
  getAll () {
    return request.get('/connections')
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
  }

}
