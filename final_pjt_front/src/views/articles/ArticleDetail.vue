<template>
  <div class="container text-left" style="margin-top:10%">
    <div style="min-height:70vh;">
      <div class="edit-btn mb-4 d-flex justify-content-end">
        <span v-if="me==review.username">
          <button class="btn btn-secondary ghost-button ml-2" @click="goUpdate(review)">수정하기</button>
          <button  class="btn btn-secondary ghost-button ml-2" @click="onDelete(review.id)">삭제하기</button>
        </span>
        <span >
          <button class="btn btn-secondary ghost-button ml-2" @click="goBack(review)">뒤로가기</button>
        </span>
      </div>
      <div class="article-overview rounded container mb-4 bg-light">
        <h1> 제목 : {{review.title}} </h1>
        <hr>
        <h2> 내용 </h2>
        <h3> {{review.content}} </h3>
      </div>
      <!-- <div class="m-3"><PostLike :review_id="review_id"/></div> -->
      <div class="row d-flex mb-2">
        <div class="col-1 article-title">-></div>
        <div class="col-10 article-review rounded mb-4 bg-secondary">
          <ArticleComment :review_id="review_id"/>
        </div>
      </div>
      
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
.btn {
  padding: 10px 10px;
}
.article-overview {
  padding: 10px 0px;
  opacity: 0.95;
}
.article-review {
  padding: 0px 0px;
  opacity: 0.75;
}
</style>