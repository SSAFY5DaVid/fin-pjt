import Vue from "vue"
import VueRouter from "vue-router"
import Main from "@/views/Main.vue"
import MainVuex from "@/views/MainVuex.vue"
import MovieDetail from "@/views/MovieDetail.vue"
import Search from "@/views/Search.vue"
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import ArticleForm from '@/views/articles/ArticleForm'
import ArticleList from '@/views/articles/ArticleList'
import ArticleCreated from '@/views/articles/ArticleCreated'
import ArticleDetail from '@/views/articles/ArticleDetail'
import ArticleUpdate from '@/views/articles/ArticleUpdate'
import MovieReviewForm from '@/views/MovieReviewForm'
import CreateMovieReview from '@/views/CreateMovieReview.vue'
import Recommend from '@/views/Recommend.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "Main",
    component: Main,
  },
  {
    path: "/mainvuex",
    name: "MainVuex",
    component: MainVuex,
  },
  {
    path: "/detail/:id",
    name: "Detail",
    component:MovieDetail
  },
  {
    path: '/detail/create/movie_review',
    name: 'CreateMovieReview',
    component: CreateMovieReview
  },
  {
    path: '/detail/:id/movie_review_form',
    name: 'MovieReviewForm',
    component: MovieReviewForm,
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
  {
    path: '/articles/article_list',
    name: 'ArticleList',
    component: ArticleList,
  },
  {
    path: '/articles/article_created',
    name: 'ArticleCreated',
    component: ArticleCreated,
  },
  {
    path: '/articles/article_detail',
    name: 'ArticleDetail',
    component: ArticleDetail,
  },
  {
    path: '/articles/article_update',
    name: 'ArticleUpdate',
    component: ArticleUpdate,
  },
  {
    path: '/recommend',
    name: 'Recommend',
    component: Recommend,
  },    
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
})

export default router
