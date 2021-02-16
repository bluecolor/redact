import request from './request'

export default {

  getCategories (connectionId) {
    return request.get(`/connections/${connectionId}/categories`)
  }
}
