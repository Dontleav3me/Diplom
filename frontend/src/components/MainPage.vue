<template>
  <div class="main">
    <p class="header">Межрегиональный Благотворительный Общественный Фонд Социальной Защиты Населения Имени Александра Невского</p>
    <button class="head_btn" @click="this.$router.push('/trends')">Направления и развития</button>
    <div class="divider"></div>
    <p class="subheader">Фонд помощи ветеранам, инвалидам правоохранительных органов и их семей, относящимся в то время практически к малоимущим слоям населения</p>
    <video src=""></video>
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
    <div class="news_container">
      <p class="news">Последние новости</p>
    </div>
    <div class="news_container">
      <MainNewsCard v-for="(mininew, index) in mininews" :key="index" :mininew="mininew"></MainNewsCard>
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
      projects: [{ name: 'Помощь Донбассу', subname: 'Начиная с 2014 года проводится благотворительная акция по сбору средств и организации гуманитарной помощи братскому народу пострадавшему в результате военных действий и беспорядков на Донбассе.'},{ name: 'Благодатный огонь', subname: 'Полное сопровождение, транспортировка и доставка Благодатного огня в РФ к празднику святой Пасхи 2024 года из Иерусалима.'},
      { name: 'Охрана здоровья', subname: 'благотворительная программа 2023-2028 «Информирование населения об основах охраны здоровья граждан в Российской Федерации»'},
      ],
      mininews: [{ name: 'В 2014- 2018 г.г. активно участвовал в масштабной программе создания Культурно-Оздоровительного Кластера в Курортном районе г. Санкт-Петербурга по правительственной программе «Оздоровительного туризма».'},{ name: 'В 2014- 2018 г.г. активно участвовал в масштабной программе создания Культурно-Оздоровительного Кластера в Курортном районе г. Санкт-Петербурга по правительственной программе «Оздоровительного туризма».'},{ name: 'В 2014- 2018 г.г. активно участвовал в масштабной программе создания Культурно-Оздоровительного Кластера в Курортном районе г. Санкт-Петербурга по правительственной программе «Оздоровительного туризма».'}],
    }
  },  
  methods: {
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
      } catch (error) {
        console.error('Error fetching uslugi:', error);
      }
    },
},
computed(){
  this.get_projects();
  this.get_mininews();
}
  
}
</script>

<style scoped> 
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
  background: #FFFFFF;
  border-radius: 3px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-bottom: 80px;
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
  text-align: left;
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


</style>
