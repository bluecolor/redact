/* eslint-disable camelcase */
import request from '@/api/request'
import qs from 'qs'

export default {
  getAllGroupByRule (c, p, pi) {
    return request.get(
      `/connections/${c}/discovery/plans/${p}/instances/${pi}/discoveries/group-by-rule`
    )
  },
  getAll (c, p, pi, q) {
    return request.get(
      `/connections/${c}/discovery/plans/${p}/instances/${pi}/discoveries?${qs.stringify(q)}`
    )
  }
}
