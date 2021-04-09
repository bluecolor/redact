import {
  CreateConnection,
  EditConnection
} from '@/pages/oracle/connections'

import { OracleLayout } from '@/layouts'

import Policies, {
  CreatePolicy,
  EditPolicy,
  Columns as RedactionColumns
} from '@/pages/oracle/redaction/policies'
import Expressions, {
  ApplyExpression,
  ApplyExpressionToColumn as EApplyExpressionToColumn,
  CreateExpression, EditExpression
} from '@/pages/oracle/redaction/expressions'

import Categories, { EditCategory, CreateCategory, AddColumnToCategory } from '@/pages/oracle/redaction/categories'
import ExportImportLayout, { Export, Import } from '@/pages/oracle/settings/export-import'

import SettingsLayout from '@/pages/oracle/settings'

import Explore from '@/pages/discovery/explore'
import Rules, { CreateRule, EditRule } from '@/pages/discovery/rules'
import Plans, { CreatePlan, EditPlan } from '@/pages/discovery/plans'
import PlanInstances, { AllPlanInstances } from '@/pages/discovery/plan-instances'
import Discoveries, { DiscoveryDashboard, DiscoveriesGroupByRule, DiscoveriesForRule } from '@/pages/discovery/discoveries'

const routes = [
  {
    name: 'oracleLayout',
    path: '/connections/oracle/:connectionId',
    props: true,
    component: OracleLayout,
    redirect: '/connections/:connectionId/policies',
    children: [{
      path: '/connections/:connectionId/settings',
      props: true,
      component: SettingsLayout,
      redirect: '/connections/oracle/:connectionId/settings/export-import',
      children: [{
        path: '/connections/oracle/:connectionId/settings/export-import',
        props: true,
        component: ExportImportLayout,
        redirect: '/connections/oracle/:connectionId/settings/export-import/export',
        children: [{
          name: 'exportSettings',
          path: '/connections/oracle/:connectionId/settings/export-import/export',
          props: true,
          component: Export,
          meta: { group: 'export-import', title: 'Export' }
        }, {
          name: 'importSettings',
          path: '/connections/oracle/:connectionId/settings/export-import/import',
          props: true,
          component: Import,
          meta: { group: 'export-import', title: 'Import' }
        }]
      }]
    }, {
      name: 'redactionColumns',
      path: '/connections/oracle/:connectionId/policies/columns',
      props: true,
      component: RedactionColumns,
      meta: { group: 'policies', title: 'Policy Columns' }
    }, {
      name: 'policies',
      path: '/connections/oracle/:connectionId/policies',
      props: true,
      component: Policies,
      meta: { group: 'policies', title: 'Policies' }
    }, {
      name: 'editPolicy',
      path: '/connections/oracle/:connectionId/policies/edit',
      props: true,
      component: EditPolicy,
      meta: { group: 'policies', title: 'Edit Policy' }
    }, {
      name: 'createPolicy',
      path: '/connections/oracle/:connectionId/policies/create',
      props: true,
      component: CreatePolicy,
      meta: { group: 'policies', title: 'Create Policy' }
    }, {
      name: 'expressions',
      path: '/connections/oracle/:connectionId/expressions',
      props: true,
      component: Expressions,
      meta: { group: 'expressions', title: 'Expressions' }
    }, {
      name: 'applyExpression',
      path: '/connections/oracle/:connectionId/expressions/apply',
      props: true,
      component: ApplyExpression,
      meta: { group: 'expressions', title: 'Apply an Expression' }
    }, {
      name: 'createExpression',
      path: '/connections/oracle/:connectionId/expressions/create',
      props: true,
      component: CreateExpression,
      meta: { group: 'expressions', title: 'Create Expression' }
    }, {
      name: 'editExpression',
      path: '/connections/oracle/:connectionId/expressions/:policy_expression_name',
      props: true,
      component: EditExpression,
      meta: { group: 'expressions', title: 'Edit Expression' }
    }, {
      name: 'eApplyExpressionToColumn',
      path: '/connections/oracle/:connectionId/expressions/:policy_expression_name/apply-to-column',
      props: true,
      component: EApplyExpressionToColumn,
      meta: { group: 'expressions', title: 'Apply Expression' }
    }, {
      name: 'categories',
      path: '/connections/oracle/:connectionId/categories',
      props: true,
      component: Categories,
      meta: { group: 'categories', title: 'Categories' }
    }, {
      name: 'createCategory',
      path: '/connections/oracle/:connectionId/categories/create',
      props: true,
      component: CreateCategory,
      meta: { group: 'categories', title: 'Create Category' }
    }, {
      name: 'editCategory',
      path: '/connections/oracle/:connectionId/categories/:id',
      props: true,
      component: EditCategory,
      meta: { group: 'categories', title: 'Edit Category' }
    }, {
      name: 'addColumnToCategory',
      path: '/connections/oracle/:connectionId/categories/:id/add-column',
      props: true,
      component: AddColumnToCategory,
      meta: { group: 'categories', title: 'Add to Category' }
    }, {
      name: 'rules',
      path: '/connections/oracle/:connectionId/discovery/rules',
      component: Rules,
      props: true,
      meta: { title: 'Rules', group: 'rules' }
    }, {
      name: 'explore',
      path: '/connections/oracle/:connectionId/discovery/explore',
      component: Explore,
      props: route => ({
        ...route.params
      }),
      meta: { title: 'Explore', group: 'explore' }
    }, {
      name: 'createRule',
      path: '/connections/oracle/:connectionId/discovery/rules/create',
      component: CreateRule,
      props: true,
      meta: { title: 'Create Rule', group: 'rules' }
    }, {
      name: 'editRule',
      path: '/connections/oracle/:connectionId/discovery/rules/:id',
      component: EditRule,
      props: true,
      meta: { title: 'Edit Rule', group: 'rules' }
    }, {
      name: 'plans',
      path: '/connections/oracle/:connectionId/discovery/plans',
      component: Plans,
      props: true,
      meta: { title: 'Plans', group: 'plans' }
    }, {
      name: 'createPlan',
      path: '/connections/oracle/:connectionId/discovery/plans/create',
      component: CreatePlan,
      props: true,
      meta: { title: 'Create Plan', group: 'plans' }
    }, {
      name: 'planInstances',
      path: '/connections/oracle/:connectionId/discovery/plans/:planId/instances',
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

const connectionRoutes = [{
  name: 'createOracleConnection',
  path: 'connections/oracle/create',
  component: CreateConnection,
  meta: { title: 'Create Oracle Connection', group: 'connections' }
},
{
  name: 'editOracleConnection',
  path: 'connections/oracle/:id',
  component: EditConnection,
  props: true,
  meta: { title: 'Edit Oracle Connection', group: 'connections' }
}]

export default routes

export { connectionRoutes }
