<template>
  <form @submit.prevent="formHandler">
    <div class="mb-3">
      <label for="email" class="form-label">Email</label>
      <input v-model="email" type="email" id="email" class="form-control" required>
    </div>

    <div class="mb-3">
      <label for="senha" class="form-label">Senha</label>
      <input v-model="password" type="password" id="senha" class="form-control" required>
    </div>

    <div v-if="err" class="alert alert-danger py-2">
      {{ err }}
    </div>

    <button type="submit" class="btn btn-primary w-100">Entrar</button>
  </form>
</template>

<script setup lang="ts">
import { ref, type Ref } from 'vue';

interface LoginResponse {
  token?: string
  msg: string
}

const email: Ref<string> = ref('')
const password: Ref<string> = ref('')
const err: Ref<string> = ref('')

const formHandler = async () => {
  try {
    const res = await fetch(import.meta.env.BASE_URL, {
      method: 'post',
      headers: {
        'Content-type': 'application/json'
      },
      body: JSON.stringify({
        email: email.value,
        password: password.value
      })
    })
    const obj: LoginResponse = await res.json()

    if (!res.ok || !obj.token) {
      err.value = obj.msg || 'Erro inesperado'
      return
    }

    localStorage.setItem('token', obj.token)
    location.href = '/sales'
  } catch (error) {
    console.log(`Login Request error: ${error}`)
  }
}

</script>