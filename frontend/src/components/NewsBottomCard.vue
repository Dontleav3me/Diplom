<template>
  <div class="news_card" @click="goToDetailPage">
    <img :src="image" alt="">
    <div class="news_container">
      <p class="news_heads">{{ NewsBottom.name }}</p>
      <p class="news_subhead">{{ NewsBottom.subname }}</p>
    </div>
    <div class="card_head">
      <p class="card_text">{{ NewsBottom.dela }}</p>
      <div class="divider_card"></div>
      <p class="card_text">{{ NewsBottom.time }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      image: ''
    }
  },
  props: ['NewsBottom'],
  mounted(){
    this.image =  'http://127.0.0.1:8000'+this.NewsBottom.image
  },
  methods: {
    goToDetailPage() {
      this.$router.push({ 
        name: 'NewsDetailBottomPage', 
        params: { id: this.NewsBottom.id }, 
      });
    }
  }
}
</script>

<style scoped>
p{
  margin: 0;
}
.news_card{
  display: flex;
  flex-direction: column;
  gap: 15px;
  max-width: 320px;
  cursor: pointer;
}
.news_container{
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.news_heads{
  font-family: Inter Regular;
  font-size: 20px;
  font-weight: 400;
  line-height: 26px;
  text-align: justify;
  color: #000000;
  transition: all 0.3s ease;
}
.news_heads:hover{
  color: #0D42A8;
  cursor: pointer;
}
.news_subhead:hover{
  color: #0D42A8;
  cursor: pointer;
}
.news_subhead{
  font-family: Inter Regular;
  font-size: 14px;
  font-weight: 400;
  line-height: 22px;
  text-align: justify;
  color: #3D3D3D;
  transition: all 0.3s ease;
}
.card_text{
  font-family: Inter Regular;
  font-size: 12px;
  font-weight: 400;
  line-height: 18px;
  text-align: left;
  color: #000000CC;
}
.card_head{
  display: flex;
  gap: 16px;
}
.divider_card{
  border: 1px solid #000000A3;
}
img{
  border-radius: 5px;
  width: 316px;
  height: 280px;
}
</style>