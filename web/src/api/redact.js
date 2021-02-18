/* eslint-disable camelcase */
import request from './request'

export default {

  getFunctionTypes () {
    return request.get('/redact/function_types')
  },
  getFunctionParameters () {
    return request.get('/redact/function_parameters')
  },
  getPolicies (connectionId) {
    return request.get(`/connections/${connectionId}/redact/policies`)
  },
  getExpressions (connectionId) {
    return request.get(`/connections/${connectionId}/redact/expressions`)
  },
  getExpression (payload) {
    const { connectionId, policy_expression_name } = payload
    return request.get(`/connections/${connectionId}/redact/expressions/${encodeURI(policy_expression_name)}`)
  },
  createExpression (params) {
    const { connectionId, ...paylod } = params
    return request.post(`/connections/${connectionId}/redact/expressions`, paylod)
  },
  updateExpression (params) {
    const { connectionId, policy_expression_name, ...paylod } = params
    return request.put(
      `/connections/${connectionId}/redact/expressions/${encodeURI(policy_expression_name)}`,
      { policy_expression_name, ...paylod }
    )
  }
}
