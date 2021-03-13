/* eslint-disable camelcase */
import request from '@/api/request'

export default {
  getAll (connectionId) {
    return request.get(`/connections/${connectionId}/redact/expressions`)
  },
  getOne (connectionId, policy_expression_name) {
    return request.get(`/connections/${connectionId}/redact/expressions/${encodeURI(policy_expression_name)}`)
  },
  create (connectionId, payload) {
    return request.post(`/connections/${connectionId}/redact/expressions`, payload)
  },
  delete (connId, policy_expression_name) {
    return request.delete(`/connections/${connId}/redact/expressions/${encodeURI(policy_expression_name)}`)
  },
  update (connectionId, policy_expression_name, payload) {
    return request.put(
      `/connections/${connectionId}/redact/expressions/${encodeURI(policy_expression_name)}`,
      { policy_expression_name, ...payload }
    )
  }
}
