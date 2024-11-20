<template>
  <div class="form-container">
    <div class="form-card">
      <h2>Me contacter</h2>

      <form @submit.prevent="handleSubmit">
        <div class="form-group" :class="{ error: errors.from }">
          <label for="from">De :</label>
          <input
            type="email"
            id="from"
            v-model="formData.from"
            :class="{ 'input-error': errors.from }"
            @input="validateField('from')"
            placeholder="votre@email.com"
          />
          <span class="error-message" v-if="errors.from">{{
            errors.from
          }}</span>
        </div>

        <div class="form-group" :class="{ error: errors.subject }">
          <label for="subject">Sujet :</label>
          <input
            type="text"
            id="subject"
            v-model="formData.subject"
            :class="{ 'input-error': errors.subject }"
            @input="validateField('subject')"
            placeholder="Sujet de l'email"
          />
          <span class="error-message" v-if="errors.subject">{{
            errors.subject
          }}</span>
        </div>

        <div class="form-group" :class="{ error: errors.message }">
          <label for="message">Message :</label>
          <textarea
            id="message"
            v-model="formData.message"
            :class="{ 'input-error': errors.message }"
            @input="validateField('message')"
            rows="6"
            placeholder="Votre message ici"
          ></textarea>
          <span class="error-message" v-if="errors.message">{{
            errors.message
          }}</span>
        </div>

        <div class="form-actions">
          <button type="submit" :disabled="isLoading || !isFormValid">
            <span v-if="isLoading" class="loader"></span>
            <span v-else>Envoyer</span>
          </button>
        </div>

        <div v-if="submitStatus" :class="['status-message', submitStatus.type]">
          {{ submitStatus.message }}
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'
import emailjs from 'emailjs-com'

const formData = reactive({
  from: '',
  subject: '',
  message: '',
})

const errors = reactive({
  from: '',
  subject: '',
  message: '',
})

const isLoading = ref(false)
const submitStatus = ref(null)

const validateField = field => {
  errors[field] = ''

  switch (field) {
    case 'from':
      if (!formData[field]) {
        errors[field] = 'Ce champ est requis'
      } else if (!validateEmail(formData[field])) {
        errors[field] = 'Email invalide'
      }
      break
    case 'subject':
      if (!formData[field]) {
        errors[field] = 'Le sujet est requis'
      } else if (formData[field].length < 3) {
        errors[field] = 'Le sujet doit contenir au moins 3 caractères'
      }
      break
    case 'message':
      if (!formData[field]) {
        errors[field] = 'Le message est requis'
      } else if (formData[field].length < 10) {
        errors[field] = 'Le message doit contenir au moins 10 caractères'
      }
      break
  }
}

const validateEmail = email => {
  const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/
  return regex.test(email)
}

const validateForm = () => {
  validateField('from')
  validateField('subject')
  validateField('message')
}

const isFormValid = computed(() => {
  return (
    formData.from &&
    formData.subject &&
    formData.message &&
    !errors.from &&
    !errors.subject &&
    !errors.message
  )
})

const handleSubmit = async () => {
  validateForm()

  if (!isFormValid.value) return

  isLoading.value = true
  submitStatus.value = null

  try {
    const templateParams = {
      from: formData.from,
      message: formData.message,
      Subject: formData.subject,
    }

    await emailjs
      .send(
        'service_x7gbtpw',
        'template_zu7zli8',
        templateParams,
        'XsRO5lgvmT00IdL1u',
      )
      .then(
        response => {
          console.log('Email envoyé', response)
          submitStatus.value = {
            type: 'success',
            message: 'Email envoyé avec succès',
          }
        },
        error => {
          console.log("Erreur d'envoi d'email", error)
          submitStatus.value = {
            type: 'error',
            message: "Erreur lors de l'envoi de l'email",
          }
        },
      )
  } catch (error) {
    submitStatus.value = {
      type: 'error',
      message: "Erreur lors de l'envoi. Veuillez réessayer.",
    }
    console.error('Erreur:', error)
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped>
.form-container {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f5f5f5;
  padding: 20px;
}

.form-card {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 500px;
}

h2 {
  color: #333;
  margin-bottom: 1.5rem;
  text-align: center;
  font-size: 1.5rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: #555;
  font-weight: 500;
}

input,
textarea {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #e1e1e1;
  border-radius: 6px;
  font-size: 1rem;
  transition:
    border-color 0.3s,
    box-shadow 0.3s;
}

input:focus,
textarea:focus {
  outline: none;
  border-color: #4caf50;
  box-shadow: 0 0 0 3px rgba(76, 175, 80, 0.1);
}

.input-error {
  border-color: #dc3545;
}

.error-message {
  color: #dc3545;
  font-size: 0.875rem;
  margin-top: 0.25rem;
}

button {
  width: 100%;
  padding: 0.75rem;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #45a049;
}

button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.loader {
  display: inline-block;
  width: 20px;
  height: 20px;
  border: 3px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  border-top-color: white;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.status-message {
  margin-top: 1rem;
  padding: 0.75rem;
  border-radius: 6px;
  text-align: center;
}

.success {
  background-color: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.error {
  background-color: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}

@media (max-width: 768px) {
  .form-card {
    padding: 1.5rem;
  }
}
</style>
