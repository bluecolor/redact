import Vue from 'vue'
import Vuex from 'vuex'

import app from './modules/app'
import md from './modules/md'
import connection from './modules/connection'

import category from './modules/redact/category'
import column from './modules/redact/column'
import expression from './modules/redact/expression'
import func from './modules/redact/func'
import policy from './modules/redact/policy'
import redaction from './modules/redact/redaction'

import discovery from './modules/discovery/discovery'
import planInstance from './modules/discovery/planInstance'
import plan from './modules/discovery/plan'
import rule from './modules/discovery/rule'
import impexp from './modules/settings/impexp'
import user from './modules/user'
import auth from './modules/auth'
import appsetting from './modules/appsetting'

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
    auth,
    appsetting
  }
})
