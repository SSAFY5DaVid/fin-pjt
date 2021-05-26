<template>
  <div id="app">
    <div id="nav" class="navbar sticky-top d-flex justify-content-between">
      <span v-if="isLogin">
        <router-link  to="/">Home</router-link> |
        <router-link to="/search">Search</router-link> |
        <router-link to="/articles/article_list">Article</router-link> |
        <router-link to="/recommend">Recommend</router-link> |
        <router-link to="#" @click.native="onLogout">Logout</router-link> 
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link> 
      </span>
    </div>
    <b-spinner
      class="d-block ml-auto mr-auto"
      v-if="loading"
      label="Spinning"
    ></b-spinner>
    <router-view @login="onLogin" :isLogin="isLogin" />
  </div>
</template>
<script>
import { mapState } from "vuex"
export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
    onLogin: function () {
      this.isLogin = true
    },
    onLogout: function () {
      localStorage.removeItem('jwt')
      localStorage.removeItem('jwt')
      localStorage.removeItem('username')
      localStorage.removeItem('user')
      this.isLogin = false
      this.$router.push({ name: 'Login'})
    }
  },
  created: function () {
    const jwt = localStorage.getItem('jwt')

    if (jwt) {
      this.isLogin = true
    }
  },
  computed: {
    ...mapState(["loading"]),
  },
};
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@700&display=swap');
* {
  color: #000000;
}
div {
  font-family: 'Nanum Gothic', sans-serif;
}
#app {
  background-color: rgb(255, 255, 255);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  color: #2c3e50;
  min-height: 100vh;
}

#nav {
  text-align: center;
  padding: 20px;
  z-index: 99;
  background-color: rgb(241, 241, 241);
}

#nav a {
  font-weight: bold;
  color: #95a0ac;
}

#nav a.router-link-exact-active {
  color: #7e3371;
}

</style>
