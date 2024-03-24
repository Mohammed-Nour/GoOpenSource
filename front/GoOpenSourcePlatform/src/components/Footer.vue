<template>
    <section class="empty"></section>
   <hr class="line">
  <footer class="footer-info">
    <div class="company-logo">
      <a id="inno-logo" href="https://innopolis.university/" ><img src="../assets/images/InnopolisULogo.svg" alt="goOS-logo"></a>
      <a href="https://engineers2030.ru/"><img src="../assets/images/SchoolofAELogo.svg" alt="goOS-logo"></a>
    </div>
    <div class="footer-navigation">
      <ul class="nav-sections">
        <li class="nav-colm">
          <div class="section-name">Projects</div>
          <ul class="section-elements">
            <li><RouterLink to="/projects">UI ChatBot</RouterLink></li>
            <li><RouterLink to="/projects">AI Image generator</RouterLink></li>
          </ul>
        </li>
        <li class="nav-colm">
          <div class="section-name">Company</div>
          <ul class="section-elements">
            <li><RouterLink to="/about_us" class="navbar-txt">About Us</RouterLink></li>
          </ul>
        </li>
        <li class="nav-colm">
          <div class="section-name">Resources</div>
          <ul class="section-elements">
            <li><a href="#">Contacts</a></li>
            <li><a href="#">Documentation</a></li>
          </ul>
        </li>
      </ul>
    </div>

  </footer>
     <!-- Footer -->
    <footer class="footer-links">
        <div class="footer-logos">
            <div class="space"><a href="https://t.me/universityinnopolis?lang=ru&id=12&site=s1&template=university24&landing_mode=edit"><img src="@/assets/public/telegram.svg" alt="tg-logo" ></a> </div>
            <div class="space"><a href="https://vk.com/innopolisu?lang=ru&id=12&site=s1&template=university24&landing_mode=edit"><img src="@/assets/public/vk.svg" alt="fb-logo"></a> </div>
            <div class="space"><a href="https://www.youtube.com/user/InnopolisU?lang=ru&id=12&site=s1&template=university24&landing_mode=edit"><img src="@/assets/public/youtube.svg" alt="inst-logo"></a> </div>
        </div>
        <ul class="footer-list">
            <li><a class="footer-txt" href="#">Terms of Service</a></li>
            <li><a class="footer-txt" href="#">Privacy Policy</a></li>
            <li><a class="footer-txt" href="#">Cookies</a></li>
        </ul>
    </footer>
</template>

<style scoped>
    
.empty{
    height: 15vh;
    width: 100%;
}
.footer-logos {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.footer-info {
  position: inline-block;
  right: 0;
  bottom: 0;
  z-index: 1000;
  width: 100%;
  /* display: none;*/
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 25px 13.5%;
  /* background: transparent; */
  margin-top: 25px;
}
.nav-sections {
  display: flex;
  flex-direction: row;
}
.nav-colm {
  margin-left: 85px;
}




#inno-logo {
  padding-right: 0.5rem;
}
hr {
  border: none;
  border-top: 1px solid #c7c7c7;
  width: 90%;
  text-align: center;
  margin: 0 auto;
}
.section-name {
  color: #000;
  font-family: Raleway;
  font-size: 20px;
  font-style: normal;
  font-weight: 600;
  margin-bottom:15px;
}
.section-elements li {
  font-family: Raleway;
  font-size: 16px;
  font-style: normal;
  font-weight: 400;
  line-height: 200%;
}

.section-elements li:hover {
  text-decoration: underline;
}

.section-elements li a {
  color: black;
}



.footer-links {
    position: inline-block;
    right: 0;
    bottom: 0;
    z-index: 1000;
    width: 100%;
    background-color: #06b6d4;
   /* display: none;*/
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 25px 13.5%;
    margin-top: 25px;
}
.space {
  margin: auto 85px auto auto;
}
.footer-logos div a img{
  transform: scale(1.25);
  transition: all .55s ease;
  /* color: white; */

}
.footer-logos div a img:hover{
  transform: scale(1.4);
  filter: opacity(0.5);
  /* color: white; */
}
.footer-list{
    display: flex;
}
.footer-txt{
  color: #FFF;
  text-align: center;
  font-family: Raleway;
  font-size: 16px;
  font-style: normal;
  font-weight: 400;
  line-height: 27.5px;
    margin: auto auto auto 85px;
    border-bottom: 3px solid transparent;
    transition: all .55s ease;
}

.footer-txt:hover{
  text-decoration: underline;
}
@media only screen and (max-width: 1400px) {
  .footer-txt{
    margin: auto auto auto 65px;
  }
  .space {
    margin: auto 65px auto auto;
  }
}
@media only screen and (max-width: 1200px) {
  .nav-colm {
    margin-left: 65px;
  }
}
@media only screen and (max-width: 1025px) {
  .company-logo {
    margin-bottom: 30px;
  }
  .nav-colm {
    margin-left: 40px;
    text-align: center;
    margin-right: 40px;
    width:150px;
  }
  .footer-info {
    flex-direction: column;
  }
  .footer-links {
    flex-direction: column;
  }
  .footer-logos {
  margin-bottom: 30px;
  }
  .space {
    margin: auto 40px auto 40px;
  }
  .footer-txt{
    margin: auto 40px auto 40px;
    display:flex;
    width: 150px;
    text-align: center;
    justify-content: center;
  }
  .footer-list {
    flex-direction: column;
  }
}
@media only screen and (max-width: 768px) {
  .nav-colm {
    margin-left: 40px;
    text-align: center;
    margin-right: 40px;
    width:150px;
    margin-bottom: 40px;
  }
  .nav-sections {
    flex-direction: column;
  }
  .footer-info {
    padding-bottom: 0px;
  }
  .footer-links {
    margin-top: 0px;
  }
}
@media screen and (max-device-width: 800px) and (orientation: landscape) {
  .company-logo a img{
      //width: 30%;
      //height: auto;
  }
  .company-logo {
    display: flex;
    width: auto;
    transform: scale(0.75);
    height: 75px;
    align-items: center;
    //display: flex;
    //justify-content: center;
  }
}


</style>
<script setup>
</script>