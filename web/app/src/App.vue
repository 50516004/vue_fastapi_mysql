<script setup>
import { ref } from 'vue';

// URL入力、応答、エラーを管理するリアクティブ変数
const url = ref('http://localhost:8000');
const response = ref(null);
const error = ref(null);

const fetchData = async () => {
  response.value = null; // 応答をリセット
  error.value = null; // エラーをリセット
  try {
    const res = await fetch(url.value);
    if (!res.ok) {
      throw new Error(`HTTP error! Status: ${res.status}`);
    }
    const data = await res.json(); // 応答をJSON形式で取得
    response.value = JSON.stringify(data, null, 2); // フォーマット済みのJSON
  } catch (err) {
    error.value = (err).message; // エラーメッセージを保存
  }
};
</script>

<template>
  <div class="url-fetcher">
    <form @submit.prevent="fetchData">
      <input type="text" v-model="url" placeholder="Enter URL" class="url-input" required />
      <button type="submit" class="fetch-button">Fetch</button>
    </form>
    <div v-if="response" class="response">
      <h3>Response:</h3>
      <pre>{{ response }}</pre>
    </div>
    <div v-if="error" class="error">
      <h3>Error:</h3>
      <p>{{ error }}</p>
    </div>
  </div>
</template>

<style scoped>
.url-fetcher {
  font-family: Arial, sans-serif;
  max-width: 600px;
  margin: 0 auto;
}

.url-input {
  width: 80%;
  padding: 8px;
  margin-right: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.fetch-button {
  padding: 8px 16px;
  border: none;
  background-color: #3498db;
  color: white;
  border-radius: 4px;
  cursor: pointer;
}

.fetch-button:hover {
  background-color: #2980b9;
}

.response,
.error {
  margin-top: 20px;
  padding: 10px;
  border-radius: 4px;
  white-space: pre-wrap;
}

.response {
  background-color: #f4f4f4;
  border: 1px solid #ddd;
}

.error {
  background-color: #ffe6e6;
  border: 1px solid #ffcccc;
  color: #cc0000;
}
</style>
