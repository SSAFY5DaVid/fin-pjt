<template>
  <div >
    <select v-model="mode" class="form-select mb-4" style="width:30%">
      <option value="latest">최신 영화 추천</option>
      <option value="popular">인기 영화 추천</option>
      <option value="vote">평점순 영화 추천</option>
    </select>
    
    <div class="row row-cols-1 row-cols-md-3 g-4">
      <div class="col mt-3 mb-3" v-for="(movie, index) in movieList" :key="index">
        <div class="card h-100">
          <img :src="movie.fields.poster_path" class="card-img-top h-100" style="object-fit: cover;">
          <div class="card-body">
            <a :href="`http://127.0.0.1:8000/posts/${movie.pk}/`" class="text-decoration-none"><h6 class="card-title fw-bold">{{ movie.fields.title }}</h6></a>
            <p class="card-text">평점 : {{ movie.fields.vote_average }}</p>
          </div>
        </div>
      </div>
    </div>
    </div>
  </template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  data : function () {
    return {
      mode: 'latest',
      movieList: [],
    } 
  },
  methods : {
    setToken : function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers : {
          Authorization : `JWT ${token}`,
        }
      }
      return config
    },
    getMovies: function () {
      const config = this.setToken()
      const mode = this.mode
      axios.get(`${SERVER_URL}/posts/recommended?mode=${mode}`,config, {params: {mode: this.mode}})
      .then((res)=>{  
        this.movieList = res.data
        }).catch((err)=>{
        console.log(err)
        })
      },
  },
  watch: {
    mode: {
      handler: function () {
        this.getMovies()
      }
    }
  },
  created: function () {
    this.getMovies()
  }
}
</script>

<style>

</style>