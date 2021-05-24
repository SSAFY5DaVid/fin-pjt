<template>
  <div class="container text-center" style="width:50% ;margin-top : 10%">
    <div class="text-left my-3">Movie Title</div>
      <div id="movie-title-container">
        <h3></h3>
        <div class="text-left btn btn-secondary" type="text" style="width:100% ;" id="movieTitle">{{ movieDetail.title }}</div>
        <!-- <input class="text-left btn btn-secondary" type="text" style="width:100%" id="movieTitle"  autocomplete="off" @keyup="showSuggestion"> -->
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
    // axios 요청 보내기
    console.log(data)
    this.movieDetail = data
    this.SET_LOADING(false)
    // backdro
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
      // const movieTitle = `${ movieDetail.title }`
      // const movieTitle = document.querySelector('#movieTitle').value
      console.log(movieTitle)
      // const isContained = this.movies.filter(function(movie) {
      //   return movie.title=== movieTitle
      // })
      // if (isContained.length===0){
      //   alert('chose right movie title')
      //   return
      // }
      // else {
      //   this.MovieReview.movie_title = movieTitle
      // }
      this.MovieReview.movie_title = this.movieDetail.title
      // this.MovieReview.movie_title = document.getElementById('movieTitle').innerHTML
      const movieReview = this.MovieReview
      const config = this.setToken()
      
      
      // axios.post(`${SERVER_URL}/detail/${movieDetail.title}/movie_review_list_create/`,movieReview, config)
      axios.post(`${SERVER_URL}/articles/movie_review_list_create/`,movieReview, config)
      .then(()=>{
        // 이게 지금 id값을 받아야함
        this.$router.push({name : "Detail", params: { id: movieDetail.id }})
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    // showSuggestion : function (event) {
    //   const suggestionsContainer = document.querySelector('#movie-title-container')
    //   if (!document.getElementById("movie-title-suggestions")){
    //     const tmp = document.createElement('div')
    //     tmp.setAttribute('id','movie-title-suggestions')
    //     suggestionsContainer.appendChild(tmp)
    //   }
    //   const suggestionsPanel = document.querySelector('#movie-title-suggestions')
    //   suggestionsPanel.innerHTML = '';
    //   suggestionsContainer.appendChild(suggestionsPanel)
    //   const movieTitle = document.querySelector('#movieTitle').value
    //   const suggestions = this.movies.filter(function(movie) {
    //     return movie.title.toLowerCase().startsWith(movieTitle)
    //   })
    //   suggestions.forEach(function(suggested) {
    //     const div = document.createElement('div')
    //     div.setAttribute("class","btn-secondary ghost-button block")
    //     div.innerHTML = suggested.title
    //     div.addEventListener("click", function (){
    //       const movieTitle = document.querySelector('#movieTitle')
    //       movieTitle.value =  suggested.title
    //       document.getElementById("movie-title-suggestions").remove()
    //     })
    //     div.setAttribute("class","btn-secondary ghost-button block change-cursor")
    //     suggestionsPanel.appendChild(div)
    //   })
    //   if (movieTitle === '') {
    //     suggestionsPanel.innerHTML = ''
    //   }
    //   if (event.key=='Enter'){
    //     console.log('enter!!!!!!!!')
    //   }
    // }
  }
}
</script>

<style>
.fill-star{
  color : rgb(248, 0, 0);
}
</style>