<template>
   <div>
    <ArticleForm />
    <router-view/>
  </div>
</template>

<script>
import ArticleForm from './ArticleForm.vue'

export default {
  components: {
    ArticleForm    
  },
}
</script>

<style>

</style>