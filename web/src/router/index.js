import Vue from 'vue'
import VueRouter from 'vue-router'
import MainLayout, { ConnectionLayout } from '@/layouts'
import Home from '@/pages/Home.vue'
import Connections, { CreateConnection, EditConnection } from '@/pages/settings/connections'
import Policies, { CreatePolicy, EditPolicy, AddColumn as AddRedactionColumn, Columns as RedactionColumns } from '@/pages/policies'
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
        name: 'createConnection',
        path: 'settings/connections/create',
        component: CreateConnection
      },
      {
        name: 'editConnection',
        path: 'settings/connections/:id/edit',
        component: EditConnection,
        props: true
      }, {
        name: 'connections',
        path: 'settings/connections',
        component: Connections
      }, {
        name: 'connectionsLayout',
        path: '/connections/:connectionId',
        props: true,
        component: ConnectionLayout,
        children: [{
          name: 'redactionColumns',
          path: '/connections/:connectionId/policies/columns',
          props: true,
          component: RedactionColumns,
          meta: { group: 'policies' }
        }, {
          name: 'addRedactionColumn',
          path: '/connections/:connectionId/policies/columns/add',
          props: true,
          component: AddRedactionColumn,
          meta: { group: 'policies' }
        }, {
          name: 'policies',
          path: '/connections/:connectionId/policies',
          props: true,
          component: Policies,
          meta: { group: 'policies' }
        }, {
          name: 'editPolicy',
          path: '/connections/:connectionId/policies/edit',
          props: true,
          component: EditPolicy,
          meta: { group: 'policies' }
        }, {
          name: 'createPolicy',
          path: '/connections/:connectionId/policies/create',
          props: true,
          component: CreatePolicy,
          meta: { group: 'policies' }
        }, {
          name: 'expressions',
          path: '/connections/:connectionId/expressions',
          props: true,
          component: Expressions,
          meta: { group: 'expressions' }
        }, {
          name: 'createExpression',
          path: '/connections/:connectionId/expressions/create',
          props: true,
          component: CreateExpression,
          meta: { group: 'expressions' }
        }, {
          name: 'editExpression',
          path: '/connections/:connectionId/expressions/:policy_expression_name',
          props: true,
          component: EditExpression,
          meta: { group: 'expressions' }
        }, {
          name: 'categories',
          path: '/connections/:connectionId/categories',
          props: true,
          component: Categories,
          meta: { group: 'categories' }
        }, {
          name: 'createCategory',
          path: '/connections/:connectionId/categories/create',
          props: true,
          component: CreateCategory,
          meta: { group: 'categories' }
        }, {
          name: 'editCategory',
          path: '/connections/:connectionId/categories/:id',
          props: true,
          component: EditCategory,
          meta: { group: 'categories' }
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

export default router
