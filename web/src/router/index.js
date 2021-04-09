import Vue from 'vue'
import VueRouter from 'vue-router'
import MainLayout from '@/layouts'
import Home from '@/pages/Home.vue'

import Login from '@/pages/auth'

import oracleRoutes from './oracle'
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
    children: [
      {
        name: 'home',
        path: '',
        component: Home,
        meta: { title: 'Home' }
      },
      ...sharedRoutes,
      ...oracleRoutes
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
