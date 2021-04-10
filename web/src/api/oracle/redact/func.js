/* eslint-disable camelcase */
import request from '@/api/request'

export default {
  getTypes () {
    return request.get('/oracle/redact/functions/types')
  },
  getParameters () {
    return request.get('/oracle/redact/functions/parameters')
  },
  getActions () {
    return request.get('/oracle/redact/functions/actions')
  }
}
