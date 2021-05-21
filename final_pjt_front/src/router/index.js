import Vue from "vue"
import VueRouter from "vue-router"
import Main from "@/views/Main.vue"
import MainVuex from "@/views/MainVuex.vue"
import MovieDetail from "@/views/MovieDetail.vue"
import Search from "@/views/Search.vue"
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import ArticleForm from '@/views/articles/ArticleForm'

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "Home",
    component: Main,
  },
  {
    path: "/mainvuex",
    name: "Main",
    component: MainVuex,
  },
  {
    path: "/detail/:id",
    name: "Detail",
    component:MovieDetail
  },
  {
    path:"/search",
    name:"Search",
    component:Search
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/articles/article_form',
    name: 'ArticleForm',
    component: ArticleForm,
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
})

export default router
