/* eslint-disable camelcase */
import request from './request'

export default {
  getAll (connectionId) {
    return request.get(`/connections/${connectionId}/discovery/plans`)
  },
  getOne (connectionId, id) {
    return request.get(`/connections/${connectionId}/discovery/plans/${id}`)
  },
  create (connectionId, payload) {
    return request.post(`/connections/${connectionId}/discovery/plans`, payload)
  },
  update (connectionId, id, payload) {
    return request.put(`/connections/${connectionId}/discovery/plans/${id}`, payload)
  },
  delete (connectionId, id) {
    return request.delete(`/connections/${connectionId}/discovery/plans/${id}`)
  },
  run (connectionId, id) {
    return request.get(`/connections/${connectionId}/discovery/plans/${id}/run`)
  }
}
