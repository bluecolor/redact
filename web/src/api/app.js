/* eslint-disable camelcase */
import request from './request'

export default {
  getVersion () {
    return request.get('/application/version')
  }
}
