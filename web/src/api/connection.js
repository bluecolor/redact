import request from './request'

export default {
  create (payload) {
    return request.post('/connections', payload)
  },
  getAll () {
    return request.get('/connections')
  },
  delete (id) {
    return request.delete(`/connections/${id}`)
  }

}
