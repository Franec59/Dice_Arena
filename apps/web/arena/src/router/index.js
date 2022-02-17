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
    path: '/neutre/:id',
    name: 'Neutre',
    component: () => import(/* webpackChunkName: "Neutre" */ '../views/Neutre.vue'),
    props: true
  },
  {
    path: '/donjon/:id',
    name: 'Donjon',
    component: () => import(/* webpackChunkName: "Donjon" */ '../views/Donjon.vue'),
    props: true
  },
  {
    name: 'Warhammer',
    path: '/warhammer/:id',
    component: () => import(/* webpackChunkName: "Warhammer" */ '../views/Warhammer.vue'),
    props: true

  },
  {
    name: 'Yam',
    path: '/yam/:id',
    component: () => import(/* webpackChunkName: "Warhammer" */ '../views/Yam.vue'),
    props: true

  },
  {
    // path: '/:catchAll(.*)',
    path: '/:pathMatch(.*)*',
    name: 'Notfound',
    component: () => import(/* webpackChunkName: "Notfound" */ '../views/Notfound.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
