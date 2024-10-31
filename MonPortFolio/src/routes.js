import BlogPage from "./pages/BlogPage.vue";
import ContactPage from "./pages/contactPage.vue";
import HomePage from "./pages/HomePage.vue";

export const routes = [
    {path: '/', component: HomePage},
    {path: '/blog', component: BlogPage},
    {path: '/contact', component: ContactPage},
]