<template>
  <div class="bg">
    <div class="main">
      <p class="mission">Миссия фонда</p>
      <p class="main_text">Мы направляем наши усилия на изыскание и поддержку стратегически-важных проектов и ключевых инициатив. Согласно указу Президента о национальных целях развития Российской Федерации на период до 2030 года и на перспективу до 2036 года и Посланию Президента Федеральному Собранию деятельность Фонда направлена на улучшение качества жизни граждан Российской Федерации через содействие в реализации приоритетных Государственных программ, способствующих развитию общества и экономики и укреплению здоровья нации.
        Деятельность фонда сфокусирована на следующих направлениях: сохранении истинного культурно-исторического наследия России, морально-нравственном, военно- патриотическом и духовном воспитании молодежи, а также сохранении связи поколений и традиционных семейных ценностей, формировании доступной и комфортной среды в сферах образования, досуга и спорта. Особое внимание уделяется поддержке и развитию проектов в области инновационных технологий, цифровизации, и передовым разработкам, а также межотраслевой синергии, способствующей импортозамещению.
        Мы верим, что совместными усилиями государства, бизнеса и гражданского общества мы можем добиться устойчивого и долгосрочного благополучия для всех россиян.</p>
      <p class="trends">Направления развития</p>
      <div class="main_container">
        <TrendsCard v-for="(direction, index) in directions" :key="index" :direction="direction" ></TrendsCard>
      </div>
    </div>
  </div>
</template>

<script>
import TrendsCard from '../components/TrendsCard.vue'
import axios from 'axios'
export default {
  components: { TrendsCard},
  data() {
    return {
      directions: []

    }
  },
  methods: {
    async get_directions(){
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/directions/`);
        this.directions = response.data;
      } catch (error) {
        console.error('Error fetching uslugi:', error);
      }
    },
},
mounted(){
  this.get_directions();
}
}
</script>

<style scoped>
.bg{
  position: relative;
  z-index: 1;
  background: 
    url(../../static/img/Vector2.png) no-repeat,
    url(../../static/img/Vector3.png) no-repeat;
  object-fit: cover;
  background-repeat: no-repeat;
  background-size: 100% 450px, 100% 600px;
  background-position: top left, bottom left;
}
.main {
  margin: 30px 125px 20px 125px;
  display: flex;
  flex-direction: column;
  align-items: left;
}
.mission{
  font-family: Athelas;
  font-size: 64px;
  font-weight: 400;
  line-height: 71.68px;
  letter-spacing: -0.02em;
  text-align: left;
  color: #191819;
  margin-bottom: 80px;
}
.main_text{
  font-family: Inter Medium;
  font-size: 21px;
  line-height: 29.05px;
  letter-spacing: -0.01em;
  text-align: justify;
  color: #191819;
  max-width: 1200px;
  margin-bottom: 50px;
}
p{
  margin: 0;
}
.content{
  font-family: Athelas;
  font-size: 40px;
  font-weight: 400;
  line-height: 44.8px;
  letter-spacing: -0.01em;
  text-align: left;
  color: #191819;
  max-width: 350px;
  align-self: center;
  margin-bottom: 200px;
}
.trends{
  font-family: Athelas;
  font-size: 64px;
  font-weight: 400;
  line-height: 71.68px;
  letter-spacing: -0.01em;
  text-align: left;
  color: #191819;
  margin-bottom: 100px;
}
.main_container{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: 1fr;
  gap: 60px;
}
@media (max-width: 797px) {
  .main { 
    margin: 30px 15px 20px 15px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }
  .mission{
    max-width: 500px;
    font-family: Athelas;
    font-size: 24px;
    line-height: 24.4px;
    letter-spacing: -0.02em;
    text-align: left;
    margin-bottom: 30px;
  }
  .main_text{
    font-family: Inter Regular;
    font-size: 12px;
    line-height: 16.1px;
    letter-spacing: -0.01em;
    text-align: justify;
  }
  .trends{
    max-width: 500px;
    font-family: Athelas;
    font-size: 24px;
    line-height: 24.4px;
    letter-spacing: -0.02em;
    text-align: left;
    margin-bottom: 30px;
  }
  .main_container{
    align-self: center;
    display: grid;
    grid-template-columns: repeat(1, 1fr);
    grid-template-rows: 1fr;
    gap: 60px;
  }
}
</style>
