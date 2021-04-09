import request from '@/api/request'

export default {

  export (connId, payload) {
    return request({
      method: 'post',
      responseType: 'blob',
      url: `/connections/oracle/${connId}/settings/export`,
      data: payload
    })
  }
}
