/* eslint-disable camelcase */
import request from '@/api/request'

export default {
  askColumns (connId, payload) {
    return request.post(`/connections/${connId}/redact/ask/columns`, payload)
  }
}
