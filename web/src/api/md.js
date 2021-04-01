/* eslint-disable camelcase */
import request from './request'
import qs from 'qs'

export default {
  getObjectSchemas (connId) {
    return request.get(`/connections/${connId}/metadata/object_owners`)
  },
  getTables (connId, owner) {
    return request.get(`/connections/${connId}/metadata/tables?owner=${encodeURI(owner)}`)
  },
  getColumns (connId, object_schema, object_name) {
    return request.get(
      `/connections/${connId}/metadata/columns?owner=${encodeURI(object_schema)}&table_name=${encodeURI(object_name)}`)
  },
  search (connId, q) {
    return request.get(`/connections/${connId}/metadata/search?q=${encodeURI(q)}`)
  },
  getColumnSample (connId, params) {
    const q = qs.stringify(params)
    return request.get(`/connections/${connId}/metadata/columns/sample?${q}`)
  }
}
