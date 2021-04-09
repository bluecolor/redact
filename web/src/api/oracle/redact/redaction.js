/* eslint-disable camelcase */
import request from '@/api/request'
import qs from 'qs'

export default {
  askColumns (connId, payload) {
    return request.post(`/connections/${connId}/redact/ask/columns`, payload)
  },
  askInfo (connId, params) {
    return request.get(`/connections/${connId}/redact/ask/info?${qs.stringify(params)}`)
  },
  askPolicy (connId, params) {
    return request.get(`/connections/${connId}/redact/ask/policy?${qs.stringify(params)}`)
  },
  askExpression (connId, params) {
    return request.get(`/connections/${connId}/redact/ask/expression?${qs.stringify(params)}`)
  }
}
