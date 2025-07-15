<template>
    <form v-on:submit="handleForm" method="post">
        <div class="row">
            <div class="col text-start">
                <label class="text-start" for="name">Nome</label>
                <input class="form-control" v-model="form.name" type="text" name="name" id="name" required>
            </div>
        </div>
        <div class="row">
            <div class="col text-start">
                <label for="email">E-mail</label>
                <input class="form-control" v-model="form.email" type="email" name="email" id="email" required>
            </div>
            <div class="col text-start">
                <label class="" for="phone">Telefone</label>
                <input class="form-control" v-model="form.phone" type="tel" name="phone" id="phone" required>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <label for="address">Endereço</label>
                <input v-model="form.address" class="form-control" type="text" name="address" id="address">
            </div>
        </div>
        <input class="btn btn-primary bg-gradient mt-1" type="submit" value="Cadastrar">
        <input v-on:click="clearForm" class="btn btn-warning bg-gradient mt-1 ms-1" type="button" value="Limpar" required>
    </form>

</template>

<script setup lang="ts">
import { ref, type Ref } from 'vue'


interface User {
    name: string
    email: string
    phone: string
    address: string
}

const form: Ref<User> = ref({
    name: '',
    email: '',
    phone: '',
    address: ''
})

interface CreateSupplierResponse {
    msg: string
}

const clearForm = () => {
    form.value = {
        name: '',
        email: '',
        phone: '',
        address: ''
    }
}

const handleForm = async () => {

    try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/supplier/create`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('token')}`,
                'Content-type': 'application/json'
            },
            body: JSON.stringify({
                name: form.value.name,
                email: form.value.email,
                phone: form.value.phone,
                address: form.value.address
            })
        })

        const obj: CreateSupplierResponse = await res.json()

        alert(obj.msg)
    } catch (error) {
        console.log(`User Form error: ${error}`)
    }
}

</script>