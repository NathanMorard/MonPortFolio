<template>
  <div class="content">
    <div class="wrapper">
      <div class="text-box">
        <h1>Nathan Morard</h1>
        <h2>Développeur full-stack</h2>
        <div class="buttons">
          <RouterLink
            to="/contact"
            class="nav-item"
            :class="{ active: $route.path === '/contact' }"
            id="FirstBut"
          >
            Me contacter
          </RouterLink>

          <RouterLink
            to="/Resume"
            class="nav-item"
            :class="{ active: $route.path === '/Resume' }"
            id="SecondBut"
          >
            Mon cv
          </RouterLink>
        </div>
      </div>
      <div class="img">
        <img class="image" src="../assets/img/pp.jpg" alt="coucou" />
      </div>
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
.content {
  display: flex;
  justify-content: center;
  min-height: 100vh;
}

.wrapper {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 70%;
}

.text-box {
  flex: 1;
  padding-right: 20px;
}

.image {
  max-width: 320px;
  height: auto;
}

.img {
  flex-shrink: 0;
}

/* .homepage {
  position: relative;
  width: 100%;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 55px;
  padding-top: 25dvh;
} */

.content {
  flex: 1;
  text-align: left;
}

.content h1 {
  color: Black;
  font-size: 4rem;
  font-weight: bold;
  margin: 0;
}

.content h2 {
  margin: 0;
  padding-bottom: 2rem;
  font-size: 2rem;
  color: #1a2236;
}

.buttons {
  display: flex;
  gap: 1rem;
}


/* .img {
  height: 1dvh;
  width: 10dvh;
  margin-right: 100dvb;
} */
</style>
