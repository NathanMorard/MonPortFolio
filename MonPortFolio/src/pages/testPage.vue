<template>
  <div>
    <textImgModele
      class="text-img"
      :imageSrc="nuage"
      texth1="Texte h1"
      texth2="text h2"
      textp="texte p"
    />
  </div>
</template>

<script setup>
import textImgModele from '@/components/textImgModele.vue'
import nuage from '@/assets/img/nuage.jpg'
</script>

<style scoped>
.text-img {
  position: relative;
  align-items: center;
  justify-content: center;
}
</style>
