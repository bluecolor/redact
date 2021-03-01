/* eslint-disable camelcase */
import request from './request'

export default {
  getObjectSchemas (connectionId) {
    return request.get(`/connections/${connectionId}/metadata/object_owners`)
  },
  getTables (connectionId, owner) {
    return request.get(`/connections/${connectionId}/metadata/tables?owner=${encodeURI(owner)}`)
  },
  getColumns (connectionId, object_schema, object_name) {
    return request.get(
      `/connections/${connectionId}/metadata/columns?owner=${encodeURI(object_schema)}&table_name=${encodeURI(object_name)}`)
  }
}
