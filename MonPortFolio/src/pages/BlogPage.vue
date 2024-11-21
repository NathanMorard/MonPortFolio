<template>
  <div class="Content">
    <h1>Qui suis-je ?</h1>
    <div id="txtPres">
      <p>
        <strong>
          🎯 Développeur informatique | Passionné par la création d'applications
          et de solutions web innovantes
        </strong>
      </p>
      <p>
        Je suis Nathan Morard, développeur spécialisé dans la conception et le
        développement d'applications et de sites web. Diplômé d'un Bachelor
        Développeur et Concepteur d'Applications (2023-2024) après un BTS
        Développement Informatique, je suis désormais freelance.
      </p>
      <p>💻 Compétences techniques :</p>

      <p>
        &nbsp; &nbsp;- Langages et frameworks : JavaScript, TypeScript, Python,
        Vue.js, Flutter, Java (Spring), HTML, CSS, JSON, WinDev, WebDev
      </p>
      <p>&nbsp; &nbsp;- Bases de données : MySQL, MongoDB</p>
      <p>
        &nbsp; &nbsp;- Outils et gestion de projet : Hyper-V, gestion de projet
        Agile, Jira
      </p>
      <p>
        🌍 En quête de nouveaux défis : Je suis à la recherche de missions
        captivantes pour appliquer mes compétences, innover, et accompagner mes
        clients vers le succès.
      </p>
      <p>
        📩 Contactez moi pour discuter d'une collaboration :
        morard.nathan@gmail.com ou 0625836649
      </p>
    </div>
    <h2>Mon parcours</h2>
    <div class="timeline">
      <div class="container left">
        <img src="../assets/img/logoStJo.jpg" alt="Logo saint joseph" />
        <div class="content">
          <h2>Lycée saint Joseph</h2>
          <small>2020 - 2021</small>
          <p>
            Obtention d'un bac général spécialités SVT, mathématiques et
            physique-chimie au lycée saint joseph à Avignon.
          </p>
          <span class="left-container-arrow"></span>
        </div>
      </div>
      <div class="container right">
        <img src="../assets/img/logoCA.jpg" alt="logo Campus Academy" />
        <div class="content">
          <h2>Campus Academy</h2>
          <small>2021 - 2022</small>
          <p>
            Première année d'étude supérieure dans le domaine du développement
            informatique à l'école Campus Academy.
          </p>
          <span class="right-container-arrow"></span>
        </div>
      </div>
      <div class="container left">
        <img src="../assets/img/logoCESI.jpg" alt="Logo CESI" />
        <div class="content">
          <h2>CESI</h2>
          <small>2022 - 2023</small>
          <p>Obtention d'un BTS "Développeur informatique".</p>
          <span class="left-container-arrow"></span>
        </div>
      </div>
      <div class="container right">
        <img src="../assets/img/logoCESI.jpg" alt="Logo CESI" />
        <div class="content">
          <h2>CESI</h2>
          <small>2023 - 2024</small>
          <p>
            Obtention d'un bachelor "Concepteur et développeur d'application".
          </p>
          <span class="right-container-arrow"></span>
        </div>
      </div>
      <div class="container left">
        <!-- <img :src="logoDG" alt="Logo DG inventaires" /> -->
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
        <img src="../assets/img/freelance.jpg" alt="Logo freelance" />
        <div class="content">
          <h2>Freelance</h2>
          <small>2024 - </small>
          <p>Développeur informatique freelance.</p>
          <span class="right-container-arrow"></span>
        </div>
      </div>
    </div>
    <!-- <div class="Skills">
      <div class="wrapper">
        <div class="text-box">
          <h2>Mes competences</h2>
        </div>
        <div class="img">
          <img class="image" src="../assets/img/pp.jpg" alt="photo de profil" />
        </div>
      </div>
    </div> -->
  </div>
</template>

<script setup>
// import logoDG from '../assets/img/logodg.jpg'
</script>

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
  border: solid;
  border-width: thin;
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
  background-color: #fe934b;
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
  margin: 0;
  margin-bottom: 20px;
  font-weight: 600;
}

.content small {
  font-size: medium;
  display: inline-block;
  margin-bottom: 5px;
}

.content p {
  margin: 0;
  font-size: large;
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
