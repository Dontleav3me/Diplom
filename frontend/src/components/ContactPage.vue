<template>
  <div class="main">
    <div class="head">
      <p class="contact_text">Наши контакты</p>
      <p class="contact_subtext">Рады предоставить дополнительную информацию о работе МБОФ им. А. Невского и ответить на ваши вопросы. Для публикации в СМИ или для приглашения команды фонда на мероприятия пишите ппо контактам указанным для СМИ </p>
    </div>
    <div class="proekt_container mobile">
      <div class="proekt_content">
        <p class="proekt_text">
          Мы находимся здесь, чтобы помочь тем, кто оказался в тяжелой ситуации поддерживая как материально, так и духовно.
        </p>
        <img src="../../static/img/mailing.svg" alt="">
      </div>
      <div class="divider_proekt"></div>
    </div>
    <div class="info_container">
      <div class="info_wrapper">
        <div class="info">
          <img src="../../static/img/mail.svg" alt="">
          <p class="info_text">Электронная почта: info@foundation-an.ru</p>
        </div>
        <div class="info">
          <img src="../../static/img/phone.svg" alt="">
          <p class="info_text">Телефон: +7 (812) 426-70-77</p>
        </div>
        <div class="info">
          <img src="../../static/img/geo.svg" alt="">
          <p class="info_text">Адрес: 197198, Россия, Санкт – Петербург,<br> ул. Съзжинская дом.22</p>
        </div>
      </div>
      <div class="proekt_container pc">
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
      <div class="bottom_right pc">
        <p class="bottom_text">@alekseypak</p>
      </div>
    </div>
    <p class="bottom_text_info mobile">Рады предоставить дополнительную информацию о работе МБОФ им. А. Невского и ответить на ваши вопросы. Для публикации в СМИ или для приглашения команды фонда на мероприятия пишите по контактам указанным для СМИ </p>
    <div class="niz mobile">
      <div class="bottom_right mobile">
        <p class="bottom_text">@alekseypak</p>
      </div>
      <p class="bottom_text_black">Контакты для СМИ</p>
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
  font-family: Inter Regular;
  font-size: 16px;
  line-height: 19.36px;
  letter-spacing: -0.01em;
  text-align: justify;
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
  font-family: Inter SemiBold;
  font-size: 24px;
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
  font-family: Inter Regular;
  font-size: 16px;
  line-height: 19.36px;
  letter-spacing: -0.01em;
  text-align: justify;
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
  font-family: Inter SemiBold;
  font-size: 24px;
  line-height: 29.05px;
  letter-spacing: -0.01em;
  text-align: left;
  color: #0D42A8;
  cursor: pointer;
}
.mobile{
  display: none;
}
@media (max-width: 797px) {
  .head{
    margin: 0;
  }
  .main { 
    margin: 30px 15px 20px 15px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }
  .contact_text{
    max-width: 500px;
    font-family: Athelas;
    font-size: 24px;
    line-height: 24.4px;
    letter-spacing: -0.02em;
    text-align: left;
    margin-bottom: 30px;
  }
  .contact_subtext{
    display: none;
  }
  .mobile{
    display: block;
  }
  .pc{
    display: none;
  }
  .info_text{
    font-family: Inter SemiBold;
    font-size: 12px;
    line-height: 14.52px;
    letter-spacing: -0.01em;
    text-align: justify;
  }
  .bottom_text{
    font-family: Inter SemiBold;
    font-size: 14px;
    line-height: 16.52px;
    letter-spacing: -0.01em;
    text-align: justify;
  }
  .niz{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 5px;
  }
  .bottom_text_black{
    font-family: Inter Medium;
    font-size: 14px;
    line-height: 16.52px;
    letter-spacing: -0.01em;
    text-align: justify;
    color: #191819;
  }
  .bottom_text_info{
    font-family: Inter Medium;
    font-size: 14px;
    line-height: 16.68px;
    letter-spacing: -0.01em;
    text-align: justify;
    color: #191819;
    margin-bottom: 30px;
  }
  .bottom_left{
    margin-bottom: 30px;
  }
  .info_container{
    margin-bottom: 30px;
  }
  .proekt_text{
    font-family: Inter Medium;
    font-size: 12px;
    font-weight: 400;
    line-height: 16.1px;
    letter-spacing: -0.01em;
    text-align: left;

  }
  .proekt_container {
    max-width: 350px;
    align-self: flex-end;
  }
  .divider_proekt{
    width: auto;
  }
}
</style>