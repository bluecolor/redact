/* eslint-disable camelcase */
import request from '@/api/request'

export default {

  getAll (connId) {
    return request.get(`/connections/${connId}/redact/policies`)
  },
  update (connId, payload) {
    return request.put(`/connections/${connId}/redact/policies`, payload)
  },
  create (connId, payload) {
    return request.post(`/connections/${connId}/redact/policies`, payload)
  },
  delete (connId, payload) {
    return request.put(`/connections/${connId}/redact/policies/delete`, payload)
  }
}
