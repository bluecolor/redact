import Vue from 'vue'
import Vuex from 'vuex'

import app from './modules/app'
import md from './modules/md'
import connection from './modules/connection'

import category from './modules/oracle/redact/category'
import column from './modules/oracle/redact/column'
import expression from './modules/oracle/redact/expression'
import func from './modules/oracle/redact/func'
import policy from './modules/oracle/redact/policy'
import redaction from './modules/oracle/redact/redaction'

import discovery from './modules/discovery/discovery'
import planInstance from './modules/discovery/planInstance'
import plan from './modules/discovery/plan'
import rule from './modules/discovery/rule'
import impexp from './modules/oracle/settings/impexp'
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
