import BlogPage from './pages/BlogPage.vue'
import ContactPage from './pages/ContactPage.vue'
import HomePage from './pages/HomePage.vue'
import ResumePage from './pages/ResumePage.vue'
import CreationPage from './pages/CreationPage.vue'
// import TestPage from './pages/testPage.vue'

export const routes = [
  { path: '/', component: HomePage },
  { path: '/blog', component: BlogPage },
  { path: '/contact', component: ContactPage },
  { path: '/resume', component: ResumePage },
  { path: '/realisation', component: CreationPage },

  // { path: '/test', component: TestPage },
]
