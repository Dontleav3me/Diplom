<template>
  <div class="header_card" @click="goToDetailPage">
    <img :src="image" alt="">
    <div class="header_card_container">
      <div class="card_head">
        <p class="card_text">{{ NewsTop.head }}</p>
        <div class="divider_card"></div>
        <p class="card_text">{{ NewsTop.date }}</p>
      </div>
      <p class="card_main_text">{{ NewsTop.name }}</p>
      <div class="card_head">
        <p class="card_text">{{ NewsTop.dela }}</p>
        <div class="divider_card"></div>
        <p class="card_text">{{ NewsTop.time }}</p>
      </div>
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
  props: ['NewsTop'],
  mounted(){
    this.image = 'http://127.0.0.1:8000' + this.NewsTop.image;
  },
  methods: {
    goToDetailPage() {
      this.$router.push({ name: 'NewsDetailPage', params: { id: this.NewsTop.id } });
    }
  }
}
</script>

<style scoped>
.header_card{
  display: flex;
  align-items: flex-start;
  gap: 20px;
}
p{
  margin: 0;
}
.header_card_container{
  max-width: 270px;
  display: flex;
  flex-direction: column;
  gap: 15px;
}
.card_head{
  display: flex;
  gap: 16px;
}
.divider_card{
  border: 1px solid #000000A3;
}
.card_text{
  font-family: Inter Regular;
  font-size: 12px;
  font-weight: 400;
  line-height: 18px;
  text-align: left;
  color: #000000CC;
}
.card_main_text{
  font-family: Inter Regular;
  font-size: 20px;
  font-weight: 400;
  line-height: 26px;
  text-align: justify;
  color: #000000;
  transition: all 0.3s ease;
}
img{
  width: 114px;
  height: 118px;
  border-radius: 5px;
  cursor: pointer;
  object-fit: cover;
}
.card_main_text:hover{
  color: #0D42A8;
  cursor: pointer;
}
@media (max-width: 797px) {
  .card_text{
    font-family: Athelas;
    font-size: 64px;
    font-weight: 400;
    line-height: 71.68px;
    letter-spacing: -0.02em;
    text-align: left;
    color: #191819;
    display: flex;
    align-self: flex-start;
  }
}
</style>
