<template>
  <div class="content">
    <div class="wrapper">
      <div class="image-container">
        <img class="image" src="../assets/img/pp.jpg" alt="Profile Picture" />
      </div>
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
      <!-- <div class="img">
        <img class="image" src="../assets/img/pp.jpg" alt="coucou" />
      </div> -->
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
.content {
  background-image: url('../assets/img/backgroundHome.jpg');
  background-size: cover;
  background-position: center;
  display: flex;
  justify-content: center;
  min-height: 100vh;
  flex: 1;
  text-align: left;
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

.image-container {
  display: none;
}

.image {
  width: 100%;
  height: auto;
  border-radius: 50%;
  border: solid;
  border-color: #fe934b;
  object-fit: cover;
}

.img {
  flex-shrink: 0;
}

.content h1 {
  color: Black;
  font-size: 3rem;
  font-weight: bold;
  margin: 0;
}

.content h2 {
  margin: 0;
  padding-bottom: 1.5rem;
  font-size: 2rem;
  color: #1a2236;
}

.buttons {
  display: flex;
  gap: 1rem;
}

/* Mobile-specific styling */
@media (max-width: 768px) {
  .content {
    background-image: url('../assets/img/backgroundHomePhone.jpg');
    max-width: 768px;
  }

  .wrapper {
    flex-direction: column;
    text-align: center;
    width: 90%;
  }

  .text-box {
    padding-right: 0;
  }

  .content h1 {
    font-size: 3rem;
  }

  .content h2 {
    font-size: 1.5rem;
  }

  .buttons {
    flex-direction: column;
    align-items: center;
  }

  .image-container {
    display: block;
    margin-top: 2rem;
    margin-bottom: 2rem;
  }
}
</style>
