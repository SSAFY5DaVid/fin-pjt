<template>
  <div class="container" style="margin-top:10%">
    <div class="post-btn d-flex justify-content-between">
      <router-link class="btn btn-secondary ghost-button" to="/articles/article_form">글쓰기</router-link>
    </div>
    <div class="article-list rounded container text-left bg-light">
      <div class="d-flex row row mt-2 mb-4">
        <div class="col-2 article-title">제목</div>
        <div class="col-4 article-content">내용</div> 
        <div class="col-2 post-username">작성자</div>
        <div class="col-2" >작성일</div>       
      </div>
      <div v-for="review in Posts" :key="review.id">
        <div class="row d-flex mb-2" @click="onClick(review)">
          <div class="col-2 article-title text-truncate">{{ review.title }}</div>
          <div class="col-4 article-content">{{ review.content }}</div> 
          <div class="col-2 post-username">{{ review.username }} </div>
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
      window.location.href=`http://localhost:8080/articles/article_detail?review_id=${review.id}`
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
      }).catch((err)=>{
      console.log(err)
    })
  }
}
</script>

<style>
.article-list {
  padding: 10px 0px;
  opacity: 0.95;
}
.post-btn {
  padding: 10px 0px;
}
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