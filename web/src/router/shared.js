import Connections, { Vendors } from '@/pages/appsettings/connections'

import { SettingsLayout as AppSettingsLayout } from '@/layouts'
import Users, { CreateUser, EditUser } from '@/pages/appsettings/users'
import Notifications from '@/pages/appsettings/notifications'
import Preferences from '@/pages/appsettings/preferences'

import { connectionRoutes as oracleConnectionRoutes } from './oracle'

const routes = [
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
        name: 'vendors',
        path: 'connections/vendors',
        component: Vendors,
        meta: { title: 'Select Database Type', group: 'connections' }
      }, {
        name: 'connections',
        path: 'connections',
        component: Connections,
        meta: { title: 'Connections', group: 'connections' }
      },
      ...oracleConnectionRoutes,
      {
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
  }
]

export default routes
