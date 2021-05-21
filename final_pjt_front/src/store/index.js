import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    loading: true,
    nowPlaying:[],
    popular:[],
    upComing:[]
  },
  mutations: {
    SET_LOADING(state, data){
      state.loading = data;
    },
    SET_NOW_PLAYING(state, data){
      state.nowPlaying = data;
    },
    SET_POPULAR(state, data){
      state.popular = data;
    },
    SET_UP_COMING(state, data){
      state.upComing = data;
    }
    
  },
  actions: {
  },
  modules: {
  }
})
