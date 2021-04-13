import Vue from 'vue'
import VueRouter from 'vue-router'
import MainLayout from '@/layouts'
import Home from '@/pages/Home.vue'
import Notifications from '@/pages/Notifications.vue'

import Login from '@/pages/auth'

import oracleRoutes from './oracle'
import mssqlRoutes from './mssql'
import sharedRoutes from './shared'

Vue.use(VueRouter)

const routes = [
  {
    path: '/auth/login',
    component: Login
  },
  {
    path: '/',
    component: MainLayout,
    props: true,
    children: [
      {
        name: 'home',
        path: '',
        props: true,
        component: Home,
        meta: { title: 'Home' }
      },
      {
        name: 'allNotifications',
        path: '/notifications',
        props: true,
        component: Notifications,
        meta: { title: 'Notifications' }
      },
      ...sharedRoutes,
      ...oracleRoutes,
      ...mssqlRoutes
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
