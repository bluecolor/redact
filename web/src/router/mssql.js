import { SqlServerLayout } from '@/layouts'
import MaskedColumns, { CreateMask, EditMask, GrantUnmask, RevokeUnmask } from '@/pages/vendors/mssql/masks'

import {
  CreateConnection,
  EditConnection
} from '@/pages/vendors/mssql/connections'

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
