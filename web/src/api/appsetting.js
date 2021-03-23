import request from '@/api/request'

export default {

  get (name) {
    return request.get(`/settings/${encodeURI(name)}`)
  },
  getAll () {
    return request.get('/settings')
  },
  set (payload) {
    const { name } = payload
    return request.put(`/settings/${name}`, payload)
  },
  setAll (payload) {
    return request.post('/settings', payload)
  }
}
