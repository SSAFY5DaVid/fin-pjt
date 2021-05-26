<template>
  <div class="d-flex justify-content-center">
    <input  class="btn btn-secondary comment-form" type="text" v-model="comment.content" @keypress.enter="createComment">
    <button  class="btn btn-secondary ghost-button mx-4" @click="createComment">COMMENT</button>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  data : function () {
    return {
      comment : {
        content : '',
        username : localStorage.getItem('username'),
      }
    }
  },
  props : {
    review_id : [String,Number],
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
    createComment : function () {
      const config = this.setToken()
      axios.post(`${SERVER_URL}/articles/${this.review_id}/comments/`,this.comment,config)
      .then((res)=>{
        console.log(res)
        this.$router.go(this.$router.currentRoute)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
  },

}
</script>

<style>
.comment-form {
  min-width: 5%;
}
</style>