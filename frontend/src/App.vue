<template>
  <div class="main" v-if="isErrorPage">
    <NavbarPage></NavbarPage>
    <router-view></router-view>
    <FooterPage></FooterPage>
  </div>
  <ErrorPage v-else></ErrorPage>
</template>


<script>
import NavbarPage from './components/NavbarPage.vue';
import FooterPage from './components/FooterPage.vue';
import ErrorPage from './components/ErrorPage.vue';

export default {
  components: { NavbarPage, FooterPage, ErrorPage },
  data() {
    return {
      
    }
  },
  computed:{
    isErrorPage(){
      console.log(this.$route.name)
      return this.$route.name != "error"
    }
  }
}
</script>

<style>
#app {
  text-align: center;
}
body{
  margin: 0;
}
</style>
