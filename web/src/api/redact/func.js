/* eslint-disable camelcase */
import request from '@/api/request'

export default {

  getTypes () {
    return request.get('/redact/functions/types')
  },
  getParameters () {
    return request.get('/redact/functions/parameters')
  }
}
