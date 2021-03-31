/* eslint-disable camelcase */
import request from '@/api/request'
import qs from 'qs'

export default {
  getAllByPlan (connectionId, planId) {
    return request.get(`/connections/${connectionId}/discovery/plans/${planId}/instances`)
  },
  getAll (connectionId, params) {
    return request.get(`/connections/${connectionId}/discovery/plans/instances?${qs.stringify(params)}`)
  },
  getOne (connectionId, planId, id) {
    return request.get(`/connections/${connectionId}/discovery/plans/${planId}/instances/${id}`)
  },
  delete (connectionId, planId, id) {
    return request.delete(`/connections/${connectionId}/discovery/plans/${planId}/instances/${id}`)
  },
  stop (connectionId, planId, id) {
    return request.put(`/connections/${connectionId}/discovery/plans/${planId}/instances/${id}/stop`)
  }
}
