<template>
    <v-container class="pa-4" max-width="600px">
      <v-card elevation="2" class="pa-4">
        <v-card-title class="text-h6">Subir video a S3</v-card-title>
  
        <v-file-input
          label="Selecciona un video"
          accept="video/mp4"
          v-model="archivo"
          prepend-icon="mdi-video"
          outlined
          dense
        />
  
        <v-btn
          :disabled="!archivo || cargando"
          color="primary"
          class="mt-4"
          @click="subirVideo"
          :loading="cargando"
        >
          Subir Video
        </v-btn>
  
        <v-progress-linear
          v-if="progreso > 0"
          class="mt-4"
          :model-value="progreso"
          color="deep-purple-accent-4"
          height="8"
          striped
          :indeterminate="cargando && progreso === 0"
        />
  
        <v-alert
          v-if="mensaje"
          type="success"
          class="mt-4"
          dismissible
        >
          {{ mensaje }}
        </v-alert>
      </v-card>
    </v-container>
</template>
  
<script setup>
import { ref } from 'vue'
import { obtainUploadUrl, uploadVideoToS3 } from '@/utils/s3'

// Aquí tu lógica reactiva
const archivo = ref(null)
const progreso = ref(0)
const cargando = ref(false)
const mensaje = ref('')

const subirVideo = async () => {
  mensaje.value = ''
  cargando.value = true
  progreso.value = 0

  try {
    if (!archivo.value) {
        mensaje.value = 'Selecciona un archivo antes de subir'
        return
    }

    const file_name = archivo.value.name
    console.log('📁 Archivo seleccionado:', file_name)
    const url = await obtainUploadUrl(file_name)

    await uploadVideoToS3(url, 
        archivo.value, 
        (p) => (
            progreso.value = p
        )
    )

    mensaje.value = '✅ Video subido con éxito'
  } catch (err) {
    mensaje.value = '❌ Error al subir el video'
    console.error(err)
  } finally {
    cargando.value = false
  }
}
</script>
