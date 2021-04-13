import { SqlServerLayout } from '@/layouts'
import MaskedColumns, { CreateMask, EditMask, GrantUnmask, RevokeUnmask } from '@/pages/vendors/mssql/masks'

import {
  CreateConnection,
  EditConnection
} from '@/pages/vendors/mssql/connections'

import Explore from '@/pages/discovery/explore'
import Rules, { CreateRule, EditRule } from '@/pages/discovery/rules'
import Plans, { CreatePlan, EditPlan } from '@/pages/discovery/plans'
import PlanInstances, { AllPlanInstances } from '@/pages/discovery/plan-instances'
import Discoveries, { DiscoveryDashboard, DiscoveriesGroupByRule, DiscoveriesForRule } from '@/pages/discovery/discoveries'

const routes = [{
  name: 'sqlServerLayout',
  path: '/connections/:connectionId/mssql',
  props: true,
  component: SqlServerLayout,
  redirect: '/connections/:connectionId/mssql/masks/columns',
  children: [{
    name: 'maskedColumns',
    path: '/connections/:connectionId/mssql/masks/columns',
    props: true,
    component: MaskedColumns,
    meta: { group: 'masks', title: 'Masked Columns' }

  }, {
    name: 'createMask',
    path: '/connections/:connectionId/mssql/masks/columns/create',
    props: true,
    component: CreateMask,
    meta: { group: 'masks', title: 'Add Mask to Column' }
  }, {
    name: 'editMask',
    path: '/connections/:connectionId/mssql/masks/columns/edit',
    props: true,
    component: EditMask,
    meta: { group: 'masks', title: 'Edit Mask' }
  }, {
    name: 'grantUnmask',
    path: '/connections/:connectionId/mssql/masks/columns/grant',
    props: true,
    component: GrantUnmask,
    meta: { group: 'masks', title: 'Grant Unmask' }
  }, {
    name: 'revokeUnmask',
    path: '/connections/:connectionId/mssql/masks/columns/revoke',
    props: true,
    component: RevokeUnmask,
    meta: { group: 'masks', title: 'Revoke Unmask' }
  }, {
    name: 'mssqlRules',
    path: '/connections/:connectionId/mssql/discovery/rules',
    component: Rules,
    props: true,
    meta: { title: 'Rules', group: 'rules' }
  }, {
    name: 'mssqlExplore',
    path: '/connections/:connectionId/mssql/discovery/explore',
    component: Explore,
    props: route => ({
      ...route.params
    }),
    meta: { title: 'Explore', group: 'explore' }
  }, {
    name: 'mssqlCreateRule',
    path: '/connections/:connectionId/mssql/discovery/rules/create',
    component: CreateRule,
    props: true,
    meta: { title: 'Create Rule', group: 'rules' }
  }, {
    name: 'mssqlEditRule',
    path: '/connections/:connectionId/mssql/discovery/rules/:id',
    component: EditRule,
    props: true,
    meta: { title: 'Edit Rule', group: 'rules' }
  }, {
    name: 'mssqlPlans',
    path: '/connections/:connectionId/mssql/discovery/plans',
    component: Plans,
    props: true,
    meta: { title: 'Plans', group: 'plans' }
  }, {
    name: 'mssqlCreatePlan',
    path: '/connections/:connectionId/mssql/discovery/plans/create',
    component: CreatePlan,
    props: true,
    meta: { title: 'Create Plan', group: 'plans' }
  }, {
    name: 'mssqlPlanInstances',
    path: '/connections/:connectionId/mssql/discovery/plans/:planId/instances',
    component: PlanInstances,
    props: true,
    meta: { title: 'Plan Runs', group: 'planInstances' }
  }, {
    name: 'mssqlAllPlanInstances',
    path: '/connections/:connectionId/mssql/discovery/plans/instances',
    component: AllPlanInstances,
    props: true,
    meta: { title: 'All Plan Runs', group: 'planInstances' }
  }, {
    name: 'mssqlEditPlan',
    path: '/connections/:connectionId/mssql/discovery/plans/:id',
    component: EditPlan,
    props: true,
    meta: { title: 'Edit Plan', group: 'plans' }
  }, {
    name: 'mssqlDiscoveries',
    path: '/connections/:connectionId/mssql/discovery/plans/instances/:planInstanceId/discoveries',
    component: Discoveries,
    props: true,
    meta: { title: 'Discoveries', group: 'planInstances' }
  }, {
    name: 'mssqlDiscoveriesGroupByRule',
    path: '/connections/:connectionId/mssql/discovery/plans/:planId/instances/:planInstanceId/discoveries-by-rule',
    component: DiscoveriesGroupByRule,
    props: true,
    meta: { title: 'Discoveries by Rule', group: 'planInstances' }
  }, {
    name: 'mssqlDiscoveriesForRule',
    path: '/connections/:connectionId/mssql/discovery/plans/:planId/instances/:planInstanceId/rules/:ruleId/discoveries',
    component: DiscoveriesForRule,
    props: true,
    meta: { title: 'Discoveries for Rule', group: 'planInstances' }
  }, {
    name: 'mssqlDiscoveriesDashboard',
    path: '/connections/:connectionId/mssql/discovery/plans/:planId/instances/:planInstanceId/dashboard',
    component: DiscoveryDashboard,
    props: true,
    meta: { title: 'Discovery Dashboard', group: 'planInstances' }
  }]
}]

const connectionRoutes = [{
  name: 'createSqlServerConnection',
  path: 'connections/create/mssql',
  component: CreateConnection,
  meta: { title: 'Create MSSQL Connection', group: 'connections' }
},
{
  name: 'editSqlServerConnection',
  path: 'connections/:id/mssql',
  component: EditConnection,
  props: true,
  meta: { title: 'Edit MSSQL Connection', group: 'connections' }
}]

export default routes

export { connectionRoutes }
