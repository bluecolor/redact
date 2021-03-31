import Vue from 'vue'
import VueRouter from 'vue-router'
import MainLayout, { ConnectionLayout, SettingsLayout as AppSettingsLayout } from '@/layouts'
import Home from '@/pages/Home.vue'
import Connections, { CreateConnection, EditConnection } from '@/pages/appsettings/connections'
import Users, { CreateUser, EditUser } from '@/pages/appsettings/users'
import Notifications from '@/pages/appsettings/notifications'
import Preferences from '@/pages/appsettings/preferences'

import Explore from '@/pages/discovery/explore'
import Rules, { CreateRule, EditRule } from '@/pages/discovery/rules'
import Plans, { CreatePlan, EditPlan } from '@/pages/discovery/plans'
import PlanInstances, { AllPlanInstances } from '@/pages/discovery/plan-instances'
import Discoveries, { DiscoveryDashboard, DiscoveriesGroupByRule, DiscoveriesForRule } from '@/pages/discovery/discoveries'

import Policies, {
  CreatePolicy,
  EditPolicy,
  Columns as RedactionColumns
} from '@/pages/redaction/policies'
import Expressions, {
  ApplyExpressionToColumn as EApplyExpressionToColumn,
  CreateExpression, EditExpression
} from '@/pages/redaction/expressions'
import Categories, { EditCategory, CreateCategory } from '@/pages/redaction/categories'
import Login from '@/pages/auth'
import SettingsLayout from '@/pages/settings'
import ExportImportLayout, { Export, Import } from '@/pages/settings/export-import'

Vue.use(VueRouter)

const routes = [
  {
    path: '/auth/login',
    component: Login
  },
  {
    path: '/',
    component: MainLayout,
    children: [
      {
        name: 'home',
        path: '',
        component: Home,
        meta: { title: 'Home' }
      },
      {
        path: '/settings',
        component: AppSettingsLayout,
        children: [
          {
            name: 'profile',
            path: 'profile',
            component: EditUser,
            meta: { title: 'Profile', group: 'profile' }
          },
          {
            name: 'preferences',
            path: 'preferences',
            component: Preferences,
            meta: { title: 'Preferences', group: 'preferences' }
          },
          {
            name: 'notifications',
            path: 'notifications',
            component: Notifications,
            meta: { title: 'Notifications', group: 'notifications' }
          },
          {
            name: 'createConnection',
            path: 'connections/create',
            component: CreateConnection,
            meta: { title: 'Create Connection', group: 'connections' }
          },
          {
            name: 'editConnection',
            path: 'connections/:id',
            component: EditConnection,
            props: true,
            meta: { title: 'Edit Connection', group: 'connections' }
          }, {
            name: 'connections',
            path: 'connections',
            component: Connections,
            meta: { title: 'Connections', group: 'connections' }
          }, {
            name: 'users',
            path: 'users',
            component: Users,
            meta: { title: 'Users', group: 'users' }
          }, {
            name: 'createUser',
            path: 'users/create',
            component: CreateUser,
            meta: { title: 'Create User', group: 'users' }
          }, {
            name: 'editUser',
            path: 'users/:id',
            props: true,
            component: EditUser,
            meta: { title: 'Edit User', group: 'users' }
          }
        ]
      }, {
        name: 'connectionsLayout',
        path: '/connections/:connectionId',
        props: true,
        component: ConnectionLayout,
        redirect: '/connections/:connectionId/expressions',
        children: [{
          path: '/connections/:connectionId/settings',
          props: true,
          component: SettingsLayout,
          redirect: '/connections/:connectionId/settings/export-import',
          children: [{
            path: '/connections/:connectionId/settings/export-import',
            props: true,
            component: ExportImportLayout,
            redirect: '/connections/:connectionId/settings/export-import/export',
            children: [{
              name: 'exportSettings',
              path: '/connections/:connectionId/settings/export-import/export',
              props: true,
              component: Export,
              meta: { group: 'export-import', title: 'Export' }
            }, {
              name: 'importSettings',
              path: '/connections/:connectionId/settings/export-import/import',
              props: true,
              component: Import,
              meta: { group: 'export-import', title: 'Import' }
            }]
          }]
        }, {
          name: 'redactionColumns',
          path: '/connections/:connectionId/policies/columns',
          props: true,
          component: RedactionColumns,
          meta: { group: 'policies', title: 'Policy Columns' }
        }, {
          name: 'policies',
          path: '/connections/:connectionId/policies',
          props: true,
          component: Policies,
          meta: { group: 'policies', title: 'Policies' }
        }, {
          name: 'editPolicy',
          path: '/connections/:connectionId/policies/edit',
          props: true,
          component: EditPolicy,
          meta: { group: 'policies', title: 'Edit Policy' }
        }, {
          name: 'createPolicy',
          path: '/connections/:connectionId/policies/create',
          props: true,
          component: CreatePolicy,
          meta: { group: 'policies', title: 'Create Policy' }
        }, {
          name: 'expressions',
          path: '/connections/:connectionId/expressions',
          props: true,
          component: Expressions,
          meta: { group: 'expressions', title: 'Expressions' }
        }, {
          name: 'createExpression',
          path: '/connections/:connectionId/expressions/create',
          props: true,
          component: CreateExpression,
          meta: { group: 'expressions', title: 'Create Expression' }
        }, {
          name: 'editExpression',
          path: '/connections/:connectionId/expressions/:policy_expression_name',
          props: true,
          component: EditExpression,
          meta: { group: 'expressions', title: 'Edit Expression' }
        }, {
          name: 'eApplyExpressionToColumn',
          path: '/connections/:connectionId/expressions/:policy_expression_name/apply-to-column',
          props: true,
          component: EApplyExpressionToColumn,
          meta: { group: 'expressions', title: 'Apply Expression' }
        }, {
          name: 'categories',
          path: '/connections/:connectionId/categories',
          props: true,
          component: Categories,
          meta: { group: 'categories', title: 'Categories' }
        }, {
          name: 'createCategory',
          path: '/connections/:connectionId/categories/create',
          props: true,
          component: CreateCategory,
          meta: { group: 'categories', title: 'Create Category' }
        }, {
          name: 'editCategory',
          path: '/connections/:connectionId/categories/:id',
          props: true,
          component: EditCategory,
          meta: { group: 'categories', title: 'Edit Category' }
        }, {
          name: 'rules',
          path: '/connections/:connectionId/discovery/rules',
          component: Rules,
          props: true,
          meta: { title: 'Rules', group: 'rules' }
        }, {
          name: 'explore',
          path: '/connections/:connectionId/discovery/explore',
          component: Explore,
          props: true,
          meta: { title: 'Explore', group: 'explore' }
        }, {
          name: 'createRule',
          path: '/connections/:connectionId/discovery/rules/create',
          component: CreateRule,
          props: true,
          meta: { title: 'Create Rule', group: 'rules' }
        }, {
          name: 'editRule',
          path: '/connections/:connectionId/discovery/rules/:id',
          component: EditRule,
          props: true,
          meta: { title: 'Edit Rule', group: 'rules' }
        }, {
          name: 'plans',
          path: '/connections/:connectionId/discovery/plans',
          component: Plans,
          props: true,
          meta: { title: 'Plans', group: 'plans' }
        }, {
          name: 'createPlan',
          path: '/connections/:connectionId/discovery/plans/create',
          component: CreatePlan,
          props: true,
          meta: { title: 'Create Plan', group: 'plans' }
        }, {
          name: 'planInstances',
          path: '/connections/:connectionId/discovery/plans/:planId/instances',
          component: PlanInstances,
          props: true,
          meta: { title: 'Plan Runs', group: 'planInstances' }
        }, {
          name: 'allPlanInstances',
          path: '/connections/:connectionId/discovery/plans/instances',
          component: AllPlanInstances,
          props: true,
          meta: { title: 'All Plan Runs', group: 'planInstances' }
        }, {
          name: 'editPlan',
          path: '/connections/:connectionId/discovery/plans/:id',
          component: EditPlan,
          props: true,
          meta: { title: 'Edit Plan', group: 'plans' }
        }, {
          name: 'discoveries',
          path: '/connections/:connectionId/discovery/plans/instances/:planInstanceId/discoveries',
          component: Discoveries,
          props: true,
          meta: { title: 'Discoveries', group: 'planInstances' }
        }, {
          name: 'discoveriesGroupByRule',
          path: '/connections/:connectionId/discovery/plans/:planId/instances/:planInstanceId/discoveries-by-rule',
          component: DiscoveriesGroupByRule,
          props: true,
          meta: { title: 'Discoveries by Rule', group: 'planInstances' }
        }, {
          name: 'discoveriesForRule',
          path: '/connections/:connectionId/discovery/plans/:planId/instances/:planInstanceId/rules/:ruleId/discoveries',
          component: DiscoveriesForRule,
          props: true,
          meta: { title: 'Discoveries for Rule', group: 'planInstances' }
        }, {
          name: 'discoveriesDashboard',
          path: '/connections/:connectionId/discovery/plans/:planId/instances/:planInstanceId/dashboard',
          component: DiscoveryDashboard,
          props: true,
          meta: { title: 'Discovery Dashboard', group: 'planInstances' }
        }]
      }
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  // Vite exposes env variables on the special import.meta.env object
  base: process.env.BASE_URL,
  routes
})

// const __proto__ = Object.getPrototypeOf(router)
// const _push = __proto__.push
// __proto__.push = function push (...args) {
//   return _push.call(this, ...args)
//     .catch(error => {
//       if (error.name !== 'NavigationDuplicated') throw error
//     })
// }

export default router
