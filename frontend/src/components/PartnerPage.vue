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
      <div class="wide_card"></div>
      <div class="card"></div>
      <div class="card"></div>
      <div class="card"></div>
      <div class="card"></div>
      <div class="card"></div>
      <div class="card"></div>
    </div>
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
  text-align: left;
  color: #191819;
}
.spectr_subtext {
  font-family: Inter Regular;
  font-size: 16px;
  font-weight: 400;
  line-height: 19.36px;
  letter-spacing: -0.01em;
  text-align: left;
  color: #191819;
}
.text_container {
  align-self: flex-end;
  max-width: 650px;
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 190px;
}
.card_container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(2, 1fr);
  gap: 45px;
  justify-content: center;
  align-self: center;
}
.card {
  width: 240px;
  height: 240px;
  background: #0D42A8;
  border-radius: 5px;
}
.wide_card {
  grid-column: span 2;
  background: #0D42A8;
  border-radius: 5px;
}
</style>
