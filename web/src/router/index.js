import Vue from 'vue'
import VueRouter from 'vue-router'
import MainLayout, { ConnectionLayout, SettingsLayout } from '@/layouts'
import Home from '@/pages/Home.vue'
import Connections, { CreateConnection, EditConnection } from '@/pages/settings/connections'
import Rules, { CreateRule, EditRule } from '@/pages/discovery/rules'
import Plans, { CreatePlan, EditPlan } from '@/pages/discovery/plans'
import PlanInstances, { AllPlanInstances } from '@/pages/discovery/plan-instances'
import Discoveries, { DiscoveriesByRule, DiscoveriesForRule } from '@/pages/discovery/discoveries'

import Policies, {
  CreatePolicy,
  EditPolicy,
  AlterPolicyAddColumn,
  AlterPolicyModifyExpression,
  Columns as RedactionColumns
} from '@/pages/policies'
import Expressions, { CreateExpression, EditExpression } from '@/pages/expressions'
import Categories, { EditCategory, CreateCategory } from '@/pages/categories'
import Login from '@/pages/auth'

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
      { name: 'home', path: '', component: Home },
      {
        path: '/settings',
        component: SettingsLayout,
        children: [
          {
            name: 'createConnection',
            path: 'connections/create',
            component: CreateConnection,
            meta: { title: 'Create Connection' }
          },
          {
            name: 'editConnection',
            path: 'connections/:id',
            component: EditConnection,
            props: true,
            meta: { title: 'Edit Connection' }
          }, {
            name: 'connections',
            path: 'connections',
            component: Connections,
            meta: { title: 'Connections' }
          }
        ]
      }, {
        name: 'connectionsLayout',
        path: '/connections/:connectionId',
        props: true,
        component: ConnectionLayout,
        redirect: '/connections/:connectionId/expressions',
        children: [{
          name: 'redactionColumns',
          path: '/connections/:connectionId/policies/columns',
          props: true,
          component: RedactionColumns,
          meta: { group: 'policies', title: 'Redaction Columns' }
        }, {
          name: 'alterPolicyAddColumn',
          path: '/connections/:connectionId/policies/columns/add',
          props: true,
          component: AlterPolicyAddColumn,
          meta: { group: 'policies', title: 'Add Column' }
        }, {
          name: 'alterPolicyModifyExpression',
          path: '/connections/:connectionId/policies/columns/modify-expression',
          props: true,
          component: AlterPolicyModifyExpression,
          meta: { group: 'policies', title: 'Modify Expression' }
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
          path: 'discovery/rules',
          component: Rules,
          props: true,
          meta: { title: 'Rules', group: 'rules' }
        }, {
          name: 'createRule',
          path: '/connections/:connectionId/discovery/rules/create',
          component: CreateRule,
          props: true,
          meta: { title: 'CreateRule', group: 'rules' }
        }, {
          name: 'editRule',
          path: '/connections/:connectionId/discovery/rules/:id',
          component: EditRule,
          props: true,
          meta: { title: 'EditRule', group: 'rules' }
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
          name: 'discoveriesByRule',
          path: '/connections/:connectionId/discovery/plans/:planId/instances/:planInstanceId/discoveries-by-rule',
          component: DiscoveriesByRule,
          props: true,
          meta: { title: 'Discoveries by Rule', group: 'planInstances' }
        }, {
          name: 'discoveriesForRule',
          path: '/connections/:connectionId/discovery/plans/:planId/instances/:planInstanceId/rules/:ruleId/discoveries',
          component: DiscoveriesForRule,
          props: true,
          meta: { title: 'Discoveries for Rule', group: 'discoveries' }
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
