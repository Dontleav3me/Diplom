<template>
  <div class="main">
    <img src="../../static/img/logo_error.svg" alt="" class="img_error" draggable="false">
    <p class="main_text">Приносим извинения за предоставленные неудобства</p>
    <p class="main_subtext">Страница не найдена<br>Ошибка 404</p>
    <button class="back" @click="this.$router.push('/')">Вернуться на  главную страницу</button>
    <div class="container">
      <p class="main_descr">МБОФ им. А. Невского © 2015–2024</p>
      <p class="main_descr cursor">Terms & policies</p>
      <p class="main_descr cursor">Privacy policy</p>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped> 
.main{  
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.img_error{
  margin-top: 30px;
  margin-bottom: 20px;
}
.main_text{
  font-family: Athelas;
  font-size: 64px;
  font-weight: 400;
  line-height: 68px;
  text-align: center;
  color: #191819;
  max-width: 811px;
  margin-bottom: 40px;
}
.main_subtext{
  font-family: Athelas;
  font-size: 48px;
  font-weight: 400;
  line-height: 64px;
  text-align: center;
  color: #191819;
  max-width: 450px;
  margin-bottom: 50px;
}
p{
  margin: 0;
}
.back {  
  width: auto;
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
}
.back:hover {
  color: #FFFFFF;
  background: #0D42A8;
}
.container{
  margin-top: 100px;
  display: flex;
  gap: 35px;
}
.main_descr{
  font-family: Inter Regular;
  font-size: 12px;
  font-weight: 400;
  line-height: 21px;
  text-align: left;
  color: #191819;
}
.cursor{
  cursor: pointer;
}
.cursor:hover{
  color: #0D42A8;
}
</style>