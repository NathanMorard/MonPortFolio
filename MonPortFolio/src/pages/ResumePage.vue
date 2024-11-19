<template>
  <div class="cv-container">
    <h1>Mon CV</h1>
    <img src="../assets/img/cv.png" alt="CV Nathan Morard" class="cv-image" />
    <div class="buttons">
      <button @click="downloadCV">Télécharger fichier</button>
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
  margin-bottom: 100px;
}
.buttons button {
  background-color: #1e1e1e;
  color: white;
  border: none;
  padding: 0.8rem 1.5rem;
  font-size: 1rem;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  opacity: 1;
}

.buttons button:hover {
  background-color: #333333;
}
</style>
