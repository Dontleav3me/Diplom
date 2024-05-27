<template>
  <div class="news_card">
    <div class="img_container">
      <img :src="image" alt="">
    </div>
    <p class="news_text">{{ mininew.name }}</p>
  </div>  
</template>

<script>
export default {
  data() {
    return {
      image: ''
    }
  },
  props: ['mininew'],
  mounted(){
    console.log('77777777777',this.mininew)
    this.image = 'http://127.0.0.1:8000' + this.mininew.image;
    console.log('121312312312312312312',this.image)
  },

}
</script>

<style scoped>
p{
  margin: 0;
}
.news_card{
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 25px;
  background: #4386C4;
  padding: 38px;
  border-radius: 3px;
}
.img_container{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 50px;
  height: 50px;
  background: #FFFBFB;
}
.news_text{
  font-family: Inter;
  font-size: 16px;
  line-height: 19.36px;
  letter-spacing: -0.01em;
  text-align: left;
  color: #FFFBFB;
}
</style>