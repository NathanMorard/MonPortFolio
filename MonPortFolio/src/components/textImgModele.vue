<template>
  <div class="content">
    <div class="wrapper">
      <div class="text-box">
        <div class="text-h1" v-if="texth1">
          <h1>{{ texth1 }}</h1>
        </div>
        <div class="text-h2" v-if="texth2">
          <h2>{{ texth2 }}</h2>
        </div>
        <div class="text-p" v-if="textp">
          <p>{{ textp }}</p>
        </div>
      </div>
      <div class="img">
        <img :src="imageSrc" alt="Card Image" />
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  imageSrc: {
    type: String,
    required: true,
  },
  texth1: {
    type: String,
    required: false,
  },
  texth2: {
    type: String,
    required: false,
  },
  textp: {
    type: String,
    required: false,
  },
})
</script>

<style scoped>
.content {
  display: flex;
  padding: 20px;
}

.wrapper {
  display: flex;
  gap: 40px; /* Espacement entre l'image et le texte */
  width: 70%;
  max-width: 1200px;
}

.img {
  position: relative;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  max-width: 450px;
  overflow: hidden;
}

.img img {
  width: 100%;
  height: auto;
  object-fit: cover;
  margin-top: -20px;
}

.text-box {
  flex: 0 1 auto;
  max-width: 600px;
  min-width: 300px;
  padding: 0;
  padding-top: 20px;
  box-sizing: border-box;
  word-wrap: break-word;
}

h1 {
  font-size: 50px;
}

h2 {
  font-size: 40px;
}

p {
  font-size: 30px;
}

@media (max-width: 768px) {
  .wrapper {
    flex-direction: column;
    width: 90%;
    align-items: center;
  }

  .img {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    max-width: 320px;
  }

  .img img {
    margin: 0 auto;
  }

  .text-box {
    text-align: center;
  }
}
</style>
