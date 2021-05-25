<template>
  <div class="container text-center" style="width:50% ;margin-top : 10%">
    <div class="text-left my-3">Title</div>
    <div><input class="text-left btn btn-secondary" type="text" style="width:100%" v-model="Article.title"></div>
    <div class="text-left my-3">Content</div>
    <div><input class="text-left btn btn-secondary" type="text" style="width:100% ; height:100px;" v-model="Article.content"></div>
    <button class="btn btn-secondary my-3" @click="onArticle">게시글 작성</button>
  </div>
</template>
<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  data : function () {
    return {
      Article : {
        content : this.$route.params.review.content,
        title : this.$route.params.review.title,
        username : this.$route.params.review.username,
      }
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
    onArticle : function () {
      const config = this.setToken()
      axios.put(`${SERVER_URL}/articles/${this.$route.params.review.id}/`,this.Article,config)
      .then((res)=>{
        console.log(res)
        this.$router.push({name : "ArticleList"})
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>