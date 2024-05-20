<script>
import TheWelcome from '../components/TheWelcome.vue'
import NavBar from '@/components/Home/NavBar.vue';
import Hero1 from '@/components/Home/Hero1.vue';
import Hero2 from '@/components/Home/Hero2.vue'
import CarouselVue from '../components/Home/Carousel.vue';
import FAQVue from '../components/Home/FAQ.vue';
export default {
  components:{
    TheWelcome,
    NavBar,
    Hero1,
    Hero2,
    CarouselVue,
    FAQVue
  }
}
</script>


<template>
  <div class="main-section"> 
    <div class="center-hero">
      <Hero1 ></Hero1>
    </div>
    <CarouselVue></CarouselVue> 
    <div class="center-hero">
      <Hero2 ></Hero2>
    </div>
    <FAQVue></FAQVue> 
  </div>
</template>

<style>
  .main-section {
    width: 100%;
  }

  .center-hero {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .hero-image {
    height: 600px;
    width: 600px;

  }
  .faq-section {
    width: 100%;
  }

</style>
