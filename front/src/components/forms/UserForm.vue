<template>
    <form v-on:submit="handleForm" action="" method="post">
        <div class="row">
            <div class="col text-start">
                <label class="text-start" for="name">Nome</label>
                <input class="form-control" v-model="form.name" type="text" name="name" id="name">
            </div>
        </div>
        <div class="row">
            <div class="col text-start">
                <label for="email">E-mail</label>
                <input class="form-control" v-model="form.email" type="email" name="email" id="email">
            </div>
            <div class="col text-start">
                <label for="email">Confirmar E-mail</label>
                <input v-model="emailConfirm" class="form-control" type="email">
            </div>
        </div>
        <div class="row">
            <div class="col text-start">
                <label class="" for="phone">Telefone</label>
                <input class="form-control" v-model="form.phone" type="tel" name="phone" id="phone">
            </div>
        </div>
        <div class="row">
            <div class="col text-start">
                <label for="password">Senha</label>
                <input class="form-control" v-model="form.password" type="password" name="password" id="password">
            </div>
            <div class="col text-start">
                <label for="password">Confirmar Senha</label>
                <input v-model="passwordConfirm" class="form-control" type="password">
            </div>
        </div>

        <input class="btn btn-primary bg-gradient mt-1" type="submit" value="Cadastrar">
        <input v-on:click="clearForm" class="btn btn-warning bg-gradient mt-1 ms-1" type="button" value="Limpar">
    </form>

</template>

<script setup lang="ts">
import { ref, type Ref } from 'vue'


interface User {
    name: string
    email: string
    phone: string
    password: string
}

const emailConfirm: Ref<string> = ref('')
const passwordConfirm: Ref<string> = ref('')

const form: Ref<User> = ref({
    name: '',
    email: '',
    phone: '',
    password: ''
})

interface CreateUserResponse {
    msg: string
}

const clearForm = () => {
    form.value = {
        name: '',
        email: '',
        phone: '',
        password: ''
    }
    emailConfirm.value = ''
    passwordConfirm.value = ''
}

const handleForm = async () => {
    if (emailConfirm.value != form.value.email || passwordConfirm.value != form.value.password) {
        alert('E-mail ou senha não são equivalentes')
        return
    }
    try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/users/create`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('token')}`,
                'Content-type': 'application/json'
            },
            body: JSON.stringify({
                name: form.value.name,
                email: form.value.email,
                phone: form.value.phone,
                password: form.value.password
            })
        })

        const obj: CreateUserResponse = await res.json()

        alert(obj.msg)
    } catch (error) {
        console.log(`User Form error: ${error}`)
    }
}

</script>