<template>
  <div class="footer">
    <div class="footer_container">
      <div class="buttons">
        <div class="menu">
          <p class="buttons_text">Меню</p>
          <div class="submenu">
            <p class="buttons_subtext" @click="this.$router.push('/about')">О нас</p>
            <p class="buttons_subtext" @click="this.$router.push('/trends')">Направления</p>
            <p class="buttons_subtext" @click="this.$router.push('/news') " style="display: none;">Новости</p>
            <p class="buttons_subtext" @click="this.$router.push('/')">Главная</p>
          </div>
        </div>
        <div class="menu">
          <p class="buttons_text">Сотрудничество</p>
          <div class="submenu">
            <p class="buttons_subtext" @click="this.$router.push('/partner')">Партнёрство</p>
            <p class="buttons_subtext" @click="this.$router.push('/contact')">Вакансии</p>
            <p class="buttons_subtext" @click="this.$router.push('/contact')">Контакты</p>
            <p class="buttons_subtext" style="display: none;">Награды</p>
          </div>
        </div>
        <div class="menu">
          <p class="buttons_text">Социальные сети</p>
          <div class="submenu">
            <p class="buttons_subtext">Телеграм</p>
            <p class="buttons_subtext">Вконтакте</p>
            <p class="buttons_subtext">Twitter</p>
            <p class="buttons_subtext">Почта</p>
          </div>
        </div>
      </div>
      <div class="mailing">
        <div class="mailing_container" style="display: none;">
          <p class="mailing_text" >Подписаться на рассылку</p>
          <img src="../../static/img/mailing.svg" alt="">
        </div>
        <div class="divider"></div>
      </div>
    </div>
    <div class="mailing_mobile" style="display: none;">
      <div class="mailing_container">
        <p class="mailing_text">Подписаться на рассылку</p>
        <img src="../../static/img/mailing.svg" alt="">
      </div>
      <div class="divider otrez"></div>
    </div>
    <div class="footer_bottom">
      <div class="divider"></div>
      <div class="footer_wrapper">
        <p class="bottom_text">МБОФ им. А. Невского © 1996–2025</p>
        <div class="bottom_right" style="display: none;">
          <p class="bottom_text">Terms & policies</p>
          <p class="bottom_text">Privacy policy</p>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.mailing{
  display: flex;
  flex-direction: column;
  gap: 15px;
}
.mailing_container{
  display: flex;
  align-items: flex-start;
  gap: 95px;
}
.mailing_text{
  color: #0D42A8;
  font-size: 16px;
  text-align: left;
  font-family: Inter Medium;
  cursor: pointer;
}
.footer_container{
  display: flex;
  justify-content: space-between;
}
.buttons_text{
  color: #191819;
  font-size: 21px;
  text-align: left;
  font-family: Inter Medium;
  user-select: none;
}
.buttons_subtext{
  color: #191819;
  font-size: 13 px;
  text-align: left;
  font-family: Inter Medium;
  user-select: none;
  cursor: pointer;
  transition: all 0.3s ease;
}
.buttons_subtext:hover{
  color: #0D42A8;
}
.footer{
  display: flex;
  flex-direction: column;
  margin: 100px 65px 30px 65px;
  justify-content: center;
  gap: 65px;
}
.buttons{
  display: flex;
  gap: 70px;
}
p{
  margin: 0;
}
.menu{
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.submenu{
  display: flex;
  flex-direction: column;
  gap: 17px;
}
.divider {
  border-bottom: 1px solid rgba(13, 66, 168, 1); 
  width: auto;
}
.bottom_text{
  color: #0D42A8;
  font-size: 12px;
  text-align: left;
  font-family: Inter Regular;
}
.footer_bottom{
  display: flex;
  flex-direction: column;
  gap: 15px;
}
.footer_wrapper{
  display: flex;
  justify-content: space-between;
}
.bottom_right{
  display: flex;
  gap: 35px;
}
.mailing_mobile{
  display: none;
}
@media (max-width: 797px) {
  .buttons{
    gap: 50px;
  }
  .buttons_text{
    font-family: Inter Medium;
    font-size: 12px;
    line-height: 12.1px;
    letter-spacing: 0.01em;
    text-align: left;
  }
  .buttons_subtext{
    font-family: Inter Medium;
    font-size: 10px;
    line-height: 9.68px;
    letter-spacing: 0.01em;
    text-align: left;
  }
  .footer{
    margin: 60px 0 30px 0;
    gap: 30px;
  }
  .mailing{
    display: none;
  }
  .mailing_mobile{
    display: block;
    max-width: 242px;
  }
  .footer_container{
    justify-content: center;
    margin: 0 20px;
  }
  .mailing_container{
    margin-left: 10px;
    gap: 10px;
    align-items: center;
  }
  .otrez{
    margin-top: 10px;
    max-width: auto;
    margin-left: 10px;
  }
  .bottom_right{
    display: none;
  }
  .bottom_text{
    margin-left: 10px;
  }
}
</style>