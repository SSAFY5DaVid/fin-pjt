<template>
  <div class="container text-center" style="width:50% ;margin-top : 10%">
    <div class="text-left my-3">Movie Title</div>
      <div id="movie-title-container">
        <h3></h3>
        <div class="text-left btn btn-secondary" type="text" style="width:100% ;" id="movieTitle">{{ movieDetail.title }}</div>
      </div>
    <div class="text-left my-3">Review Title</div>
      <div><input class="text-left btn btn-secondary" type="text" style="width:100%" v-model="MovieReview.title"></div>

    <div class="text-left my-3">Content</div>
      <div><input class="text-left btn btn-secondary" type="text" style="width:100% ; height:100px;" v-model="MovieReview.content"></div>
    <div class="text-left my-3">Rank</div>
      <div style=" color:#545454;font-size : 1.5rem" id="star-rank">
        <span class="change-cursor mx-1" @click="starClick(1)" @mouseover="fillStar(1)" @mouseout="clearStar" id="star-1">★</span>
        <span class="change-cursor mx-1" @click="starClick(2)" @mouseover="fillStar(2)" @mouseout="clearStar" id="star-2">★</span>
        <span class="change-cursor mx-1" @click="starClick(3)" @mouseover="fillStar(3)" @mouseout="clearStar" id="star-3">★</span>
        <span class="change-cursor mx-1" @click="starClick(4)" @mouseover="fillStar(4)" @mouseout="clearStar" id="star-4">★</span>
        <span class="change-cursor mx-1" @click="starClick(5)" @mouseover="fillStar(5)" @mouseout="clearStar" id="star-5">★</span>
      </div>
    <button class="btn btn-secondary my-3" @click="createReview">submit your review</button>
  </div>
</template>

<script>
import axios from 'axios'
import movies from '@/movies.json'
import { movieApi } from "../utils/axios"
import { mapMutations } from "vuex"

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  data : function () {
    return {
      MovieReview : {
        rank : 0,
        content : '',
        movie_title : '',
        title : '',
        username : localStorage.getItem('username'),
        movie_id : 0,
      },
      starStatus : false,
      movies : movies,
      movieDetail: {},
    }
  },
  async mounted() {
    this.SET_LOADING(true)
    console.log(this.$route)
    console.log(this.$route.params.id)
    const { id } = this.$route.params
    const { data } = await movieApi.movieDetail(id)
    console.log(data)
    this.movieDetail = data
    this.SET_LOADING(false)
  },
  methods : {
    ...mapMutations(["SET_LOADING"]),
    setToken : function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers : {
          Authorization : `JWT ${token}`,
        }
      }
      return config
    },
    fillStar : function (count) {
      if (this.starStatus){
        return
      }
      for (let i=1;i<count+1;i++){
        const star = document.querySelector(`#star-${i}`)
        star.classList.add("fill-star")
      }
    },
    clearStar : function () {
      if (this.starStatus){
        return
      }
      for (let i=1;i<6;i++){
        const star = document.querySelector(`#star-${i}`)
        star.setAttribute("class","change-cursor mx-1")
      }
    },
    starClick : function (count) {
      this.starStatus = !this.starStatus
      if (this.starStatus) {
        this.MovieReview.rank = count 
      }
      else {
        this.MovieReview.rank = 0
      }
    },
    createReview : function () {
      if (this.MovieReview.rank === 0) {
        alert('chose rank')
        return
      }

      this.MovieReview.movie_title = this.movieDetail.title
      this.MovieReview.movie_id = this.movieDetail.id
      const movieReview = this.MovieReview
      const config = this.setToken()
      
      // 이것은 서버와 URL을 연동시켜야함 (SERVER_URL)
      axios.post(`${SERVER_URL}/articles/movie_review_list_create/`,movieReview, config)
      .then(()=>{
        // 저장한 값을 보냄 호출 : $route.params.review
        this.$router.push({name : "Detail", params: { review: movieReview }})
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  }
}
</script>

<style>
.fill-star{
  color : rgb(248, 0, 0);
}
</style>