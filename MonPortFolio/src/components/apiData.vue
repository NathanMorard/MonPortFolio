<!-- src/components/ApiData.vue -->
<template>
  <div>
    <h1>Data from API</h1>
    <p>{{ apiMessage }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      apiMessage: '',
    };
  },
  mounted() {
    // Appel à l'API Flask
    axios.get('http://127.0.0.1:5000/api/data')
      .then(response => {
        this.apiMessage = response.data.message;
      })
      .catch(error => {
        console.error("Erreur lors de la récupération des données :", error);
      });
  },
};
</script>
