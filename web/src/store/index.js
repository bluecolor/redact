import Vue from 'vue'
import Vuex from 'vuex'

import app from './modules/app'
import md from './modules/md'
import connection from './modules/connection'

import category from './modules/category'
import column from './modules/vendors/oracle/redact/column'
import expression from './modules/vendors/oracle/redact/expression'
import func from './modules/vendors/oracle/redact/func'
import policy from './modules/vendors/oracle/redact/policy'
import redaction from './modules/vendors/oracle/redact/redaction'

import discovery from './modules/discovery/discovery'
import planInstance from './modules/discovery/planInstance'
import plan from './modules/discovery/plan'
import rule from './modules/discovery/rule'
import impexp from './modules/vendors/oracle/settings/impexp'
import user from './modules/user'
import appsetting from './modules/appsetting'
import notification from './modules/notification'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    connection,
    category,
    column,
    policy,
    func,
    expression,
    app,
    md,
    redaction,
    discovery,
    planInstance,
    plan,
    rule,
    impexp,
    user,
    appsetting,
    notification
  }
})
