<template>
    <div class="title">
        <h1>Me contacter</h1>
    </div>
    <div class="form">
        <form @submit.prevent="submitForm">
            <label for="fname">Prénom</label><br>
            <input v-model="form.fname" type="text" id="fname" name="fname" required><br>
            <label for="lname">Nom</label><br>
            <input v-model="form.lname" type="text" id="lname" name="lname" required><br>
            <label for="subject">Objet</label><br>
            <input v-model="form.subject" type="text" id="subject" name="subject" required><br>
            <label for="email">Mail</label><br>
            <input v-model="form.email" type="email" id="email" name="email" required><br><br>
            <input type="submit" value="Envoyer">
        </form>
    </div>
</template>

<script setup>
import { reactive } from 'vue'

const form = reactive({
    fname: '',
    lname: '',
    subject: '',
    email: ''
})

function submitForm() {
    // Example payload creation, ready to be sent to an email API or backend
    const payload = {
        firstName: form.fname,
        lastName: form.lname,
        subject: form.subject,
        email: form.email
    }

    // Here you could use a POST request to send the payload to a backend or email API
    // Example: await fetch('https://your-backend.com/send-email', {
    //     method: 'POST',
    //     headers: { 'Content-Type': 'application/json' },
    //     body: JSON.stringify(payload)
    // });

    alert('Formulaire envoyé !')
}
</script>

<style scoped>
.title {
    text-align: center;
}
.form {
    max-width: 500px;
    margin: 0 auto;
}
</style>
