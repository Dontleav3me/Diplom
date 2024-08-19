<template>
  <div class="z-index">

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
      <div class="nav_container_img">
        <img src="../../static/img/logo.svg" alt="" draggable="false"
        @click="resetMenuItem">
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
    <div class="nav_mobile">
      <div class="nav_container_mobile">
        <router-link to="/">
          <img src="../../static/img/logo.svg" alt="" draggable="false" @click="resetMenuItems">
        </router-link>
        <div class="hamburger" @click="toggleMenu">
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>
      <div class="nav_menu" :class="{ open: isMenuOpen }">
        <div class="img_ham">
          <router-link to="/">
            <img class="logo_center" src="../../static/img/logo.svg" alt="" draggable="false" @click="resetMenuItems">
          </router-link>
          <div class="close_btn" @click="toggleMenu">&times;</div>
        </div>
        <a href="/">Главная</a>
        <a href="/about">О нас</a>
        <a href="/trends">Направления развития</a>
        <a href="/news">Новости и события</a>
        <a href="/partner">Партнерство</a>
<!--         <a href="#">Новости</a>
        <a href="#">Вакансии</a>
        <a href="#">Награды</a> -->
        <a href="/contact">Контакты</a>
        <div class="socials">
          <p>Социальные сети</p>
          <a href="#">Телеграм</a>
          <a href="#">Вконтакте</a>
          <a href="#">Tenchat</a>
          <a href="#">Почта</a>
          <a href="#">Youtube</a>
        </div>
        <div class="mailing">
          <div class="mailing_container">
            <p class="mailing_text">Подписаться на рассылку</p>
            <img src="../../static/img/mailing.svg" alt="">
          </div>
          <div class="divider"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedMenuItem: null,
      isMenuOpen: false
    };
  },
  methods: {
    selectMenuItem(item) {
      this.selectedMenuItem = item;
    },
    resetMenuItem() {
      this.selectedMenuItem = null;
      this.$router.push('/');
    },
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
      if (this.isMenuOpen) {
        document.documentElement.style.overflow = 'hidden';
        document.body.style.overflow = 'hidden';
      } else {
        document.documentElement.style.overflow = '';
        document.body.style.overflow = '';
      }
    },
    resetMenuItems() {
      this.isMenuOpen = false;
      document.documentElement.style.overflow = '';
      document.body.style.overflow = '';
    },
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
.nav_container_img {
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
  font-family: Inter Regular;
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
p {
  margin: 0;
}
.nav_mobile{
  display: none;
}
.z-index{
  position: relative;
  z-index: 99;
}

@media (max-width: 797px) {
  .nav {
    display: none;
  }
  
  .nav_mobile {
    display: block;
  }
  
  .nav_mobile {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 10px;
    background-color: #f8f8f8;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }
  
  .nav_container_mobile {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    max-width: 1200px;
  }
  
  .nav_container img {
    margin: 0 auto;
  }
  
  .hamburger {
    position: absolute;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    width: 30px;
    height: 30px;
    cursor: pointer;
    right: 0;
  }
  
  .hamburger span {
    display: block;
    height: 4px;
    background-color: #333;
    border-radius: 2px;
    transition: transform 0.3s, opacity 0.3s;
  }
  
  .nav_menu {
    position: absolute;
    top: 0;
    left: 0;
    width: 50%;
    height: 100vh;
    background-color: #d9d9d9f8;
    box-shadow: 2px 0 5px rgba(0, 0, 0, 0.5);
    transform: translateX(-100%);
    transition: transform 0.3s ease;
    padding: 10px;
    display: flex;
    flex-direction: column;
    align-items: flex-start; /* Align items to the left */
    overflow-y: hidden; /* Prevent scrolling within the menu */
  }
  
  .nav_menu.open {
    transform: translateX(0);
    overflow-y: auto; /* Allow scrolling within the menu when open */
  }
  
  .nav_menu a {
    font-family: Inter Medium;
    font-size: 16px;
    line-height: 16.94px;
    letter-spacing: -0.01em;
    margin-bottom: 20px;
    text-decoration: none;
    color: #000;
  }
  
  .img_ham {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    margin-bottom: 20px;
  }
  
  .logo_center {
    margin: 0 auto;
  }
  
  .close_btn {
    font-size: 30px;
    cursor: pointer;
    color: #000;
    margin-right: 10px;
    position: absolute;
    top: 10px;
    right: 10px;
    transition: all 0.2s ease;
  }
  .close_btn:hover{
    color: #0D42A8;
  }
  
  html.no-scroll,
  body.no-scroll {
    overflow: hidden;
    height: 100%;
  }
  .socials {
    display: flex;
    flex-direction: column;
    margin-top: auto; 
    padding-top: 20px;
  }
  
  .socials p {
    font-family: Inter Medium;
    font-size: 18px;
    line-height: 24px;
    color: #000;
    margin-bottom: 15px;
  }

  
  .socials a {
    font-family: Inter Medium;
    font-size: 16px;
    line-height: 22px;
    letter-spacing: -0.01em;
    margin-bottom: 10px;
    text-decoration: none;
    color: #000;
    text-align: left
  }
  .mailing{
    display: flex;
    flex-direction: column;
    gap: 15px;
    margin-top: 30px;
  }
  .mailing_container{
    display: flex;
    gap: 5px;
  }
  .mailing_text{
    color: #0D42A8;
    font-size: 14px;
    text-align: left;
    font-family: Inter Medium;
    cursor: pointer;
  }
  .divider {
    border-bottom: 1px solid rgba(13, 66, 168, 1); 
    width: auto;
    margin-bottom: 50px;
  }
  a{
    transition: all 0.2s ease;
  }
  a:hover{
    color: #0D42A8;
  }
}
</style>
