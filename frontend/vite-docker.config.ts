import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    // host: true,
    // strictPort: true,
    port: 5173,
    proxy: {
      '/task/': {
        target: 'http://backend:8000',
        changeOrigin: true,
      },
    },
  },
})
