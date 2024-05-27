<template>
  <div class="news_card">
    <img :src="NewsBottom.img" alt="">
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
      
    }
  },
  props: ['NewsBottom'],
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
}
.news_container{
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.news_heads{
  font-family: Inter;
  font-size: 20px;
  font-weight: 400;
  line-height: 26px;
  text-align: left;
  color: #000000;
}
.news_subhead{
  font-family: Inter;
  font-size: 14px;
  font-weight: 400;
  line-height: 22px;
  text-align: left;
  color: #3D3D3D;
}
.card_text{
  font-family: Inter;
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
}
</style>