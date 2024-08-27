<template>
  <div class="card">
    <p class="card_text">{{ direction.name }}</p>
    <transition name="fade" mode="out-in">
      <div v-if="!showDetails" class="img_container" key="image">
        <img :src="image" alt="">
        <button @click="toggleDetails" class="img_btn">Подробнее</button>
      </div>
      <div v-else class="details_container" key="details">
        <p class="card_text_flipped">{{ direction.subname }}</p>
        <button @click="toggleDetails" class="back_btn">Назад</button>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  data() {
    return {
      image: '',
      showDetails: false
    }
  },
  props: ['direction'],
  mounted(){
    this.image = 'http://127.0.0.1:8000' + this.direction.image
  },
  methods: {
    toggleDetails() {
      this.showDetails = !this.showDetails;
    }
  }
}
</script>

<style scoped>
.details_container{
  padding: 20px;
}
.card {
  display: flex;
  flex-direction: column;
  gap: 20px;
  align-items: center;
}
.card_text_flipped{
  color: #FFFFFF;
  font-family: Athelas;
  font-size: 20px;
  line-height: 28px;
  text-align: justify;
}
.card_text {
  font-family: Athelas;
  font-size: 40px;
  font-weight: 400;
  line-height: 44.8px;
  letter-spacing: -0.01em;
  text-align: center;
  color: #191819;
}

.img_container {
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

img {
  border-radius: 5px;
  width: 495px;
  height: 305px;
  transition: opacity 0.5s ease;
}

.details_container {
  position: relative;
  display: flex;
  flex-direction: column;
  width: 495px;
  height: 265px;
  background-color: #4386C4;
  border-radius: 5px;
  transition: opacity 0.5s ease;
}

.back_btn {
  position: absolute;
  width: auto;
  border: 1px solid #0D42A8;
  padding: 10px 20px;
  color: #0D42A8;
  font-family: Inter SemiBold;
  font-size: 16px;
  line-height: 19.36px;
  text-align: center;
  background: transparent;
  border-radius: 3px;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-top: 20px;
  bottom: -42px;
  right: 0;
}
.back_btn:hover{
  color: #FFFFFF !important;
  background: #0D42A8 !important;
}

.back_btn:hover {
  background: #FFFFFF;
  color: #4386C4;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.4s ease;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}

p {
  margin: 0;
}

@media (max-width: 797px) {
  .card_text {
    max-width: 500px;
    font-family: Athelas;
    font-size: 24px;
    line-height: 24.4px;
    letter-spacing: -0.02em;
    text-align: left;
    margin-bottom: 0;
  }

  img, .details_container {
    border-radius: 5px;
    width: 350px;
    height: 200px;
  }
}
</style>
