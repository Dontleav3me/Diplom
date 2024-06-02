<template>
  <div class="main">
    <div class="header">
      <div class="header_container">
        <div class="header_text">
          <p class="main_text">{{ name }}</p>
          <p class="main_subtext">{{ subname }}</p>
          <div class="descr">
            <p class="main_descr">{{ dela }}</p>
            <div class="divider_height"></div>
            <p class="main_descr">{{ geo }}</p>
            <div class="divider_height"></div>
            <p class="main_descr">{{ date }}</p>
          </div>
        </div>
        <img :src="img" alt="">
      </div>
      <div class="wrapper">
        <NewsTopCard v-for="(NewsTop, index) in NewsTops" :key="index" :NewsTop="NewsTop"></NewsTopCard>
      </div>
    </div>
    <div class="divider"></div>
    <p class="events_head">Важные события</p>
<!--     <video src="../../static/img/krest.mp4" controls width="20%" height="500px"></video> -->
    <div class="events_container">
      <p class="events_top">{{ head }}</p>
      <div class="events_bottom">
        <div class="events_left">
          <div class="event_bold">
            <p class="bold">В</p>
            <p class="events_text">ечный огонь был передан Церкви и далее его понесли по храмам и церквям Питера</p>
          </div>
          <p class="events_text">Вечный огонь был передан Церкви и далее его понесли по храмам и церквям Санкт-Петербурга. Всем понравилось, все граждане видели.</p>
          <p class="events_text">Вечный огонь был передан Церкви и далее его понесли по храмам и церквям Санкт-Петербурга. Всем понравилось, все граждане видели.</p>
        </div>
        <div class="events_right">
          <p class="events_text">Вечный огонь был передан Церкви и далее его понесли по храмам и церквям Санкт-Петербурга. Всем понравилось, все граждане видели.</p>
          <p class="events_text">Вечный огонь был передан Церкви и далее его понесли по храмам и церквям Санкт-Петербурга. Всем понравилось, все граждане видели.</p>
          <p class="events_text">Вечный огонь был передан Церкви и далее его понесли по храмам и церквям Санкт-Петербурга. Всем понравилось, все граждане видели.</p>
        </div>
      </div>
      <div class="more">
        <div class="more_head">
          <p class="more_text">Благие дела</p>
          <div class="divider_card"></div>
          <p class="more_text">10 мин чтения</p>
        </div>
        <button class="more_btn">
          Подробнее
        </button>
      </div>
    </div>
    <p class="news_head">Новости и события</p>
    <div class="news_wrapper">
      <NewsBottomCard v-for="(NewsBottom, index) in NewsBottoms" :key="index" :NewsBottom="NewsBottom"></NewsBottomCard>
    </div>
    <button class="over_btn">Больше новостей</button>
  </div>
</template>

<script>
import NewsTopCard from '../components/NewsTopCard.vue'
import NewsBottomCard from '../components/NewsBottomCard.vue'
import axios from 'axios'
export default {
  components: { NewsTopCard, NewsBottomCard},
  data() {
    return {
      NewsTops: [],
      NewsBottoms: [],
      name: '',
      subname: '',
      dela: '',
      geo: '',
      date: '',
      img: '',
    }
  },
  methods: {
    async get_solonews(){
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/solo_news/`);
        this.name = response.data[0].name;
        this.subname = response.data[0].subname;
        this.dela = response.data[0].dela;
        this.geo = response.data[0].geo;
        this.img = 'http://127.0.0.1:8000'+response.data[0].image;
        this.head = response.data[0].head;
        this.date = response.data[0].date
      } catch (error) {
        console.error('Error fetching uslugi:', error);
      }
    },
    async get_newsbottom(){
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/bottom_news/`);
        this.NewsBottoms = response.data;
      } catch (error) {
        console.error('Error fetching uslugi:', error);
      }
    },
    async get_topnews(){
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/news_top/`);
        this.NewsTops = response.data;
      } catch (error) {
        console.error('Error fetching uslugi:', error);
      }
    },
},
mounted(){
  this.get_topnews();
  this.get_newsbottom();
  this.get_solonews();
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
.main_text{
  font-family: Athelas;
  font-size: 52px;
  font-weight: 400;
  line-height: 80px;
  text-align: left;
  color: #000000;
  max-width: 450px;
}
.main_subtext{
  font-family: Inter;
  font-size: 14px;
  font-weight: 400;
  line-height: 22px;
  text-align: left;
  color: #3D3D3D;
  max-width: 420px;
}
.header_text{
  display: flex;
  flex-direction: column;
  gap: 25px;
}
.header_container{
  display: flex;
  gap: 40px;
  align-items: flex-start;
}
img{
  border-radius: 5px;
}
.descr{
  margin-top: 160px;
  display: flex;
  gap: 16px;
}
.divider_height{
  border: 1px solid #000000A3;
}
.divider_card{
  border: 1px solid #000000A3;
}
.more_head{
  display: flex;
  gap: 16px;
}
.more_text{
  font-family: Inter Regular;
  font-size: 12px;
  font-weight: 400;
  line-height: 16px;
  text-align: left;
  color: #000000B8;
}
.more{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 30px;
  margin-bottom: 55px;
}
.header{
  display: flex;
  gap: 15px;
}
.card_main_text{
  font-family: Inter;
  font-size: 20px;
  font-weight: 400;
  line-height: 26px;
  text-align: left;
  color: #000000;
}

p{
  margin: 0;
}
.wrapper{
  display: flex;
  flex-direction: column;
  gap: 40px;
}
.divider {
  border-bottom: 1px solid rgba(13, 66, 168, 1); 
  width: 100%;
  margin: 80px 0 55px 0;
}
.events_head{
  font-family: Athelas;
  font-size: 32px;
  font-weight: 400;
  line-height: 40px;
  text-align: left;
  color: #000000;
  margin-bottom: 40px;
  display: flex;
  align-self: flex-start;
}
.events_top{
  font-family: Athelas;
  font-size: 48px;
  font-weight: 400;
  line-height: 64px;
  text-align: left;
  color: #000000;
  max-width: 500px;
  margin-bottom: 30px;
}
.bold{
  font-family: Athelas;
  font-size: 88px;
  font-weight: 400;
  line-height: 68px;
  color: #000000;
}
.events_text{
  font-family: Inter Medium;
  font-size: 14px;
  font-weight: 400;
  line-height: 22px;
  text-align: left;
  color: #3D3D3D;
}
.event_bold{
  display: flex;
  align-items: flex-start;
  gap: 12px;
}
.events_left{
  display: flex;
  flex-direction: column;
  gap: 20px;
  max-width: 243px;
}
.events_bottom{
  display: flex;
  gap: 20px;
}
.events_right{
  display: flex;
  flex-direction: column;
  gap: 20px;
  max-width: 243px;
}
.more_btn {  
  width: auto;
  border: 1px solid #0D42A8;
  padding: 5px 30px;
  color: #0D42A8;
  font-family: Inter SemiBold;
  font-size: 14px;
  line-height: 19.36px;
  text-align: center;
  background: #FFFFFF;
  border-radius: 3px;
  cursor: pointer;
  transition: all 0.3s ease;  
}
.more_btn:hover {
  color: #FFFFFF;
  background: #0D42A8;
}
.news_head{
  font-family: Athelas;
  font-size: 32px;
  font-weight: 400;
  line-height: 40px;
  text-align: left;
  color: #000000;
  margin-bottom: 40px;
  display: flex;
  align-self: flex-start;
}
.news_wrapper{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: 1fr;
  gap: 100px;
  margin-bottom: 65px;
}
.over_btn {  
  width: auto;
  border: 1px solid #0D42A8;
  padding: 5px 30px;
  color: #0D42A8;
  font-family: Inter SemiBold;
  font-size: 14px;
  line-height: 29.05px;
  text-align: center;
  background: #FFFFFF;
  border-radius: 3px;
  cursor: pointer;
  transition: all 0.3s ease;  
}
.over_btn:hover {
  color: #FFFFFF;
  background: #0D42A8;
}
</style>