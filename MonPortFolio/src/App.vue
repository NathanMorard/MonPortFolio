<template>
  <Header />
  <div class="container">
    <RouterView />
  </div>
</template>

<script setup>
import Header from './components/Header.vue';
</script>

<style>
/* Container styling for main content */
.container {
  padding-top: 2rem;
  max-width: calc(100vw - 4rem);
}
</style>
