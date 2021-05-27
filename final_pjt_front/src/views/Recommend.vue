<template>
  <div class="recommend-box d-flex flex-column">
    
    <!-- 추천 사항 -->
    <select v-model="mode" class="btn btn-light border d-flex justify-content-start form-select mb-4" style="width:30%">
      <option value="latest">최신 영화 추천</option>
      <option value="popular">인기 영화 추천</option>
      <option value="vote">평점순 영화 추천</option>
    </select>
    
    <!-- 영화 리스트 -->
    <div class="container row row-cols-1 row-cols-md-3 g-4">
      <div class="col mt-3 mb-5" v-for="(movie, index) in movieList" :key="index">
        <div class="card h-100">
          <img :src="movie.fields.poster_path" class="card-img" style="object-fit: cover;">
          <div class="card-body">
            <h6 class="card-title fw-bold text-truncate">{{ movie.fields.title }}</h6>
            <p class="card-text">개봉일 : {{ movie.fields.release_date }}</p>
            <p class="card-text">인기도 : {{ movie.fields.popularity }}</p>
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
.recommend-box {
  position: relative;
  width : 100%;
  justify-content: center;
  align-items:center;
  overflow: hidden;
  padding: 100px;
}
.card-img{
  width:125px;
  height:600px;
}
</style>