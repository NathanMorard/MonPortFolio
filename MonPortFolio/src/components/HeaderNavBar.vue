<template>
  <header class="header">
    <nav class="navbar">
      <!-- Bouton menu burger -->
      <button class="burger" @click="toggleMenu">☰</button>
      <!-- Menu principal -->
      <div :class="['nav-links', { open: isMenuOpen }]">
        <RouterLink
          to="/"
          class="nav-item"
          :class="{ active: $route.path === '/' }"
          @click="closeMenu"
        >
          Home
        </RouterLink>
        <RouterLink
          to="/blog"
          class="nav-item"
          :class="{ active: $route.path === '/blog' }"
          @click="closeMenu"
        >
          À propos de moi
        </RouterLink>
        <RouterLink
          to="/resume"
          class="nav-item"
          :class="{ active: $route.path === '/resume' }"
          @click="closeMenu"
        >
          Curriculum
        </RouterLink>
        <RouterLink
          to="/realisation"
          class="nav-item"
          :class="{ active: $route.path === '/realisation' }"
          @click="closeMenu"
        >
          Mes réalisations
        </RouterLink>
        <RouterLink
          to="/contact"
          class="nav-item"
          :class="{ active: $route.path === '/contact' }"
          @click="closeMenu"
        >
          Contact
        </RouterLink>
        <!-- <switchMode/> -->
      </div>
    </nav>
  </header>
</template>

<script setup>
import { ref } from 'vue'
// import switchMode from './switchMode.vue'

const isMenuOpen = ref(false)

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const closeMenu = () => {
  isMenuOpen.value = false
}
</script>

<style>
.header {
  display: flex;
  justify-content: center;
  background-color: #333;
}

.navbar {
  display: flex;
  align-items: center;
  width: 100%;
  position: relative;
}

.burger {
  display: none;
  font-size: 2rem;
  background: none;
  border: none;
  color: white;
  cursor: pointer;
  margin-left: 1rem;
}

.nav-links {
  display: flex;
  flex-grow: 1;
  /* justify-content: center; */
  transition: transform 0.3s;
}

.nav-links.open {
  transform: translateY(0);
}

.nav-item {
  padding: 1rem 2rem;
  color: white;
  text-decoration: none;
  background-color: #333;
  transition: background-color 0.3s;
}

.nav-item:hover {
  background-color: #555;
}

.active {
  background-color: #0066a5;
}

/* Responsive styles */
@media (max-width: 768px) {
  .burger {
    display: block;
  }

  .nav-links {
    display: flex;
    flex-direction: column;
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    background-color: #333;
    transform: translateY(-200%);
    z-index: 10;
  }

  .nav-links.open {
    transform: translateY(0);
  }

  .nav-item {
    padding: 1rem;
    text-align: center;
  }
}
</style>
