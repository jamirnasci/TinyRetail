<template>
    <SideBar/>
    <h1>Sales</h1>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import SideBar from '../components/SideBar.vue';

interface Sale{
    total: number
}

interface SalesHistoryResponse{
    msg: string
    history?: Sale[]
}

onMounted(async () => {
    try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/sales/history`, {
            method: 'POST',
            headers:{
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            }
        })
        const obj: SalesHistoryResponse = await res.json()
        if(!res.ok){
            location.href = '/login'
        }
    } catch (error) {
        console.log(`Sales history error: ${error}`)
    }
})
</script>