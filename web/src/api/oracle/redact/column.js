/* eslint-disable camelcase */
import request from '@/api/request'
import qs from 'qs'

export default {
  getAll (connId, q) {
    return request.get(`/connections/${connId}/redact/columns?${qs.stringify(q)}`)
  }
}
