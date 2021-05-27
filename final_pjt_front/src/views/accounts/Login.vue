<template>
<div class="login-box">
  <div class="align-items-center">
    <h1>Login</h1>
    <div>
      <input  class="btn btn-secondary login-form my-3" placeholder="사용자 이름" type="text" v-model="credentials.username">
    </div>
    <div>
      <input  class="btn btn-secondary login-form my-3" placeholder="비밀번호" type="password" v-model="credentials.password" @keypress.enter="login">
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
    setToken : function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers : {
          Authorization : `JWT ${token}`,
        }
      }
      return config
    },
    login: function () {
      axios.post(`${SERVER_URL}/accounts/api-token-auth/`, this.credentials)
      .then((res) => {
        localStorage.setItem('jwt',res.data.token)
        const config = this.setToken()
        axios.get(`${SERVER_URL}/accounts/username/`,config)
        .then((res)=>{
          localStorage.setItem('username',res.data.username)
          localStorage.setItem('user_id',res.data.user_id) 
          this.$emit('login')
          this.$router.push({ name: 'Main'})
        })
      })
    }
  },
  created: function () {
    if (this.isLogin) {
      this.$router.push({ name: 'Main'})
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
  opacity: 0.4;
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