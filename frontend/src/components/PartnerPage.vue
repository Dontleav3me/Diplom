<template>
  <div class="main">
    <div class="wrapper">
      <p class="head">Мы открыты ко всему новому и будем рады сотрудничеству</p>
      <p class="subhead">Наши партнеры играют ключевую роль в реализации проектов и предоставлении помощи населению</p>
      <p class="descr">Мы взаимодействуем с партнерами не только на коммерческой основе, но и в рамках взаимного усиления в продвижении инициатив и поддержки социальных проектов</p>
    </div>
    <div class="text_container">
      <p class="spectr_text">Мы развиваем широкий спектр проектов</p>
      <p class="spectr_subtext">И приглашаем инвесторов к сотрудничеству! Вместе мы можем реализовать масштабные миссии в области социальной защиты и благотворительности.</p>
    </div>
    <div class="card_container">
      <div class="card">
        <a href="https://kamaflow.com/ru/" target="_blank">
          <img src="../../static/img/kama_flow.jpg" alt="Kama Flow">
        </a>
      </div>
      <div class="card">
        <a href="https://www.ioffe.ru/ru/" target="_blank">
          <img src="../../static/img/fti.jpg" alt="FTI">
        </a>
      </div>
    </div>
    <button @click="this.$router.push('/contact')">Присоединиться к партнерству</button>
  </div>
</template>

<script>
export default {  

}
</script>

<style scoped>
.wrapper{
  display: flex;
  flex-direction: column;
  align-self: flex-start;
}
.main {
  margin: 30px 125px 20px 125px;
  display: flex;
  flex-direction: column;
  align-items: left;
}
p {
  margin: 0;
}
.head {
  font-family: Athelas;
  font-size: 64px;
  font-weight: 400;
  line-height: 71.68px;
  letter-spacing: -0.02em;
  text-align: justify;
  color: #191819;
  margin-bottom: 110px;
  max-width: 850px;
}
.subhead {
  font-family: Inter SemiBold;
  font-size: 24px;
  font-weight: 600;
  line-height: 29.05px;
  letter-spacing: -0.01em;
  text-align: justify;
  color: #191819;
  max-width: 650px;
  margin-bottom: 22px;
}
.descr {
  font-family: Inter Regular;
  font-size: 16px;
  font-weight: 400;
  line-height: 19.36px;
  letter-spacing: -0.01em;
  text-align: justify;
  color: #191819;
  max-width: 650px;
  margin-bottom: 60px;
}
.spectr_text {
  font-family: Inter SemiBold;
  font-size: 24px;
  font-weight: 600;
  line-height: 29.05px;
  letter-spacing: -0.01em;
  text-align: justify;
  color: #191819;
}
.spectr_subtext {
  font-family: Inter Regular;
  font-size: 16px;
  font-weight: 400;
  line-height: 19.36px;
  letter-spacing: -0.01em;
  text-align: justify;
  color: #191819;
}
.text_container {
  align-self: flex-end;
  max-width: 650px;
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 100px;
}
.card_container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(1fr);
  gap: 45px;
  justify-content: center;
  align-self: center;
  margin-bottom: 110px;
}
.card {
  display: flex;
  align-items: center;
  width: 300px;
  border-radius: 5px;
  border: 1px solid #0D42A8
}
button {  
  border: 1px solid #0D42A8;
  padding: 10px 120px;
  color: #0D42A8;
  font-family: Inter SemiBold;
  font-size: 16px;
  line-height: 19.36px;
  text-align: center;
  background: #FFFFFF;
  border-radius: 3px;
  cursor: pointer;
  transition: all 0.3s ease;  
  width: 40%;
  display: flex;
  justify-content: center;
  align-self: center;
}
button:hover {
  color: #FFFFFF;
  background: #0D42A8;
}
.card img{
  width: 100%;
  cursor: pointer;
}
@media (max-width: 797px) {
  .main { 
    margin: 30px 15px 20px 15px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .head{
    max-width: 500px;
    font-family: Athelas;
    font-size: 24px;
    line-height: 24.4px;
    letter-spacing: -0.02em;
    text-align: left;
    margin-bottom: 30px;
  }
  .subhead{
    font-family: Inter SemiBold;
    font-size: 14px;
    line-height: 16.52px;
    letter-spacing: -0.01em;
    text-align: justify;
    max-width: 360px;
  }
  .descr{
    font-family: Inter Regular;
    font-size: 12px;
    line-height: 16.1px;
    letter-spacing: -0.01em;
    text-align: justify;
    max-width: 300px;
    margin-bottom: 30px;
  }
  .spectr_text{
    font-family: Inter SemiBold;
    font-size: 14px;
    line-height: 16.52px;
    letter-spacing: -0.01em;
    text-align: justify;
  }
  .spectr_subtext{
    font-family: Inter Regular;
    font-size: 12px;
    line-height: 16.1px;
    letter-spacing: -0.01em;
    text-align: justify;
  }
  .text_container{
    max-width: 320px;
    margin-bottom: 30px;
  }
  .card_container{
    display: grid;
    grid-template-columns: repeat(1, 1fr);
    grid-template-rows: repeat(1fr);
    gap: 45px;
    justify-content: center;
    align-self: center;
    margin-bottom: 50px;
  }
  button{
    font-family: Inter SemiBold;
    font-size: 12px;
    font-weight: 600;
    line-height: 14.52px;
    letter-spacing: -0.01em;
    text-align: justify;
    padding: 15px 32px;
    width: auto;
  }
}
</style>
