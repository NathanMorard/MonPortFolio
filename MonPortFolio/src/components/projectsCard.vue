<script setup>
defineProps({
  project: {
    type: Object,
    required: true,
  },
})
</script>

<template>
  <div class="project-card">
    <div class="project-image-container">
      <img :src="project.image" :alt="project.title" class="project-image" />
      <div class="project-overlay">
        <div class="project-links">
          <a
            v-if="project.liveUrl"
            :href="project.liveUrl"
            target="_blank"
            class="project-btn live-btn"
          >
            Voir le site
          </a>
          <a
            v-if="project.demoUrl"
            :href="project.demoUrl"
            target="_blank"
            class="project-btn demo-btn"
          >
            Voir la démo
          </a>
          <a
            v-if="project.githubUrl"
            :href="project.githubUrl"
            target="_blank"
            class="project-btn github-btn"
          >
            GitHub
          </a>
        </div>
      </div>
    </div>
    <div class="project-info">
      <h3 class="project-title">{{ project.title }}</h3>
      <p class="project-description">{{ project.description }}</p>
      <div class="project-tech-stack">
        <span v-for="tech in project.technologies" :key="tech" class="tech-tag">
          {{ tech }}
        </span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.project-card {
  background: #2c3e50;
  border-radius: 16px;
  overflow: hidden;
  transition: all 0.3s ease-in-out;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
  max-width: 400px;
  margin: 0 auto;
}

.project-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 25px rgba(0, 0, 0, 0.3);
}

.project-image-container {
  position: relative;
  height: 250px;
  overflow: hidden;
}

.project-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.project-card:hover .project-image {
  transform: scale(1.05);
}

.project-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.project-card:hover .project-overlay {
  opacity: 1;
}

.project-links {
  display: flex;
  gap: 15px;
}

.project-btn {
  padding: 10px 20px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;
}

.live-btn {
  background-color: #4caf50;
  color: white;
}

.demo-btn {
  background-color: #2196f3;
  color: white;
}

.github-btn {
  background-color: #333;
  color: white;
}

.project-btn:hover {
  transform: scale(1.05);
  opacity: 0.9;
}

.project-info {
  padding: 20px;
}

.project-title {
  color: #ffffff;
  margin-bottom: 10px;
  font-size: 1.3em;
}

.project-description {
  color: #b0b0b0;
  margin-bottom: 15px;
}

.project-tech-stack {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tech-tag {
  background-color: #2c2c2c;
  color: #7de38d;
  padding: 5px 10px;
  border-radius: 20px;
  font-size: 0.8em;
}
</style>
