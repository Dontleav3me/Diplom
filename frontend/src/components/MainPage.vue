<template>
  <div class="bg">
    <div class="main">
      <p class="header">Межрегиональный Благотворительный Общественный Фонд Социальной Защиты Населения Имени Александра Невского</p>
      <button class="head_btn" @click="this.$router.push('/trends')">Направления и развития</button>
      <div class="divider"></div>
      <p class="subheader">Фонд помощи ветеранам, инвалидам правоохранительных органов и их семей, относящимся в то время практически к малоимущим слоям населения</p>
      <div class="slider">
        <button class="slider-btn prev-btn" @click="prevSlide">&#9664;</button>
        <div class="slider-wrapper" :style="{ transform: `translateX(${-currentIndex * 100}%)` }">
          <div class="slider-image" v-for="(image, index) in images" :key="index">
            <img :src="image" :alt="'Slide ' + (index + 1)" />
          </div>
        </div>
        <button class="slider-btn next-btn" @click="nextSlide">&#9654;</button>
      </div>
      <div class="proekt_container">
        <div class="proekt_content">
          <p class="proekt_text">
            Каждый день, мы развиваем разные проекты от поддержки малоимущих семей, до духовного просвещения граждан и восстановлению инфраструктуры на новых территориях 
          </p>
          <img src="../../static/img/mailing.svg" alt="">
        </div>
        <div class="divider_proekt"></div>
      </div>
      <div class="project_container">
        <p class="project">Наши действующие проекты</p>
      </div>
      <div class="project_content">
        <MainCard v-for="(project, index) in projects" :key="index" :project="project"></MainCard>
      </div>
      <div class="news_container" style="display: none;">
        <p class="news">Последние новости</p>
      </div>
      <div class="news_container" style="display: none;">
        <MainNewsCard v-for="(mininew, index) in mininews" :key="index" :mininew="mininew"></MainNewsCard>
      </div>
    </div>
  </div>
</template>

<script>
import MainCard from '../components/MainCard.vue'
import MainNewsCard from '../components/MainNewsCard.vue'
import axios from 'axios'
export default {
  components: { MainCard, MainNewsCard},
  data() {
    return {
      projects: [],
      mininews: [],
      images: [
        require('@/assets/crunch1.jpg'),
        require('@/assets/kazanski2.jpg'),
        require('@/assets/4.jpg'),
      ],
      currentIndex: 0,
    }
  },  
  methods: {
    prevSlide() {
      this.currentIndex =
        this.currentIndex > 0 ? this.currentIndex - 1 : this.images.length - 1;
    },
    nextSlide() {
      this.currentIndex =
        this.currentIndex < this.images.length - 1 ? this.currentIndex + 1 : 0;
    },
    startAutoSlide() {
      this.autoSlideInterval = setInterval(() => {
        this.nextSlide();
      }, 5000);
    },
    stopAutoSlide() {
      clearInterval(this.autoSlideInterval);
    },
    async get_projects(){
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/projects/`);
        this.projects = response.data;
      } catch (error) {
        console.error('Error fetching uslugi:', error);
      }
    },
    async get_mininews(){
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/mini_news/`);
        this.mininews = response.data;
        console.log(this.mininews)
      } catch (error) {
        console.error('Error fetching uslugi:', error);
      }
    },
},
beforeUnmount() {
    this.stopAutoSlide();
  },
async mounted(){
  await this.get_projects();
  await this.get_mininews();
  this.startAutoSlide();
}
  
}
</script>

<style scoped> 
.slider {
  position: relative;
  width: 80%;
  height: 550px;
  overflow: hidden;
  margin: 20px auto;
  border: 2px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.slider-wrapper {
  display: flex;
  transition: transform 0.5s ease-in-out;
}

.slider-image {
  min-width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.slider-image img {
  width: 100%;
  height: 550px;
  object-fit: cover;
}

.slider-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background-color: rgba(0, 0, 0, 0.5);
  color: #fff;
  border: none;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;
}

.prev-btn {
  left: 10px;
}

.next-btn {
  right: 10px;
}

.slider-btn:hover {
  background-color: rgba(0, 0, 0, 0.7);
}
.bg{
  position: relative;
  z-index: 1;
  background: 
    url(../../static/img/head_stripe_blue.png) no-repeat,
    url(../../static/img/head_stripe_red.png) no-repeat;
  object-fit: cover;
  background-repeat: no-repeat;
  background-size: 100% 450px, 100% 500px;
  background-position: top left, top left;
}
.main {
  margin: 30px 125px 20px 125px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.header {
  font-size: 48px;
  color: #191819;
  font-family: Athelas;
  margin-bottom: 120px;
  max-width: 1150px;
}
p {
  margin: 0;
}
.head_btn {
  width: 520px;
  border: 1px solid #0D42A8;
  padding: 10px 0px 10px 2px;
  color: #0D42A8;
  font-family: Inter SemiBold;
  font-size: 16px;
  line-height: 19.36px;
  text-align: left;
  border-radius: 3px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-bottom: 80px;
  background: none;
}
.head_btn:hover {
  color: #FFFFFF;
  background: #0D42A8;
}
.divider {
  border-bottom: 1px solid rgba(13, 66, 168, 1); 
  width: 100%;
  margin-bottom: 20px;
}
.divider_proekt {
  border-bottom: 1px solid rgba(13, 66, 168, 1); 
  width: 453px;
  margin-top: 10px;
  margin-bottom: 35px;
}
.subheader {
  font-family: Inter Regular;
  font-size: 16px;
  line-height: 19.36px;
  letter-spacing: -0.01em;
  text-align: center;
  margin-bottom: 45px;
  color: #191819;
}
video {
  width: 50%;
  margin-bottom: 40px;
}
.proekt_container {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}
.proekt_content {
  display: flex;
  gap: 20px;
  align-items: flex-start;
}
.proekt_text {
  font-family: Inter Regular;
  font-size: 16px;
  line-height: 19.36px;
  letter-spacing: -0.01em;
  text-align: justify;
  max-width: 420px;
  color: #191819;
}
.project_container {
  width: 100%;
  display: flex;
  justify-content: flex-start;
}
.project {
  font-family: Athelas;
  font-size: 40px;
  font-weight: 400;
  line-height: 44.8px;
  letter-spacing: -0.01em;
  text-align: left;
  color: #191819; 
  margin-bottom: 60px;
}
.project_content {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: 1fr;
  gap: 20px;
  margin-bottom: 30px;
  align-self: flex-start;
}
.news_container {
  width: 100%;
  display: flex;
  justify-content: flex-start;
}
.news {
  font-family: Athelas;
  font-size: 40px;
  line-height: 44.8px;
  letter-spacing: -0.01em;
  text-align: left;
  color: #191819;
  margin-bottom: 65px;
}
.news_container{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: 1fr;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  gap: 20px;
}

@media (max-width: 797px) {
  .header{
    max-width: 500px;
    font-family: Athelas;
    font-size: 20px;
    line-height: 22.4px;
    letter-spacing: -0.02em;
    text-align: center;
    margin-bottom: 30px;
  }
  .head_btn{
    width: 65%;
  }
  .subheader{
    font-family: Inter Regular;
    font-size: 14px;
    line-height: 18.1px;
    letter-spacing: -0.01em;
    text-align: center;
  }
  .main{
    margin: 30px 15px 20px 15px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .project_content {
    display: grid;
    grid-template-columns: repeat(1, 1fr);
    grid-template-rows: 1fr;
    gap: 20px;
    margin-bottom: 30px;
    align-self: flex-start;
  }
  .news_container{
    display: grid;
    grid-template-columns: repeat(1, 1fr);
    grid-template-rows: 1fr;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    gap: 20px;
  }
  .project{
    font-family: Athelas;
    font-size: 24px;
    line-height: 17.92px;
    letter-spacing: -0.01em;
    text-align: justify;
    margin-bottom: 30px;
  }
  .proekt_text{
    font-family: Inter Regular;
    font-size: 12px;
    line-height: 12.1px;
    letter-spacing: -0.01em;
    text-align: justify;
  }
  .proekt_content{
    max-width: 300px;
  }
  .divider_proekt{
    max-width: 300px;
  }
  .news{
    font-family: Athelas;
    font-size: 24px;
    line-height: 17.92px;
    letter-spacing: -0.01em;
    text-align: justify;
    margin-bottom: 30px;
  }
  .bg{
    position: relative;
    z-index: 1;
    object-fit: cover;
    background-position: top left, top left, top left;
    background: 
    url(../../static/img/mobile_level_1.png) no-repeat,
    url(../../static/img/mobile_level_2.png) no-repeat,
    url(../../static/img/mobile_level_3.png) no-repeat;
    background-size: 100% 450px, 100% 450px, 100% 500px;
    background-repeat: no-repeat;
  }
  .slider {
    width: 90%;
    height: auto;
  }

  .slider-image img {
    height: 250px;
  }

  .slider-btn {
    width: 30px;
    height: 30px;
    font-size: 14px;
  }

  .prev-btn {
    left: 5px;
  }

  .next-btn {
    right: 5px;
  }
}
</style>
