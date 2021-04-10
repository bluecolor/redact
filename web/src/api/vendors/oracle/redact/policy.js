/* eslint-disable camelcase */
import request from '@/api/request'
import qs from 'qs'

export default {

  getAll (connId, q) {
    return request.get(`/connections/${connId}/oracle/redact/policies?${qs.stringify(q)}`)
  },
  getOwners (connId) {
    return request.get(`/connections/${connId}/oracle/redact/policies/owners`)
  },
  getTables (connId, owner) {
    return request.get(`/connections/${connId}/oracle/redact/policies/owners/${encodeURI(owner)}/tables`)
  },
  getOne (connId, q) {
    return request.get(`/connections/${connId}/oracle/redact/policies/one?${qs.stringify(q)}`)
  },
  update (connId, payload) {
    return request.put(`/connections/${connId}/oracle/redact/policies`, payload)
  },
  create (connId, payload) {
    return request.post(`/connections/${connId}/oracle/redact/policies`, payload)
  },
  delete (connId, payload) {
    return request.delete(`/connections/${connId}/oracle/redact/policies?${qs.stringify(payload)}`)
  },
  enable (connId, payload) {
    return request.put(`/connections/${connId}/oracle/redact/policies/enable`, payload)
  },
  disable (connId, payload) {
    return request.put(`/connections/${connId}/oracle/redact/policies/disable`, payload)
  },
  askTables (connId, payload) {
    return request.post(`/connections/${connId}/oracle/redact/policies/ask/tables`, payload)
  }
}
