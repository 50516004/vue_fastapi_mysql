import { fileURLToPath, URL } from 'node:url'

import vue from '@vitejs/plugin-vue'
import { defineConfig } from 'vite'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  server: {
    host: '0.0.0.0', // 外部アクセスを許可
    port: 3000,       // 開発サーバのポート
    hmr: {
      port: 3001, // HMR用のポートを明示的に指定
    },
    watch: {
      usePolling: true, // ファイル変更検知にポーリングを使用
    },
  },
})
