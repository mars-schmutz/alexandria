<template>
    <div>
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