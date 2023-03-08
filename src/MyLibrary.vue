<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
    <header>
        <!-- <button class="btn btn-primary" @click="addAsset()">New +</button> -->
        <nav>
            <RouterLink to="/add" class="" id="addNew">New +</RouterLink>
            <RouterLink to="/">Shelves</RouterLink>
        </nav>
    </header>
    <RouterView />
</template>

<script>
export default {
    name: 'ShelfView',
    mounted() {
        window.alexandria.getSettingsPage((e, val) => {
            this.$router.push("/settings")
        })
    }
}
</script>