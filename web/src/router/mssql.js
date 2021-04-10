import {
  CreateConnection,
  EditConnection
} from '@/pages/vendors/mssql/connections'

const connectionRoutes = [{
  name: 'createMSSQLConnection',
  path: 'connections/create/mssql',
  component: CreateConnection,
  meta: { title: 'Create MS-SQL Connection', group: 'connections' }
},
{
  name: 'editMSSQLConnection',
  path: 'connections/:id/mssql',
  component: EditConnection,
  props: true,
  meta: { title: 'Edit MS-SQL Connection', group: 'connections' }
}]

export { connectionRoutes }
