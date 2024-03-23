<script>
import TheWelcome from '../components/TheWelcome.vue'
import NavBar from '@/components/Home/NavBar.vue';
import Hero1 from '@/components/Home/Hero1.vue'
import CarouselVue from '../components/Home/Carousel.vue';
export default {
  components:{
    TheWelcome,
    NavBar,
    Hero1,
    CarouselVue
  }
}
</script>


<template>
  <div class="main-section"> 
    <div class="center-hero">
      <Hero1 ></Hero1>
    </div>
    <CarouselVue></CarouselVue>  
  </div>
</template>

<style>

  .center-hero {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .hero-image {
    height: 600px;
    width: 600px;

  }

</style>
