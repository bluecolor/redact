/* eslint-disable camelcase */
import request from '@/api/request'
import qs from 'qs'

export default {

  getAll (connId, q) {
    return request.get(`/connections/oracle/${connId}/redact/policies?${qs.stringify(q)}`)
  },
  getOwners (connId) {
    return request.get(`/connections/oracle/${connId}/redact/policies/owners`)
  },
  getTables (connId, owner) {
    return request.get(`/connections/oracle/${connId}/redact/policies/owners/${encodeURI(owner)}/tables`)
  },
  getOne (connId, q) {
    return request.get(`/connections/oracle/${connId}/redact/policies/one?${qs.stringify(q)}`)
  },
  update (connId, payload) {
    return request.put(`/connections/oracle/${connId}/redact/policies`, payload)
  },
  create (connId, payload) {
    return request.post(`/connections/oracle/${connId}/redact/policies`, payload)
  },
  delete (connId, payload) {
    return request.delete(`/connections/oracle/${connId}/redact/policies?${qs.stringify(payload)}`)
  },
  enable (connId, payload) {
    return request.put(`/connections/oracle/${connId}/redact/policies/enable`, payload)
  },
  disable (connId, payload) {
    return request.put(`/connections/oracle/${connId}/redact/policies/disable`, payload)
  },
  askTables (connId, payload) {
    return request.post(`/connections/oracle/${connId}/redact/policies/ask/tables`, payload)
  }
}
