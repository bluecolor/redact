/* eslint-disable camelcase */
import request from '@/api/request'

export default {
  getOne (connectionId, id) {
    return request.get(`/connections/${connectionId}/discovery/rules/${id}`)
  },
  getAll (connectionId) {
    return request.get(`/connections/${connectionId}/discovery/rules`)
  },
  create (connectionId, payload) {
    return request.post(`/connections/${connectionId}/discovery/rules`, payload)
  },
  update (connectionId, id, payload) {
    return request.put(`/connections/${connectionId}/discovery/rules/${id}`, payload)
  },
  delete (connectionId, id) {
    return request.delete(`/connections/${connectionId}/discovery/rules/${id}`)
  }
}
