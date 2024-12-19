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
@font-face {
  font-family: 'Athelas';
  src:url('../static/fonts/Athelas/Athelas-Regular.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'Inter SemiBold';
  src:url('../static/fonts/Inter/Inter-SemiBold.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'Inter Regular';
  src:url('../static/fonts/Inter/Inter-Regular.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'Inter Medium';
  src:url('../static/fonts/Inter/Inter-Medium.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}
#app {
  text-align: center;
}
body{
  margin: 0;
  overflow: visible !important;
}
</style>
