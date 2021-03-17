/* eslint-disable camelcase */
import request from '@/api/request'

export default {
  getAll (connId) {
    return request.get(`/connections/${connId}/redact/expressions`)
  },
  getOne (connId, policy_expression_name) {
    return request.get(`/connections/${connId}/redact/expressions/${encodeURI(policy_expression_name)}`)
  },
  create (connId, payload) {
    return request.post(`/connections/${connId}/redact/expressions`, payload)
  },
  delete (connId, policy_expression_name) {
    return request.delete(`/connections/${connId}/redact/expressions/${encodeURI(policy_expression_name)}`)
  },
  update (connId, payload) {
    const { policy_expression_name } = payload
    return request.put(
      `/connections/${connId}/redact/expressions/${encodeURI(policy_expression_name)}`,
      payload
    )
  },
  apply (connId, payload) {
    const { policy_expression_name } = payload
    return request.put(
      `/connections/${connId}/redact/expressions/${encodeURI(policy_expression_name)}/apply-to-column`,
      payload
    )
  }
}
