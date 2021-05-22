<template>
<div class="login-box">
  <div class="align-items-center">
    <h1>Login</h1>
    <div>
      <input  class="btn btn-secondary login-form my-3" placeholder="username" type="text" v-model="credentials.username">
    </div>
    <div>
      <input  class="btn btn-secondary login-form my-3" placeholder="password" type="password" v-model="credentials.password" @keypress.enter="login">
    </div>
    <div class="d-flex justify-content-end">
      <button class="btn btn-secondary login-form my-3" @click="login">login</button>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  props: {
    isLogin: {
      type: Boolean,
      required: true,
    }
  },
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'POST',
        url: SERVER_URL + '/accounts/api-token-auth/',
        data: this.credentials,
      }).then(res => {
        localStorage.setItem('jwt', res.data.token)
        this.$emit('login')
        this.$router.push({ name: 'Home'})
      }).catch(err => {
        console.log(err)
      })
    }
  },
  created: function () {
    if (this.isLogin) {
      this.$router.push({ name: 'Home'})
    }
  },
}
</script>

<style>
.login-form {
  min-width: 5%;
}
::placeholder { 
  color: white;
  opacity: 1;
}

.login-box {
  position: relative;
  width : 100%;
  min-height: 90vh;
  display: flex;
  justify-content: center;
  align-items:center;
  overflow: hidden;
  padding: 100px;
}

</style>