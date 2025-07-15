<template>
    <nav class="fixed-top bg-primary d-flex align-items-center justify-content-left p-2">
        <h5 class="text-white m-0">Tiny Retail</h5>
    </nav>
    <div class="card p-2">
        <LoginForm/>
    </div>
</template>

<script setup lang="ts">
import LoginForm from '../components/forms/LoginForm.vue';
</script>