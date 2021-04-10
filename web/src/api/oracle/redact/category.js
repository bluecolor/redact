import request from '@/api/request'

export default {

  getOne (connectionId, id) {
    return request.get(`/connections/oracle/${connectionId}/categories/${id}`)
  },
  getAll (connectionId) {
    return request.get(`/connections/oracle/${connectionId}/categories`)
  },
  create (connectionId, payload) {
    return request.post(`/connections/oracle/${connectionId}/categories`, payload)
  },
  delete (connId, id) {
    return request.delete(`/connections/oracle/${connId}/categories/${id}`)
  },
  update (connectionId, payload) {
    const { id } = payload
    return request.put(`/connections/oracle/${connectionId}/categories/${id}`, payload)
  }
}
