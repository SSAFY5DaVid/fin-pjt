<template>
  <div class="login-box">
    <div class="align-items-center">
      <h1>Signup</h1>
      <div>
        <input class="btn btn-secondary login-form my-3" placeholder="사용자 이름" type="text" id="username" v-model="credentials.username">
      </div>
      <div>
        <input class="btn btn-secondary login-form my-3" placeholder="비밀번호" type="password" id="password" v-model="credentials.password">
      </div>
      <div>
        <input class="btn btn-secondary login-form my-3" placeholder="비밀번호 확인" type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation">
      </div>
      <div class="d-flex justify-content-end">
      <button class=" btn btn-secondary login-form my-3" @click="signup">회원가입</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Signup',
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
        passwordConfirmation: '',
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'POST',
        url: SERVER_URL + '/accounts/signup/',
        data: this.credentials,
      }).then(res => {
        console.log(res)
        this.$router.push({ name: 'Login'})
      }).catch(err => {
        console.log(err)
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
