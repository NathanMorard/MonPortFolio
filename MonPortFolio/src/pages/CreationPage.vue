<template>
  <div class="creations">
    <h1>Mes Créations</h1>
    <p class="intro">Découvrez mes différents projets et réalisations</p>

    <div class="projects-grid">
      <projectCard
        v-for="project in projects"
        :key="project.title"
        :project="project"
      />
    </div>
  </div>
</template>

<script setup>
import projectCard from '@/components/projectsCard.vue'

const projects = [
  {
    title: 'Flower Power',
    description: "Exemple de création d'un site web vitrine pour un fleuriste",
    image:
      'https://res.cloudinary.com/dqf0ba8xy/image/upload/f_auto,q_auto/v1/imgPotfolio/phfr1rkxx8skrbapm5qo',
    liveUrl:
      'https://res.cloudinary.com/dqf0ba8xy/video/upload/f_auto:video,q_auto/v1/imgPotfolio/tdlgpymvbw7eoukymebx',
    technologies: ['Vue.js', 'Vite', 'TailwindCSS'],
    githubUrl: 'https://github.com/NathanMorard/fleuriste',
  },
  // Ajoutez d'autres projets ici
]
</script>

<style scoped>
.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1rem;
  margin-top: 2rem;
}

.creations {
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

h1 {
  text-align: center;
  color: #646cff;
  margin-bottom: 0.5rem;
}

.intro {
  text-align: center;
  color: #888;
  margin-bottom: 3rem;
}

@media (max-width: 768px) {
  .projects-grid {
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  }
}
</style>
