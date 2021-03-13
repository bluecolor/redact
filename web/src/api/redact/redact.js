/* eslint-disable camelcase */
import request from '@/api/request'
import qs from 'qs'

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
  alterPolicy (params) {
    const { connId, ...payload } = params
    return request.put(`/connections/${connId}/redact/policies`, payload)
  },
  getExpressions (connectionId) {
    return request.get(`/connections/${connectionId}/redact/expressions`)
  },
  getExpression (payload) {
    const { connectionId, policy_expression_name } = payload
    return request.get(`/connections/${connectionId}/redact/expressions/${encodeURI(policy_expression_name)}`)
  },
  createExpression ({ connectionId, ...paylod }) {
    return request.post(`/connections/${connectionId}/redact/expressions`, paylod)
  },
  dropExpression ({ connId, policy_expression_name }) {
    return request.delete(`/connections/${connId}/redact/expressions?${qs.stringify({ name: policy_expression_name })}`)
  },
  updateExpression (params) {
    const { connectionId, policy_expression_name, ...paylod } = params
    return request.put(
      `/connections/${connectionId}/redact/expressions/${encodeURI(policy_expression_name)}`,
      { policy_expression_name, ...paylod }
    )
  },
  createPolicy (params) {
    const { connId, ...paylod } = params
    return request.post(`/connections/${connId}/redact/policies`, paylod)
  },
  getColumns (params) {
    const { connId, ...query } = params
    return request.get(`/connections/${connId}/redact/columns?${qs.stringify(query)}`)
  }
}
