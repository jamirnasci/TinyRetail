<template>
    <SideBar />
    <div class="w-100 d-flex flex-column">
        <h4>Sales</h4>
        <table class="table table-sm">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Quantidade</th>
                    <th scope="col">Total Venda</th>
                    <th scope="col">Data</th>
                    <th scope="col">Ação</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="s, i in sales">
                    <th scope="row">{{ i + 1 }}</th>
                    <td>{{ s.total_itens }}</td>
                    <td>R$ {{ s.total }}</td>
                    <td>{{ new Date(s.created_at).toLocaleDateString('pt-br') }}</td>
                    <td><button @click="navigateToDetails(s.id)" class="btn btn-secondary">Abrir</button></td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import SideBar from '../../components/SideBar.vue';
import type { Ref } from 'vue';
import { useRouter } from 'vue-router';

interface Sale {
    id: number
    total: number
    total_itens: number
    created_at: string
}

interface SalesHistoryResponse {
    msg: string
    history?: Sale[]
}

const sales: Ref<Sale[]> = ref([])
const router = useRouter()

onMounted(async () => {
    try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/sales/history`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            }
        })
        const obj: SalesHistoryResponse = await res.json()
        
        if (res.ok && obj.history) {
            sales.value = obj.history
        }
    } catch (error) {
        console.log(`Sales history error: ${error}`)
    }
})

const navigateToDetails = (id: number)=>{
    
    router.push({
        name: 'saleDetails',
        params:{
            id: id
        }
    })
}
</script>