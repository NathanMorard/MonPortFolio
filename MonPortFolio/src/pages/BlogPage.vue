<template>
  <div class="Content">
    <h1>Qui suis-je ?</h1>
    <div id="txtPres">
      <p>
        <strong>
          👨🏻‍💻 Développeur informatique | Passionné par la création d'applications
          et de solutions web innovantes
        </strong>
      </p>
      <p>
        Je m'appelle Nathan Morard, développeur spécialisé dans la conception et
        le développement d'applications et de sites web. Diplômé d'un Bachelor
        Développeur et Concepteur d'Applications (2023-2024) après un BTS
        Développement Informatique, je suis désormais freelance.
      </p>
      <p>🤖 Compétences techniques :</p>

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
        🚀 En quête de nouveaux défis : Je suis à la recherche de missions
        captivantes pour appliquer mes compétences, innover, et accompagner mes
        clients vers le succès.
      </p>
      <p>
        📩 Contactez moi pour discuter d'une collaboration :
        morard.nathan@gmail.com ou 0625836649
      </p>
    </div>
    <h2>Mon parcours</h2>
    <timelineComponent />
    <div class="text-img">
      <textImgModele
        class="text-img"
        imageSrc="https://res.cloudinary.com/dqf0ba8xy/image/upload/f_auto,q_auto/v1/imgPotfolio/rm7lbqtgc8f5sqxnz39o"
        texth1="Mes compétences"
      />
    </div>
  </div>
</template>

<script setup>
import textImgModele from '@/components/textImgModele.vue'
import timelineComponent from '@/components/timelineComponent.vue'
</script>

<style scoped>
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

.text-img {
  background-color: white;
  position: relative;
  align-items: center;
  justify-content: center;
}

@media screen and (max-width: 768px) {
  h1 {
    font-size: 2rem;
  }

  p {
    font-size: 0.95rem;
    padding: 0 10px;
  }
}
</style>
