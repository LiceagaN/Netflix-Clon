<template>
    <v-container class="pa-4" max-width="600px">
      <v-card class="pa-4" elevation="3">
        <v-card-title class="text-h6">Guardar información del video</v-card-title>
  
        <v-form @submit.prevent="guardar" v-model="formValido">
          <v-text-field v-model="form.title" label="Título" required />
          <v-textarea v-model="form.description" label="Descripción" auto-grow rows="3" />
          <v-text-field v-model="form.category" label="Categoría" />
          <v-text-field v-model="form.url" label="URL del video (S3)" required />
          <v-text-field v-model="form.duration" label="Duración (formato hh:mm:ss)" required />
  
          <v-btn type="submit" color="primary" class="mt-4" :loading="cargando">
            Guardar Video
          </v-btn>
        </v-form>
  
        <v-alert v-if="mensaje" type="success" class="mt-4" dismissible>
          {{ mensaje }}
        </v-alert>
      </v-card>
    </v-container>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { getAuth } from 'firebase/auth'
  import axios from 'axios'
  import { API_BASE_URL } from '@/config/api' // ✅ Importamos la URL base
  
  const formValido = ref(false)
  const cargando = ref(false)
  const mensaje = ref('')
  const form = ref({
    title: '',
    description: '',
    category: '',
    url: '',
    duration: ''
  })
  
  const guardar = async () => {
    cargando.value = true
    mensaje.value = ''
    try {
      const token = await getAuth().currentUser.getIdToken()
      await axios.post(`${API_BASE_URL}/api/videos/`, form.value, {
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
      mensaje.value = '✅ Video guardado correctamente'
      form.value = {
        title: '',
        description: '',
        category: '',
        url: '',
        duration: ''
      }
    } catch (error) {
      mensaje.value = '❌ Error al guardar el video'
      console.error(error)
    } finally {
      cargando.value = false
    }
  }
  </script>
  