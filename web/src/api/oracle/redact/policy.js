/* eslint-disable camelcase */
import request from '@/api/request'
import qs from 'qs'

export default {

  getAll (connId, q) {
    return request.get(`/connections/${connId}/redact/policies?${qs.stringify(q)}`)
  },
  getOwners (connId) {
    return request.get(`/connections/${connId}/redact/policies/owners`)
  },
  getTables (connId, owner) {
    return request.get(`/connections/${connId}/redact/policies/owners/${encodeURI(owner)}/tables`)
  },
  getOne (connId, q) {
    return request.get(`/connections/${connId}/redact/policies/one?${qs.stringify(q)}`)
  },
  update (connId, payload) {
    return request.put(`/connections/${connId}/redact/policies`, payload)
  },
  create (connId, payload) {
    return request.post(`/connections/${connId}/redact/policies`, payload)
  },
  delete (connId, payload) {
    return request.delete(`/connections/${connId}/redact/policies?${qs.stringify(payload)}`)
  },
  enable (connId, payload) {
    return request.put(`/connections/${connId}/redact/policies/enable`, payload)
  },
  disable (connId, payload) {
    return request.put(`/connections/${connId}/redact/policies/disable`, payload)
  },
  askTables (connId, payload) {
    return request.post(`/connections/${connId}/redact/policies/ask/tables`, payload)
  }
}
