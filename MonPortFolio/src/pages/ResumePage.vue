<template>
  <div class="cv-container">
    <h1>Mon CV</h1>
    <img src="../assets/img/CV.jpg" alt="CV Nathan Morard" class="cv-image" />
    <div class="buttons">
      <button id="FirstBut" @click="downloadCV">Télécharger fichier</button>
    </div>
  </div>
</template>

<script setup>
const downloadCV = () => {
  const link = document.createElement('a')
  link.href = '../../public/pdf/CV.pdf'
  link.download = 'cv_nathan_morard.pdf'
  link.click()
}
</script>

<style>
.cv-container {
  text-align: center;
  margin-top: 20px;
}

.cv-image {
  display: block;
  margin: 20px auto;
  max-width: 80%;
}

.buttons {
  margin-bottom: 1rem;
}
</style>
