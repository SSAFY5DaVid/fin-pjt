<template>
  <div class="container text-left" style="margin-top:10%">
    <div style="min-height:70vh;">
      <span v-if="me==review.username">
        <button class="btn btn-secondary ghost-button" @click="goUpdate(review)">수정하기</button>
        <button  class="btn btn-secondary ghost-button" @click="onDelete(review.id)">삭제하기</button>
      </span>
      <span >
        <button class="btn btn-secondary ghost-button" @click="goBack(review)">뒤로가기</button>
      </span>
      <h1> 제목 : {{review.title}} </h1>
      <br>
      <h2> 내용 : {{review.content}} </h2>

      <!-- <div class="m-3"><PostLike :review_id="review_id"/></div> -->
      <ArticleComment :review_id="review_id"/>
      <ArticleCommentForm :review_id="review_id"/>
    </div>

    <div><ArticleList /></div>
  </div>
</template>

<script>
import axios from 'axios'
import ArticleList from './ArticleList.vue'
import ArticleComment from './ArticleComment.vue'
import ArticleCommentForm from './ArticleCommentForm.vue'


const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  data : function () {
    return {
      review_id : this.$route.query.review_id,
      update_delete : false,
      review : '',
      me : localStorage.getItem('username')
    }
  },
  components : {
    ArticleList,
    ArticleComment,  
    ArticleCommentForm,

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
    goBack : function () {
      this.$router.push({name : 'ArticleList'})
    },
    goUpdate : function (review) {
      this.$router.push({name : 'ArticleUpdate', params : {review :review}})
    },
    onDelete : function (id) {
      const config = this.setToken()
      axios.delete(`${SERVER_URL}/articles/${id}/`,config)
      .then(()=>{
        this.$router.push({name : 'ArticleList'})
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  },
  created: function () {
    const config = this.setToken()
    axios.get(`${SERVER_URL}/articles/${this.review_id}/`,config)
    .then((res)=>{
      this.review = {
        title  : res.data.title,
        content : res.data.content,
        id : res.data.id,
        username : res.data.username,
      }
      this.username = res.data.username
      if(res.data.is_review_user){
        this.update_delete = true
      }
    })
  }
}
</script>

<style>

</style>