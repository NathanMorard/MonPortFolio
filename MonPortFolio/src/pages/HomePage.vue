<template>
  <div class="homepage">
    <div class="content">
      <h1>Nathan Morard</h1>
      <h2>Développeur full-stack</h2>
      <div class="buttons">
        <RouterLink
          to="/contact"
          class="nav-item"
          :class="{ active: $route.path === '/contact' }"
        >
          Me contacter
        </RouterLink>

        <RouterLink
          to="/Resume"
          class="nav-item"
          :class="{ active: $route.path === '/Resume' }"
        >
          Mon cv
        </RouterLink>
      </div>
    </div>
    <div class="img">
      <img src="../assets/img/pp.jpg" alt="coucou" />
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
body {
  margin: 0;
  font-family: 'Arial', sans-serif;
  background-color: #121212;
  color: white;
}

.homepage {
  position: relative;
  width: 100%;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: space-between;
  /* padding: 55px; */
  /* padding-top: 25dvh; */
}

.content {
  flex: 1;
  text-align: left;
}

.content h1 {
  font-size: 4rem;
  margin-bottom: 0.5rem;
  font-weight: bold;
}

.content h2 {
  font-size: 2rem;
  margin-bottom: 2rem;
  color: #aaaaaa;
}

.buttons {
  display: flex;
  gap: 1rem;
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

.img {
  height: 1dvh;
  width: 10dvh;
  margin-right: 100dvb;
}
</style>
