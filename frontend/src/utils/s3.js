import axios from 'axios'
import { getAuth } from 'firebase/auth'
import { API_BASE_URL } from '@/config/api'
/**
 * Solicita al backend un URL firmado para subir un archivo a S3
 * @param {string} file_name - nombre del archivo a subir
 * @returns {string} - URL firmado de S3
 */
export const obtainUploadUrl = async (file_name) => {
  const user = getAuth().currentUser
  const token = await user.getIdToken()

  const response = await axios.post(
    `${API_BASE_URL}/api/upload-url/`,  // Asegúrate del slash final
    { file_name },
    {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`,
      }
    }
  )

  return response.data.upload_url
}

/**
 * Sube el archivo a S3 usando el URL firmado
 * @param {string} uploadUrl - URL firmado proporcionado por el backend
 * @param {File} file - archivo de tipo File a subir
 * @param {(progress: number) => void} onProgress - callback opcional para progreso
 */
export const uploadVideoToS3 = async (uploadUrl, file, onProgress) => {
  await axios.put(uploadUrl, file, {
    headers: {
      'Content-Type': file.type || 'video/mp4',
    },
    onUploadProgress: (e) => {
      if (onProgress) {
        const progress = Math.round((e.loaded * 100) / e.total)
        onProgress(progress)
      }
    }
  })
}
