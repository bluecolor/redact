/* eslint-disable camelcase */
import request from './request'
import qs from 'qs'

export default {
  getRules (connectionId) {
    return request.get(`/connections/${connectionId}/discovery/rules`)
  },
  createRule (connectionId, payload) {
    return request.post(`/connections/${connectionId}/discovery/rules`, payload)
  },
  deleteRule (connectionId, id) {
    return request.delete(`/connections/${connectionId}/discovery/rules/${id}`)
  },
  getPlans (connectionId) {
    return request.get(`/connections/${connectionId}/discovery/plans`)
  },
  createPlan (connectionId, payload) {
    return request.post(`/connections/${connectionId}/discovery/plans`, payload)
  },
  deletePlan (connectionId, id) {
    return request.delete(`/connections/${connectionId}/discovery/plans/${id}`)
  },
  runPlan (connectionId, id) {
    return request.get(`/connections/${connectionId}/discovery/plans/${id}/run`)
  },
  getPlanInstances (connectionId) {
    return request.get(`/connections/${connectionId}/discovery/plans/instances`)
  },
  getDiscoveries (connectionId, planInstanceId, query) {
    return request.get(`/connections/${connectionId}/discovery/plans/instances/${planInstanceId}/discoveries?${qs.stringify(query)}`)
  }
}
