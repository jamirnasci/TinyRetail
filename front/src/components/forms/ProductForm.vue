<template>
    <form v-on:submit="formHandler" action="" method="post">
        <div class="row">
            <div class="col">
                <label for="name">Name</label>
                <input class="form-control" v-model="form.name" type="text" name="name" id="name">
            </div>
        </div>
        <div class="row">
            <div class="col">
                <label for="buy_price">Preço de compra</label>
                <input class="form-control" v-model="form.buy_price" type="number" name="buy_price" id="buy_price">
            </div>
            <div class="col">
                <label for="sell_price">Preço de venda</label>
                <input class="form-control" v-model="form.sell_price" type="number" name="sell_price" id="sell_price">
            </div>
        </div>
        <div class="row">
            <div class="col">
                <label for="quantity">Quantidade</label>
                <input class="form-control" v-model="form.quantity" type="number" name="quantity" id="quantity">
            </div>
        </div>
        <div class="row">
            <div class="col">
                <label for="supplier">Fornecedor</label>
                <select class="form-select" v-model="form.supplier" name="supplier" id="supplier">
                    <option v-for="s in suppliers" :value="s.id">{{ s.name }}</option>
                </select>
            </div>
        </div>
        <input type="submit" class="btn btn-primary bg-gradient mt-1" value="Cadastrar">
    </form>
</template>

<script setup lang="ts">
import { onMounted, ref, type Ref } from 'vue'


interface Product {
    name: string
    buy_price: number
    sell_price: number
    quantity: number
    supplier: number
}

interface Supplier {
    id: number
    name: string
}

interface SupplierResponse {
    msg: string
    suppliers: Supplier[]
}

const suppliers: Ref<Supplier[]> = ref([])

const form: Ref<Product> = ref({
    name: '',
    buy_price: 0,
    sell_price: 0,
    quantity: 0,
    supplier: -1
})

onMounted(async () => {
    try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/supplier/findall`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            }
        })
        const obj: SupplierResponse = await res.json()
        suppliers.value = obj.suppliers
    } catch (error) {
        console.log(`/supplier/findall error ${error}`)
    }
})

const formHandler = async () => {
    try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/products/create`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('token')}`,
                'Content-type': 'application/json'
            },
            body: JSON.stringify({
                name: form.value.name,
                buy_price: form.value.buy_price,
                sell_price: form.value.sell_price,
                quantity: form.value.quantity,
                supplier: form.value.supplier
            })
        })
        const obj = await res.json()
        alert(obj.msg)
    } catch (error) {
        console.log(`/products/create error ${error}`)
    }
}
</script>