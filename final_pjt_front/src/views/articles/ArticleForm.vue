<template>
  <div class="container text-center" style="width:50% ;margin-top : 10%">
    <div class="text-left my-3">Title</div>
    <div><input class="text-left btn btn-secondary" type="text" style="width:100%" v-model="title"></div>
    <div class="text-left my-3">Content</div>
    <div><input class="text-left btn btn-secondary" type="text" style="width:100% ; height:100px;" v-model="content"></div>
    <button class="btn btn-secondary my-3" @click="onArticle">게시글 작성</button>
  </div>
</template>
<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ArticleForm',
  data : function () {
    return {
      content : '',
      title : '',

    }
  },
  methods : {
    onArticle : function () {
      const Article = {
        title: this.title,
        content: this.content,

      }

      axios({
          method: 'POST',
          url: SERVER_URL + '/articles/',
          headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
        data: Article
      }).then(() => {
          this.$router.push({name : "ArticleList"})
        }).catch((err) => {
          console.log(err)
        })
    // setToken : function () {
    //   const token = localStorage.getItem('jwt')
    //   const config = {
    //     headers : {
    //       Authorization : `JWT ${token}`,
    //     }
    //   }
    //   return config
    // },
    // onArticle : function () {
    //   axios.post(`${SERVER_URL}/articles/`,this.Article,this.setToken())
    //   .then((res)=>{
    //     console.log(res)
    //     this.$router.push({name : "ArticleList"})
    //   })
    //   .catch((err)=>{
    //     console.log(err)
    //   })
    // }
    }
  }   
}
</script>

<style>

</style>