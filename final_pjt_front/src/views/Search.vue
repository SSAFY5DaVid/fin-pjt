<template>
  <div class="container search-box">
    <h1>Search</h1>
    <div>
      <b-form @submit.prevent="onSearch">
          <b-form-input class="btn btn-secondary search-form my-3" v-model="keyword" placeholder="영화 제목을 입력하세요."></b-form-input>
      </b-form>
    </div>
    <MovieText v-if="movieList" :text="'Search Result'"></MovieText>
    <MovieLists :movieList="movieList"></MovieLists>
  </div>
</template>

<script>
import MovieLists from "../components/MovieLists"
import MovieText from "../components/MovieText"
import { movieApi } from '../utils/axios'
import { mapMutations } from "vuex"
export default {
  data(){
    return {
      keyword:"",
      movieList:""
    }
  },
  components:{
    MovieText,
    MovieLists
  },
  created(){
  this.SET_LOADING(false)
  },
  methods:{
    ...mapMutations(["SET_LOADING"]),
    async onSearch(){
      this.SET_LOADING(true)
      console.log(this.keyword)
      if(!this.keyword){
          alert("영화 제목을 입력하세요!")
          this.keyword = ""
          return
      }
      const {data} = await movieApi.search(this.keyword)
      console.log(data)
      this.movieList=data.results
      this.SET_LOADING(false)
      this.keyword = ""
    },
  }
}
</script>

<style>
.search-form {
  min-width: 5%;
}
::placeholder { 
  color: white;
  opacity: 1;
}
.search-box {
  position: relative;
  width : 100%;
  justify-content: center;
  align-items:center;
  overflow: hidden;
  padding: 100px;
}
</style>
