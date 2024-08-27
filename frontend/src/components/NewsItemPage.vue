<template>
  <div class="main">
    <img :src="img_mobile" alt="" class="mobile">
    <div class="head">
        <img :src="img_items" alt="" class="pc">
        <div class="head_container">
            <p class="head_text">{{ header_items }}</p>
            <p class="head_subtext">{{ name_items }}</p>
        </div>
    </div>
    <p class="head_subtext_bottom">{{ subname_items }}</p>

  </div>
</template>
0
<script>
import axios from 'axios'

export default {
    props: ['userId'],
    data() {
        return {
            items: [],
            header_items: "",
            name_items: "",
            subname_items: "",
            img_mobile: "",
            img_items: "",
        }
    },
    mounted() {
      this.get_solonews()
    },
    methods: {
      async get_item() {
      try {
        const response = await this.$axios.get('/get_item/', {
          params: { 'user_id': this.userId }
        });
        this.items = response.data;
      } catch (error) {
        console.error('Error fetching daily reward status:', error);
      }
    },
    async get_solonews(){
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/solo_news/`);
        this.header_items = response.data[0].header_items;
        this.name_items = response.data[0].name_items;
        this.subname_items = response.data[0].subname_items;
        this.img_mobile = 'http://127.0.0.1:8000'+response.data[0].img_mobile;
        this.img_items = 'http://127.0.0.1:8000'+response.data[0].img_items;
      } catch (error) {
        console.error('Error fetching uslugi:', error);
      }
    },
  }
}

</script>

<style scoped>
.main {
    margin: 30px 125px 20px 125px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }
.head{
    display: flex;
    gap: 20px;
    margin-bottom: 10px;
}
.head_container{
    display: flex;
    flex-direction: column;
    gap: 20px;
    max-width: 600px;
}
.head_text{
    font-family: Athelas;
    font-size: 48px;
    font-weight: 400;
    line-height: 64px;
    text-align: justify;
    color: #000000;
}
.head_subtext{
    font-family: Inter Medium;
    font-size: 14px;
    font-weight: 400;
    line-height: 22px;
    text-align: justify;
}
.head_subtext_bottom{
    font-family: Inter Medium;
    font-size: 14px;
    font-weight: 400;
    line-height: 22px;
    text-align: justify;
    max-width: 890px;
}
p{
    margin: 0;
}
img{
    border-radius: 5px;
}
.mobile{
    display: none;
}
@media (max-width: 797px) {
    .main { 
        margin: 30px 15px 20px 15px;
        display: flex;
        flex-direction: column;
        align-items: center;
      }
    .head_text{
        font-family: Athelas;
        font-size: 24px;
        line-height: 24.92px;
        letter-spacing: -0.01em;
        text-align: justify;
        margin-bottom: 30px;
    }
    .mobile{
        display: block;
        margin-bottom: 30px;
    }
    .pc{
        display: none;
    }
}
</style>