import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/pseudo',
    name: 'Pseudo',
    component: () => import(/* webpackChunkName: "Pseudo" */ '../views/Pseudo.vue')
  },
  {
    path: '/createPartie',
    name: 'CreatePartie',
    component: () => import(/* webpackChunkName: "CreatePartie" */ '../views/CreatePartie.vue')
  },
  {
    path: '/joinPartie',
    name: 'JoinPartie',
    component: () => import(/* webpackChunkName: "JoinPartie" */ '../views/JoinPartie.vue')
  },
  {
    path: '/neutre',
    name: 'Neutre',
    component: () => import(/* webpackChunkName: "Neutre" */ '../views/Neutre.vue')
  },
  {
    path: '/donjon',
    name: 'Donjon',
    component: () => import(/* webpackChunkName: "Donjon" */ '../views/Donjon.vue')
  },
  {
    path: '/warhammer',
    name: 'Warhammer',
    component: () => import(/* webpackChunkName: "Warhammer" */ '../views/Warhammer.vue')
  },
  {
    path: '/:catchAll(.*)', 
    name: 'Notfound',
    component: () => import(/* webpackChunkName: "Notfound" */ '../views/Notfound.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
