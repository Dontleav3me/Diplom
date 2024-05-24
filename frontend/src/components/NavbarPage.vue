<template>
  <div class="nav">
    <router-link to="/about" style="text-decoration: none;">
      <div 
        class="nav_container" 
        :class="{ selected: selectedMenuItem === 'О нас' }"
        @click="selectMenuItem('О нас')"
      >
        <p class="nav_text">О нас</p>
      </div>
    </router-link>
    <router-link to="/trends" style="text-decoration: none;">
      <div 
        class="nav_container" 
        :class="{ selected: selectedMenuItem === 'Направления развития' }"
        @click="selectMenuItem('Направления развития')"
      >
        <p class="nav_text">Направления развития</p>
      </div>
    </router-link>
    <div class="nav_container">
      <img src="../../static/img/logo.svg" alt="" draggable="false"
      @click="this.$router.push('/')">
    </div>
    <router-link to="/news" style="text-decoration: none;">
      <div 
        class="nav_container" 
        :class="{ selected: selectedMenuItem === 'Новости и события' }"
        @click="selectMenuItem('Новости и события')"
      >
        <p class="nav_text">Новости и события</p>
      </div>
    </router-link>
    <router-link to="/partner" style="text-decoration: none;">
      <div 
        class="nav_container" 
        :class="{ selected: selectedMenuItem === 'Партнерство' }"
        @click="selectMenuItem('Партнерство')"
      >
        <p class="nav_text">Партнерство</p>
      </div>
    </router-link>
    <router-link to="/contact" style="text-decoration: none;">
      <div 
        class="nav_container" 
        :class="{ selected: selectedMenuItem === 'Контакты' }"
        @click="selectMenuItem('Контакты')"
      >
        <p class="nav_text">Контакты</p>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedMenuItem: null
    };
  },
  methods: {
    selectMenuItem(item) {
      this.selectedMenuItem = item;
    }
  }
}
</script>

<style scoped>
.nav_container {
  cursor: pointer;
  user-select: none;
  position: relative;
  transition: all 0.3s ease;
}
.nav {
  display: flex;
  gap: 45px;
  justify-content: center;
  align-items: center;
  margin: 10px 105px 40px 105px;
}
.nav_text {
  color: #191819;
  font-size: 20px;
  font-family: Inter;
  text-align: left;
}
.nav_container::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 0;
  right: 0;
  height: 2px;
  background-color: #0D42A8;
  opacity: 0;
  transition: opacity 0.3s ease;
}
.nav_container.selected::after,
.nav_container:hover::after {
  opacity: 1;
}
p{
  margin: 0;
}
</style>
