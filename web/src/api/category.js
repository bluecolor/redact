import request from '@/api/request'

export default {

  getOne (connId, id) {
    return request.get(`/connections/${connId}/categories/${id}`)
  },
  getAll (connId) {
    return request.get(`/connections/${connId}/categories`)
  },
  create (connId, payload) {
    return request.post(`/connections/${connId}/categories`, payload)
  },
  delete (connId, id) {
    return request.delete(`/connections/${connId}/categories/${id}`)
  },
  update (connId, payload) {
    const { id } = payload
    return request.put(`/connections/${connId}/categories/${id}`, payload)
  }
}
