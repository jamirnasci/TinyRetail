<template>
    <SideBar/>
    <div class="form-container p-2">
        <h4>Cadastrar usuário</h4>
        <UserForm/>
    </div>
</template>

<script setup lang="ts">
import UserForm from '../components/forms/UserForm.vue';
import SideBar from '../components/SideBar.vue';
</script>