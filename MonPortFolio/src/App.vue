<template>
  <Header />
  <div class="container">
    <RouterView />
  </div>
  <Footer />
</template>

<script setup>
import Header from './components/HeaderNavBar.vue'
import Footer from './components/FooterNavBar.vue'
</script>

<style>
/* .container {
  max-width: calc(100vw - 4rem);
} */

body {
  margin: 0;
  background: #2e364a;
}
</style>
