import { createRouter, createWebHistory } from 'vue-router'
import MainLayout from '@/layouts/MainLayout.vue'
import AuthLayout from '@/layouts/AuthLayout.vue'
import SettingsLayout from '@/layouts/SettingsLayout.vue'

import Home from '@/pages/Home.vue'
import Login from '@/pages/Login.vue'
import Settings, {
  DbtProfiles,
  Projects,
  CreateProject,
  Appearance
} from '@/pages/settings'
import Connections, { CreateConnection } from '@/pages/connections'

// Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: MainLayout,
    children: [
      { name: 'home', path: '', component: Home },
      {
        name: 'settings',
        path: 'settings',
        component: SettingsLayout,
        children: [{
          name: 'settings',
          path: '',
          component: Settings
        }, {
          name: 'projects',
          meta: { group: 'projects' },
          path: 'projects',
          component: Projects
        }, {
          name: 'createProject',
          meta: { group: 'projects' },
          path: 'projects/create',
          component: CreateProject
        }, {
          name: 'profiles',
          meta: { group: 'profiles' },
          path: 'profiles',
          component: DbtProfiles
        }, {
          name: 'connections',
          meta: { group: 'connections' },
          path: 'connections',
          component: Connections
        }, {
          name: 'appearance',
          meta: { group: 'appearance' },
          path: 'appearance',
          component: Appearance
        }]
      },
      { name: 'projects', path: 'projects', component: Projects },
      { name: 'connections', path: 'connections', component: Connections },
      {
        name: 'createConnection',
        path: 'connections/create',
        component: CreateConnection
      },
      {
        name: 'dbtProfile',
        path: 'settings/dbt-profile',
        component: DbtProfiles
      }
    ]
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../pages/About.vue')
  },
  {
    path: '/auth',
    name: 'Auth',
    component: AuthLayout,
    redirect: 'auth/login',
    children: [
      { name: 'login', path: 'login', component: Login }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
