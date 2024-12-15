<template>
  <div class="card">
    <p class="card_text">{{ project.name }}</p>
    <p class="card_subtext">{{ project.subname }}</p>
    <button class="card_btn" @click="goToDetailPage" style="display: none">Подробнее</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      
    }
  },
  props: ['project'],
  methods: {
    goToDetailPage() {
      this.$router.push({ 
        name: 'ProjectDetailPage', 
        params: { id: this.project.id }, 
      });
    }
  }
}
</script>

<style scoped>
.card {
  width: auto;
  padding: 48px;
  border: 1px solid #0D42A8;
  display: flex;
  flex-direction: column;
  gap: 20px;
  border-radius: 5px;
}
.card_text {
  font-family: Inter SemiBold;
  font-size: 24px;
  line-height: 29.05px;
  letter-spacing: -0.01em;
  text-align: justify;
  color: #191819;
}
.card_subtext {
  font-family: Inter Regular;
  font-size: 16px;
  line-height: 19.36px;
  letter-spacing: -0.01em;
  text-align: justify;
  color: #191819;
}
.card_btn {
  width: auto;
  border: 1px solid #0D42A8;
  padding: 10px 100px 10px 100px;
  color: #0D42A8;
  font-family: Inter;
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
  font-family: Inter SemiBold;
}
.card_btn:hover {
  color: #FFFFFF;
  background: #0D42A8;
}
p{
  margin: 0;
}
@media (max-width: 797px) {
  .card_text{
    font-family: Inter Medium;
    font-size: 16px;
    line-height: 14.52px;
    letter-spacing: -0.01em;
    text-align: justify;
  }
  .card_subtext{
    font-family: Inter Regular;
    font-size: 14px;
    line-height: 19px;
    letter-spacing: -0.01em;
    text-align: justify;
  }
  .card_btn{
    font-family: Inter SemiBold;
    font-size: 12px;
    font-weight: 600;
    line-height: 14.52px;
    letter-spacing: -0.01em;
    text-align: justify;
  }
  .card{
    padding: 20px;
  }
}
</style>