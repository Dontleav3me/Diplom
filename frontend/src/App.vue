<template>
  <NavbarPage></NavbarPage>
  <router-view></router-view>
  <FooterPage></FooterPage>
</template>


<script>
import NavbarPage from './components/NavbarPage.vue';
import FooterPage from './components/FooterPage.vue';

export default {
  components: { NavbarPage, FooterPage },
  data() {
    return {
      
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
body{
  margin: 0;
}
</style>
