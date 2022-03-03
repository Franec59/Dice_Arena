import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/pseudo',
    name: 'Pseudo',
    component: () => import(/* webpackChunkName: "Pseudo" */ '../views/Pseudo.vue')
  },
  {
    path: '/choix',
    name: 'Choix',
    component: () => import(/* webpackChunkName: "Pseudo" */ '../views/Choix.vue')
  },
  {
    path: '/creerPartie',
    name: 'Creer_partie',
    component: () => import(/* webpackChunkName: "Pseudo" */ '../views/Creer_partie.vue')
  },
  {
    path: '/commencer',
    name: 'Commencer',
    component: () => import(/* webpackChunkName: "Commencer" */ '../views/Commencer.vue')
  },
  {
    path: '/joinPartie',
    name: 'JoinPartie',
    component: () => import(/* webpackChunkName: "JoinPartie" */ '../views/JoinPartie.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "About" */ '../views/About.vue')
  },
  {
    path: '/lancer',
    name: 'Lancer',
    component: () => import(/* webpackChunkName: "Lancer" */ '../views/Lancer.vue')
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
    props: true,
    // beforeEnter: (to, from, next) => {
    //   // Access store here
    //   next()
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
    name: 'Craps',
    path: '/craps/:id',
    component: () => import(/* webpackChunkName: "Warhammer" */ '../views/Craps.vue'),
    props: true

  },
  {
    name: 'Wargame',
    path: '/Wargame/:id',
    component: () => import(/* webpackChunkName: "Warhammer" */ '../views/Wargame.vue'),
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
