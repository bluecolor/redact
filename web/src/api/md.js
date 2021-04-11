/* eslint-disable camelcase */
import request from './request'
import qs from 'qs'

export default {
  getSchemas (connId) {
    return request.get(`/connections/${connId}/metadata/schemas`)
  },
  getTables (connId, schema_name) {
    return request.get(`/connections/${connId}/metadata/tables?schema_name=${encodeURI(schema_name)}`)
  },
  getColumns (connId, schema_name, table_name) {
    return request.get(
      `/connections/${connId}/metadata/columns?${qs.stringify({ schema_name, table_name })}`)
  },
  search (connId, q) {
    return request.get(`/connections/${connId}/metadata/search?q=${encodeURI(q)}`)
  },
  getColumnSample (connId, params) {
    const q = qs.stringify(params)
    return request.get(`/connections/${connId}/metadata/columns/sample?${q}`)
  }
}
