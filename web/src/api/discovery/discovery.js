/* eslint-disable camelcase */
import request from '@/api/request'
import qs from 'qs'

export default {
  getRule (connectionId, id) {
    return request.get(`/connections/${connectionId}/discovery/rules/${id}`)
  },
  getRules (connectionId) {
    return request.get(`/connections/${connectionId}/discovery/rules`)
  },
  createRule (connectionId, payload) {
    return request.post(`/connections/${connectionId}/discovery/rules`, payload)
  },
  deleteRule (connectionId, id) {
    return request.delete(`/connections/${connectionId}/discovery/rules/${id}`)
  },
  getPlanInstances (connectionId, planId) {
    return request.get(`/connections/${connectionId}/discovery/plans/${planId}/instances`)
  },
  getAllPlanInstances (connectionId) {
    return request.get(`/connections/${connectionId}/discovery/plans/instances`)
  },
  getPlanInstance (connectionId, id) {
    return request.get(`/connections/${connectionId}/discovery/plans/instances/${id}`)
  },
  getDiscoveries (connectionId, planInstanceId, query) {
    return request.get(`/connections/${connectionId}/discovery/plans/instances/${planInstanceId}/discoveries?${qs.stringify(query)}`)
  },
  getDiscoveriesForRule (connectionId, planId, planInstanceId, ruleId, query) {
    return request.get(`/connections/${connectionId}/discovery/plans/${planId}/instances/${planInstanceId}/rules/${ruleId}?${qs.stringify(query)}`)
  }
}
