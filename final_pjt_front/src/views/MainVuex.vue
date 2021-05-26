<template>
  <div>
    <div class="d-flex flex-wrap" v-if="movieList">
      <MovieListsVuex></MovieListsVuex>
    </div>
  </div>
</template>

<script>
import MovieListsVuex from "../components/MovieListsVuex"
import { movieApi } from "../utils/axios"
import { mapMutations } from "vuex"
export default {
  data() {
    return {
      movieList: {},
    }
  },
  components: {
    MovieListsVuex,
  },
  methods: {
    ...mapMutations(["SET_LOADING", "SET_NOW_PLAYING", "SET_POPULAR", "SET_UP_COMING"]),
  },
  created() {
    this.SET_LOADING(true)
  },
  async mounted() {
    try {
      // vuex를 통해서 로딩을 없애준다.
      const { data } = await movieApi.nowPlaying()
      this.SET_LOADING(false)
      console.log(data.results)
      this.SET_NOW_PLAYING(data.results)

      const { nowPlaying, popular, upComing } = movieApi
      const requestArr = [nowPlaying, popular, upComing]
      const [now, pop, up] = await Promise.all(
        requestArr.map((li) => li().then((res) => res.data))
      )
      
      console.log(now, pop, up)
    
    } catch (error) {
      this.movieList = "해당 자료가 존재하지 않습니다."
    }
  },
}
</script>

<style>
.movie-card {
  margin: 12px;
  width: 125px;
  font-size: 12px;
  font-weight: 400;
}
.movie-card:hover {
  opacity: 0.5;
  cursor: pointer;
}
.movie-card > img {
  height: 180px;
  border-radius: 8px;
}
.movie-information {
  margin-top: 7px;
}

.movie-date {
  font-size: 10px;
  margin-top: 5px;
  color: #808080;
}
</style>
