import BlogPage from './pages/BlogPage.vue'
import ContactPage from './pages/ContactPage.vue'
import HomePage from './pages/HomePage.vue'
import ResumePage from './pages/ResumePage.vue'
import RealisationPage from './pages/RealisationPage.vue'

export const routes = [
  { path: '/', component: HomePage },
  { path: '/blog', component: BlogPage },
  { path: '/contact', component: ContactPage },
  { path: '/resume', component: ResumePage },
  { path: '/realisation', component: RealisationPage },
]
