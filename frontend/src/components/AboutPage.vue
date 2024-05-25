<template>
  <div class="main">
    <p class="development">Развитие фонда<br> имени Александра Невского</p>
    <div class="history">
      <p class="history_text">
        Мы находимся здесь, чтобы помочь тем, кто оказался в тяжелой ситуации поддерживая как материально, так и духовно.
      </p>
      <div class="divider"></div>
    </div>
    
  </div>
  
</template>

<script>
export default {

}
</script>

<style scoped>
.main {
  margin: 30px 125px 20px 125px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.development{
  font-family: Athelas;
  font-size: 64px;
  font-weight: 400;
  line-height: 71.68px;
  letter-spacing: -0.02em;
  text-align: left;
  color: #191819;
  display: flex;
  align-self: flex-start;
  margin-bottom: 80px;
}
.history{
  display: flex;
  flex-direction: column;
  max-width: 458px;
  align-self: flex-end;
}
.history_text {
  font-family: Inter;
  font-size: 16px;
  line-height: 19.36px;
  letter-spacing: -0.01em;
  text-align: left;
  color: #191819;
}
.divider {
  border-bottom: 1px solid rgba(13, 66, 168, 1); 
  margin-top: 10px;
  max-width: 430px;
}
p{
  margin: 0;
}
</style>