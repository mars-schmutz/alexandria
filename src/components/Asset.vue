<template>
    <span class="delete" @click="$emit('delete')">&#10006;</span>
    <div @click="$emit('view')">
        <h1>{{ name }}</h1>
        <div class="thumbnail" :style="{ backgroundImage: `url('${thumbnail}')` }"></div>
    </div>
</template>

<script>
export default {
    name: "Asset",
    props: {
        name: String,
        thumbnail: String
    },
    mounted() {
        if (this.thumbnail == "") {
            this.thumbnail = "../assets/logo.svg"
        }
    }
}
</script>

<style scoped>
div {
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;
    width: 2rem;
    height: 2rem;
}
</style>