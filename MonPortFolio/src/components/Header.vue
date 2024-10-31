<template>
    <header class="header">
        <nav class="navbar">
            <RouterLink to="/" class="nav-item active">Home</RouterLink>
            <RouterLink to="/blog" class="nav-item">Blog</RouterLink>
            <RouterLink to="/contact" class="nav-item">Contact</RouterLink>
        </nav>
    </header>
</template>

<script setup>

</script>

<style>
.header {
    display: flex;
    justify-content: center;
    background-color: #333;
}

.navbar {
    display: flex;
    width: 100%;
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
    background-color: #00a574; /* Couleur verte pour l'élément actif */
}
</style>
