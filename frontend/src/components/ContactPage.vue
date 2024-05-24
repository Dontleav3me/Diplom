<template>
  <div class="main">
    <div class="head">
      <p class="contact_text">Наши контакты</p>
      <p class="contact_subtext">Рады предоставить дополнительную информацию о работе МБОФ им. А. Невского и ответить на ваши вопросы. Для публикации в СМИ или для приглашения команды фонда на мероприятия пишите ппо контактам указанным для СМИ </p>
    </div>
    <div class="info_container">
      <div class="info_wrapper">
        <div class="info">
          <img src="../../static/img/mail.svg" alt="">
          <p class="info_text">Электронная почта: aiz-9465297@yandex.ru</p>
        </div>
        <div class="info">
          <img src="../../static/img/phone.svg" alt="">
          <p class="info_text">Телефон: +7 (812) 946-52-98</p>
        </div>
        <div class="info">
          <img src="../../static/img/geo.svg" alt="">
          <p class="info_text">Адрес: 197198, Россия, Санкт – Петербург,<br> ул. Съзжинская дом.22</p>
        </div>
      </div>
      <div class="proekt_container">
        <div class="proekt_content">
          <p class="proekt_text">
            Мы находимся здесь, чтобы помочь тем, кто оказался в тяжелой ситуации поддерживая как материально, так и духовно.
          </p>
          <img src="../../static/img/mailing.svg" alt="">
        </div>
        <div class="divider_proekt"></div>
      </div>
    </div>
    <div class="bottom">
      <div class="bottom_left">
        <p class="bottom_text">Телеграм</p>
        <p class="bottom_text">Tenchat</p>
        <p class="bottom_text">Вконтакте</p>
        <p class="bottom_text">Youtube</p>
      </div>
      <div class="bottom_right">
        <p class="bottom_text">@alekseypak</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.main{
  margin: 30px 125px 20px 125px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.contact_text{
  font-family: Athelas;
  font-size: 64px;
  line-height: 71.68px;
  letter-spacing: -0.02em;
  text-align: left;
  color: #191819;
}
.contact_subtext{
  font-family: Inter;
  font-size: 16px;
  line-height: 19.36px;
  letter-spacing: -0.01em;
  text-align: left;
  color: #191819;
  max-width: 500px;
}
.head{
  display: flex;
  align-items: center ;
  gap: 120px;
  margin-bottom: 115px;
}
p{
  margin: 0;
}
.info_text{
  font-family: Inter;
  font-size: 24px;
  font-weight: 600;
  line-height: 29.05px;
  letter-spacing: -0.01em;
  text-align: left;
  color: #191819;
}
.info{
  display: flex;
  gap: 15px;
}
.proekt_container {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}
.proekt_content {
  display: flex;
  gap: 20px;
  align-items: flex-start;
}
.proekt_text {
  font-family: Inter;
  font-size: 16px;
  line-height: 19.36px;
  letter-spacing: -0.01em;
  text-align: left;
  max-width: 420px;
  color: #191819;
}
.divider_proekt {
  border-bottom: 1px solid rgba(13, 66, 168, 1); 
  width: 453px;
  margin-top: 10px;
  margin-bottom: 35px;
}
.info_container{
  display: flex;
  gap: 115px;
  margin-bottom: 80px;
}
.info_wrapper{
  max-width: 550px;
  display: flex;
  flex-direction: column;
  gap: 30px;
  align-items: flex-start;
}
.bottom_left{
  border: 1px solid #0D42A8;
  background: #FFFFFF;
  padding: 10px 30px;
  display: flex;
  align-items: center;
  gap: 30px;
  height: 100%;
  border-radius: 3px;
}
.bottom_right{
  border: 1px solid #0D42A8;
  background: #FFFFFF;
  padding: 10px 45px;
  display: flex;
  align-items: center;
  gap: 30px;
  height: 100%;
  border-radius: 3px;
}
.bottom{
  display: flex;
  align-items: center;
  gap: 270px;
}
.bottom_text{
  font-family: Inter;
  font-size: 24px;
  font-weight: 600;
  line-height: 29.05px;
  letter-spacing: -0.01em;
  text-align: left;
  color: #0D42A8;
  cursor: pointer;
}
</style>