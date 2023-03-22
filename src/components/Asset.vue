<template>
    <span class="delete" @click="$emit('delete')">&#10006;</span>
    <div @click="$emit('view')">
        <h1>{{ name }}</h1>
    </div>
</template>

<script>
export default {
    name: "Asset",
    props: {
        name: String,
    }
}
</script>