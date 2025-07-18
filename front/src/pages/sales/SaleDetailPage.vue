<script setup lang="ts">
import { onMounted, ref, type Ref } from 'vue';
import SideBar from '../../components/SideBar.vue';
import { useRoute } from 'vue-router';

const route = useRoute()
const sales: Ref<Sale[]> = ref([])

interface Sale {
    created_at: string
    id: number
    total: number
    total_itens: number
}

interface DetailsResponse {
    msg: string
    list: Sale[]
}
onMounted(async () => {
    const saleId = route.params.id
    try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/sales/details/${saleId}`, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            }
        })
        const obj: DetailsResponse = await res.json()
        if (res.ok) {
            sales.value = obj.list
        }
        console.log(obj.msg)
    } catch (error) {
        console.log(error)
    }
})
</script>

<template>
    <SideBar />
    <div class="d-flex flex-column p-2 w-100 h-100 overflow-auto">
        <h4>Sale Details</h4>
        <table class="table table-sm">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Data</th>
                    <th scope="col">Total Itens</th>
                    <th scope="col">Total</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="sale, i in sales">
                    <th scope="row">{{ i + 1 }}</th>
                    <td>{{ new Date(sale.created_at).toLocaleDateString('pt-br') }}</td>
                    <td>{{ sale.total_itens }}</td>
                    <td>R$ {{ sale.total }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>