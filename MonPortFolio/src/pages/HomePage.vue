<template>
  <div class="content">
    <div class="wrapper">
      <div class="image-container">
        <img
          class="image"
          src="https://res.cloudinary.com/dqf0ba8xy/image/upload/f_auto,q_auto/v1/imgPotfolio/pcep2xhny4r6ly2k7fu9"
          alt="Profile Picture"
        />
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
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
.content {
  background: url('https://utfs.io/f/YTngrWOozNXkdcPqTFsHzN4UP1kYrZLje5wVuJE2FCi7xpOf') !important;
  display: flex;
  justify-content: center;
  height: 100vh;
  flex: 1;
  text-align: left;
}

.wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 70%;
  gap: 2rem;
}

.text-box {
  width: auto;
  max-width: 60%;
  margin-right: 0;
}

.image-container {
  flex-shrink: 0;
  width: 40%;
  display: flex;
  justify-content: center;
}

.image {
  width: 80%;
  max-width: 300px;
  height: auto;
  border-radius: 50%;
  border: solid;
  border-color: #fe934b;
  object-fit: cover;
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
    height: 100vh;
    overflow: hidden;
    overflow-y: auto;
    max-width: 768px;
  }

  .wrapper {
    flex-direction: column;
    text-align: center;
    width: 100%;
  }

  .text-box {
    margin-left: 0;
    max-width: 90%;
  }

  .content h2 {
    font-size: 1.5rem;
  }

  .buttons {
    flex-direction: column;
    align-items: center;
  }

  .image-container {
    width: 70%;
  }
}
</style>
