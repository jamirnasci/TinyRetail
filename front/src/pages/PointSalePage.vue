<template>
    <SideBar />
    <div class="d-flex flex-column justify-content-between p-2 w-100 h-100">
        <div class="h-100">
            <h4>Nova Venda</h4>
            <div class="d-flex align-items-end">
                <div class="w-100">
                    <label for="">Produto</label><br>
                    <select v-model="selectedProduct" class="form-select" name="product" id="product">
                        <option v-for="p in products" :value="p.id">{{ p.name }}</option>
                    </select>
                </div>
                <div class="w-25">
                    <label for="">Qtde.</label>
                    <input v-model="quantity" class="form-control" type="number" name="quantity" id="quantity" step="1">
                </div>
                <div>
                    <button v-on:click="addProduct" class="btn btn-primary ms-1">Adicionar</button>
                </div>
            </div>
            <div class="d-flex" style="height: 80%;">
                <div class="overflow-auto w-75">
                    <table class="table table-sm">
                        <thead>
                            <tr>
                                <th scope="col">#</th>
                                <th scope="col">Nome</th>
                                <th scope="col">Preço</th>
                                <th scope="col">Quantidade</th>
                                <th scope="col">Total</th>
                                <th scope="col"></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="p, i in productsSaleList">
                                <th scope="row">{{ i + 1 }}</th>
                                <td>{{ p.name }}</td>
                                <td>R$ {{ p.price }}</td>
                                <td>{{ p.item_quantity }}</td>
                                <td>R$ {{ p.total }}</td>
                                <td><button v-on:click="removeItem(i)" class="btn btn-danger">X</button></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="w-25 d-flex flex-column justify-content-between align-items-end">
                    <div class="w-100">
                        <label class="text-primary">Total Pago</label>
                        <input v-on:input="sumSale()" v-model="paid" class="form-control" type="number"
                            name="total_pago" id="total_pago">
                    </div>

                    <div class="d-flex flex-column align-items-end w-100">
                        <h4 class="text-dark">Troco: R$ {{ change }}</h4>
                        <h4 class="text-danger">Falta: R$ {{ lack }}</h4>
                        <h4 class="text-success">Total: R$ {{ totalSale }}</h4>
                        <button v-on:click="clearList" class="btn btn-warning w-100">Limpar</button>
                        <button class="btn btn-danger w-100 mt-1">Cancelar</button>
                        <button v-on:click="submitSale" class="btn btn-success w-100 mt-1">Finalizar</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref, type Ref } from 'vue';
import SideBar from '../components/SideBar.vue';

interface Product {
    id: number
    name: string
    buy_price: number
    sell_price: number
    quantity: number
}

interface SaleListProduct {
    id: number
    name: string
    price: number
    item_quantity: number
    total: number
}

interface LoadProductsResponse {
    msg: string
    list: Product[]
}

const products: Ref<Product[]> = ref([])
const productsSaleList: Ref<SaleListProduct[]> = ref([])
const quantity: Ref<number> = ref(1)
const selectedProduct: Ref<number> = ref(-1)
const totalSale: Ref<number> = ref(0)
const change: Ref<number> = ref(0)
const lack: Ref<number> = ref(0)
const paid: Ref<number> = ref(0)

onMounted(async () => {
    try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/products/findall`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            }
        })
        if (res.ok) {
            const obj: LoadProductsResponse = await res.json()
            products.value = obj.list
        }
    } catch (error) {
        console.log(`Load products error ${error}`)
    }
})

const addProduct = () => {
    if (quantity.value <= 0) {
        alert('Insira uma quantidade válida de produtos')
        return
    }
    if (selectedProduct.value <= 0) {
        alert('Selecione um produto para inserir')
        return
    }

    const productFound: Product | undefined = products.value.find((item: Product) => item.id === selectedProduct.value)
    if (productFound) {
        if (productFound.quantity < quantity.value) {
            alert('Quantidade em estoque menor que a compra')
            return
        }
        const p: SaleListProduct = {
            id: productFound.id,
            name: productFound.name,
            price: productFound.sell_price,
            item_quantity: quantity.value,
            total: quantity.value * productFound.sell_price
        }
        productsSaleList.value.push(p)
    }
    sumSale()
}

const clearList = () => {
    productsSaleList.value = []
    sumSale()
}
const removeItem = (i: number) => {
    productsSaleList.value.splice(i, 1)
    sumSale()
}

const sumSale = () => {
    let total = 0
    productsSaleList.value.forEach((p: SaleListProduct) => {
        total += p.total
    })
    totalSale.value = total
    change.value = paid.value - total < 0 ? 0 : Math.abs(paid.value - total)
    lack.value = total - paid.value < 0 ? 0 : Math.abs(total - paid.value)
}

const submitSale = async ()=>{
    const list = productsSaleList.value.map((item)=>{
        return {
            id: item.id,
            total_item: item.item_quantity
        }
    })
    const sale = {
        total: totalSale.value,
        total_itens: productsSaleList.value.length,
        list: list
    }

    const res = await fetch(`${import.meta.env.VITE_API_URL}/sales/create`, {
        method: 'POST',
        headers:{
            'Authorization': `Bearer ${localStorage.getItem('token')}`,
            'Content-type': 'application/json'
        },
        body:JSON.stringify(sale)
    })

    const obj = await res.json()
    alert(obj.msg)
}
</script>
