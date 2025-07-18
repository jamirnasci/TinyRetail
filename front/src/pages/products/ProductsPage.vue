<template>
    <SideBar/>
    <div class="form-container p-2">
        <h4>Cadastrar Produto</h4>
        <ProductForm/>
    </div>
</template>

<script setup lang="ts">
import ProductForm from '../../components/forms/ProductForm.vue';
import SideBar from '../..//components/SideBar.vue';

</script>