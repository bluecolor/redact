/* eslint-disable camelcase */
import request from './request'

export default {
  getRules (connectionId) {
    return request.get(`/connections/${connectionId}/discovery/rules`)
  },
  createRule (connectionId, payload) {
    return request.post(`/connections/${connectionId}/discovery/rules`, payload)
  },
  getPlans (connectionId) {
    return request.get(`/connections/${connectionId}/discovery/plans`)
  },
  createPlan (connectionId, payload) {
    return request.post(`/connections/${connectionId}/discovery/plans`, payload)
  }
}
