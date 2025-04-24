<template>
    <div class="p-4 max-w-md mx-auto">
      <h2 class="text-xl font-bold mb-4">Obtener ID Token de Firebase</h2>
      <form @submit.prevent="login">
        <input v-model="email" placeholder="Correo" class="w-full mb-2 p-2 border rounded" />
        <input v-model="password" type="password" placeholder="Contraseña" class="w-full mb-2 p-2 border rounded" />
        <button type="submit" class="bg-blue-600 text-white px-4 py-2 rounded w-full">
          Iniciar sesión
        </button>
      </form>
      <div v-if="token" class="mt-4 p-2 bg-gray-100 rounded break-all">
        <strong>ID Token:</strong>
        <p>{{ token }}</p>
      </div>
      <div v-if="error" class="mt-4 text-red-600">
        {{ error }}
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { initializeApp } from 'firebase/app'
  import { getAuth, signInWithEmailAndPassword } from 'firebase/auth'
  
  // 🔐 Configuración Firebase
  const firebaseConfig = {
    apiKey: import.meta.env.VITE_FIREBASE_API_KEY,
    authDomain: import.meta.env.VITE_FIREBASE_AUTH_DOMAIN,
    projectId: import.meta.env.VITE_FIREBASE_PROJECT_ID,
  }
  
  const app = initializeApp(firebaseConfig)
  const auth = getAuth(app)
  
  const email = ref('')
  const password = ref('')
  const token = ref('')
  const error = ref('')
  
  const login = async () => {
    error.value = ''
    token.value = ''
    try {
      const userCred = await signInWithEmailAndPassword(auth, email.value, password.value)
      const idToken = await userCred.user.getIdToken()
      token.value = idToken
    } catch (err) {
      error.value = err.message
    }
  }
  </script>
  