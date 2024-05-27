<template>
  <div class="card">
    <p class="card_text">{{ direction.name }}</p>
    <div class="img_container">
      <img src="{{ direction.image }}" alt="" class="">
      <button class="img_btn">Подробнее</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      
    }
  },
  props: ['direction'],
}
</script>

<style scoped>
.card{
  display: flex;
  flex-direction: column;
  gap: 20px;
  align-items: center;
}
.card_text{
  font-family: Athelas;
  font-size: 40px;
  font-weight: 400;
  line-height: 44.8px;
  letter-spacing: -0.01em;
  text-align: left;
  color: #191819;  
}
.img_container{
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}
.img_btn {  
  width: auto;
  border: 1px solid #0D42A8;
  padding: 10px 20px;
  color: #0D42A8;
  font-family: Inter SemiBold;
  font-size: 16px;
  line-height: 19.36px;
  text-align: center;
  background: #FFFFFF;
  border-radius: 3px;
  cursor: pointer;
  transition: all 0.3s ease;
}
.img_btn:hover {
  color: #FFFFFF;
  background: #0D42A8;
}
img{
  border-radius: 5px;
}
p{
  margin: 0;
}
</style>