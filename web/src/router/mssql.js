import { SqlServerLayout } from '@/layouts'
import MaskedColumns, { CreateMask } from '@/pages/vendors/mssql/masks'

import {
  CreateConnection,
  EditConnection
} from '@/pages/vendors/mssql/connections'

const routes = [{
  name: 'sqlServerLayout',
  path: '/connections/:connectionId/mssql',
  props: true,
  component: SqlServerLayout,
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
