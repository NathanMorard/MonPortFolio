<template>
  <div class="Content">
    <h1>Qui suis-je ?</h1>
    <p id="txtPres">
      Qui cum venisset ob haec festinatis itineribus Antiochiam, praestrictis
      palatii ianuis, contempto Caesare, quem videri decuerat, ad praetorium cum
      pompa sollemni perrexit morbosque diu causatus nec regiam introiit nec
      processit in publicum, sed abditus multa in eius moliebatur exitium addens
      quaedam relationibus supervacua, quas subinde dimittebat ad principem.
    </p>
    <h2>Mon parcours</h2>
    <div class="timeline">
      <div class="container left">
        <img src="../assets/img/logoStJo.png" alt="Amazon" />
        <div class="content">
          <h2>Lycée saint Joseph</h2>
          <small>2020 - 2021</small>
          <p>
            Obtention d'un bac général option SVT MATH et Physique chimie au
            lycée saint joseph à Avignon
          </p>
          <span class="left-container-arrow"></span>
        </div>
      </div>
      <div class="container right">
        <img src="../assets/img/logoCA.png" alt="tesla" />
        <div class="content">
          <h2>Campus Academy</h2>
          <small>2021 - 2022</small>
          <p>
            Première année d'étude supérieur dans le domaine du développement
            informatique à l'école Campus Academy qui a fermé ses portes
          </p>
          <span class="right-container-arrow"></span>
        </div>
      </div>
      <div class="container left">
        <img src="../assets/img/logoCESI.png" alt="Flipkart" />
        <div class="content">
          <h2>CESI</h2>
          <small>2022 - 2023</small>
          <p>Obtention d'un BTS 'Développeur informatique'</p>
          <span class="left-container-arrow"></span>
        </div>
      </div>
      <div class="container right">
        <img src="../assets/img/logoCESI.png" alt="Toyota" />
        <div class="content">
          <h2>CESI</h2>
          <small>2023 - 2024</small>
          <p>
            Obtention d'un bachelor 'Concepteur et développeur d'application'
          </p>
          <span class="right-container-arrow"></span>
        </div>
      </div>
      <div class="container left">
        <img src="../assets/img/logodg.png" alt="Flipkart" />
        <div class="content">
          <h2>DG Inventaires & Co</h2>
          <small>2022 - 2024</small>
          <p>
            Alternance effectuée au sein de l'entreprise DG Inventaires, au
            service informatique. Participation à la TMA (Tierce Maintenance
            Applicative) et au MCO (Maintien en Condition Opérationnelle) d'un
            ERP, développement d'un site web et création d'un spool.
          </p>
          <span class="left-container-arrow"></span>
        </div>
      </div>
      <div class="container right">
        <img src="../assets/img/freelance.png" alt="Toyota" />
        <div class="content">
          <h2>Freelance</h2>
          <small>2024 - </small>
          <p>Développeur informatique en freelance</p>
          <span class="right-container-arrow"></span>
        </div>
      </div>
    </div>
    <div class="Skills">
      <div class="wrapper">
        <img class="image" src="../assets/img/pp.png" alt="photo de profil" />
        <div class="text-box">
          <h2>Mes competences</h2>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
.Skills {
  display: flex;
  justify-content: center;
  min-height: 100vh;
  background: blue;
}

.wrapper {
  margin: 150px auto;
  width: 70%;
}

.image {
  float: left;
  max-width: 320px;
}

.text-box {
  color: black;
}

.text-box h2 {
  font-size: 42px;
}

.content {
  align-content: center;
}

.timeline {
  position: relative;
  max-width: 1200px;
  margin: 100px auto;
}

.container {
  padding: 10px 40px;
  position: relative;
  width: 50%;
  animation: movedawn 1s linear forwards;
  opacity: 0;
  box-sizing: border-box;
}

@keyframes movedawn {
  0% {
    opacity: 1;
    transform: translateY(-30px);
  }
  100% {
    opacity: 1;
    transform: translateY(0px);
  }
}

.container:nth-child(1) {
  animation-delay: 0s;
}
.container:nth-child(2) {
  animation-delay: 1s;
}

.container:nth-child(3) {
  animation-delay: 2s;
}
.container:nth-child(4) {
  animation-delay: 3s;
}
.container:nth-child(5) {
  animation-delay: 4s;
}
.container:nth-child(6) {
  animation-delay: 5s;
}
.container.left {
  left: 50%;
}

.container.right {
  right: 0;
}

.content {
  padding: 20px 30px;
  background-color: #d1cfcf;
  position: relative;
  border-radius: 6px;
  font-size: 15px;
}

.container img {
  position: absolute;
  width: 40px;
  border-radius: 50%;
  top: 32px;
  z-index: 10;
}

.container.right img {
  right: -20px;
}

.container.left img {
  left: -20px;
}

.timeline::after {
  content: '';
  position: absolute;
  width: 6px;
  height: 100%;
  background-color: #d1cfcf;
  top: 0;
  left: 50%;
  margin-left: -3px;
  z-index: -1;
  animation: moveline 6s linear forwards;
}
@keyframes moveline {
  0% {
    height: 0;
  }
  100% {
    height: 100%;
  }
}

.content h2 {
  font-weight: 600;
}

.content small {
  display: inline-block;
  margin-bottom: 15px;
}

.left-container-arrow {
  height: 0;
  width: 0;
  position: absolute;
  top: 28px;
  z-index: 1;
  border-top: 15px solid transparent;
  border-bottom: 15px solid transparent;
  border-right: 15px solid #fff;
  left: -15px;
}

.right-container-arrow {
  height: 0;
  width: 0;
  position: absolute;
  top: 28px;
  z-index: 1;
  border-top: 15px solid transparent;
  border-bottom: 15px solid transparent;
  border-left: 15px solid #fff;
  right: -15px;
}

h1,
h2 {
  font-size: 2.5rem;
  font-weight: bold;
  text-align: center;
  color: #333;
  margin-bottom: 20px;
  text-transform: uppercase;
  letter-spacing: 2px;
}

#txtPres {
  font-size: 1rem;
  line-height: 1.6;
  color: #555;
  text-align: justify;
  margin: 0 auto 20px auto;
  max-width: 800px;
  padding: 0 15px;
  font-family: 'Arial', sans-serif;
  background: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  padding: 15px;
}

@media screen and (max-width: 768px) {
  h1 {
    font-size: 2rem;
  }

  p {
    font-size: 0.95rem;
    padding: 0 10px;
  }

  content {
    padding: 10px;
  }
  .timeline {
    margin: 50px auto;
    size: calc(100% - 100px);
  }
  .timeline::after {
    right: 31px;
  }

  .container {
    width: calc(100% - 80px);
    padding-left: 80px;
    padding-right: 25px;
  }

  .text-box {
    font-size: 13px;
  }
  .text-box small {
    margin-bottom: 10px;
  }

  .container.right,
  .container.left {
    left: 0;
  }

  .container.left img,
  .container.right img {
    left: 10px;
  }

  .left-container-arrow,
  .right-container-arrow {
    border-right: 15px solid #fff;
    border-left: 0;
    left: -15px;
  }

  .timeline::after {
    left: 31px;
  }
}
</style>
