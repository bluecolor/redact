/* eslint-disable camelcase */
import request from '@/api/request'
import qs from 'qs'

export default {
  getMaskedColumns (connId, params) {
    return request.get(`/connections/${connId}/mssql/masks/columns?${qs.stringify(params)}`)
  },
  getMaskingFunctions () {
    return request.get('/mssql/masks/functions')
  },
  addMask (connId, payload) {
    return request.post(`/connections/${connId}/mssql/masks/columns`, payload)
  },
  dropMask (connId, params) {
    return request.delete(`/connections/${connId}/mssql/masks/columns?${qs.stringify(params)}`)
  },
  grantUnmask (connId, payload) {
    return request.post(`/connections/${connId}/mssql/masks/columns/grant-unmask`, payload)
  },
  revokeUnmask (connId, payload) {
    return request.post(`/connections/${connId}/mssql/masks/columns/revoke-unmask`, payload)
  }
}
