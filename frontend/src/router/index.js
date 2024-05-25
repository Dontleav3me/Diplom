import { createRouter, createWebHistory } from 'vue-router'
import AboutPage from '../components/AboutPage.vue'
import MainPage from '../components/MainPage.vue'
import TrendsPage from '../components/TrendsPage.vue'
import PartnerPage from '../components/PartnerPage.vue'
import NewsPage from '../components/NewsPage.vue'
import ContactPage from '../components/ContactPage.vue'
import ErrorPage from '../components/ErrorPage.vue'

const routes = [
  {
    path: '/about',
    name: 'about',
    component: AboutPage
  },
  {
    path: '/',
    name: 'main',
    component: MainPage
  },
  {
    path: '/trends',
    name: 'trends',
    component: TrendsPage
  },
  {
    path: '/news',
    name: 'news',
    component: NewsPage
  },
  {
    path: '/partner',
    name: 'partner',
    component: PartnerPage
  },
  {
    path: '/contact',
    name: 'contact',
    component: ContactPage
  },
  {
    path: '/error',
    name: 'error',
    component: ErrorPage
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
