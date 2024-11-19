<template>
  <footer class="footer">
    <nav class="navBar">
      <button class="navButton">
        <a
          href="https://www.linkedin.com/in/nathan-morard-708825222/"
          target="_blank"
          rel="noopener noreferrer"
          class="navLink"
        >
          <img
            src="../assets/img/LI-In-Bug.png"
            alt="LinkedIn Logo"
            class="icon"
          />
          LinkedIn
        </a>
      </button>

      <button class="navButton">
        <a
          href="https://github.com/NathanMorard"
          target="_blank"
          rel="noopener noreferrer"
          class="navLink"
        >
          <img
            src="../assets/img/github-mark.png"
            alt="GitHub Logo"
            class="icon"
          />
          GitHub
        </a>
      </button>
    </nav>
  </footer>
</template>

<style>
.footer {
  height: 10dvh;
  background-color: #333;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 1rem;
  position: sticky; /* Change from fixed to sticky */
  bottom: 0; /* Keep it at the bottom of the page */
  width: 100%;
  margin-top: 2rem; /* Optional, to give space above */
}

.navBar {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  width: 100%;
}

.navButton {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  font-size: 1rem;
  color: white;
  background-color: transparent;
  border: 1px solid white;
  border-radius: 5px;
  cursor: pointer;
  transition:
    background-color 0.3s,
    transform 0.2s;
}

.navButton:hover {
  background-color: #555;
  transform: scale(1.05);
}

.navLink {
  text-decoration: none;
  color: inherit; /* Hérite la couleur du bouton */
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.icon {
  width: 1.5rem;
  height: 1.5rem;
}

/* Responsive styles */
@media (max-width: 768px) {
  .navBar {
    flex-direction: column;
  }

  .navButton {
    width: 100%;
    justify-content: center;
  }
}
</style>
