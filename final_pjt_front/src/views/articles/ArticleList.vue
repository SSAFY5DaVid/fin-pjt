<template>
  <div style="margin-top:10%">
    <div class="container d-flex justify-content-between">
      <div>
        <router-link class="btn btn-secondary ghost-button" to="/articles/article_form">글쓰기</router-link>
      </div> 
    </div>
    <div class="container text-left">
      <div class="d-flex row row mt-2 mb-4">
        <div class="col-4 article-title">제목</div>
        <div class="col-4 article-content">내용</div> 
        <div class="col-2" >작성일</div>       
      </div>
      <div v-for="review in Posts" :key="review.id">
        <div class="row d-flex mb-2" >
          <div class="col-4 article-title">{{review.title}}</div>
          <div class="col-4 article-content">{{review.content}}</div> 
          <div class="col-2">{{ getCreatedAt(review) }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import moment from 'moment'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  data : function () {
    return {
      Posts : [],
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
    onClick : function (review) {
      window.location.href=`http://localhost:8080/articles/post_detail?review_id=${review.id}`
    },
    getCreatedAt : function (review) {
      return moment(review.created_at).startOf('minute').fromNow()   
    },
    

  },
  created: function () {
    const config = this.setToken()
    axios.get(`${SERVER_URL}/articles/`,config)
    .then((res)=>{  
      this.Posts = res.data
      })
    .catch((err)=>{
      console.log(err)
    })
  }
}
</script>

<style>
.post-title {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 30%;
  min-width: 20%;
}
.post-content {
  margin-left : 5%;
  min-width: 20%;
  max-width: 20%;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.post-like {
  min-width: 8%;

}
.post-username {
  margin-left : 5%;
  min-width: 15%;
}
</style>