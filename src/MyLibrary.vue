<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
    <header>
        <button class="btn btn-primary">New +</button>
        <nav>
            <RouterLink to="/">Shelves</RouterLink>
        </nav>
    </header>
    <RouterView />
</template>