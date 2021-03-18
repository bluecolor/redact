/* eslint-disable camelcase */
import request from '@/api/request'

export default {
  getAll (connId) {
    return request.get(`/connections/${connId}/discovery/plans`)
  },
  getOne (connId, id) {
    return request.get(`/connections/${connId}/discovery/plans/${id}`)
  },
  create (connId, payload) {
    return request.post(`/connections/${connId}/discovery/plans`, payload)
  },
  update (connId, id, payload) {
    return request.put(`/connections/${connId}/discovery/plans/${id}`, payload)
  },
  delete (connId, id) {
    return request.delete(`/connections/${connId}/discovery/plans/${id}`)
  },
  run (connId, id) {
    return request.put(`/connections/${connId}/discovery/plans/${id}/run`)
  },
  getLastInstance (connId, id) {
    return request.get(`/connections/${connId}/discovery/plans/${id}/last-instance`)
  }
}
