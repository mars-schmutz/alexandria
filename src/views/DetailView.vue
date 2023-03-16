<template>
    <div>
        <h1>Details</h1>
        <template v-if="asset">
            <p>{{ asset.name }}</p>
            <p>{{ asset.id }}</p>
        </template>
        <template v-else>
            <p>Loading...</p>
        </template>
    </div>
</template>

<script>
export default {
    name: "DetailView",
    data() {
        return {
            id: this.$route.params.id,
            asset: null
        }
    },
    created() {
        window.store.get("library-shelves").then((val) => {
            let i = val.findIndex(asset => asset.id == this.id)
            console.log(val[i])
            this.asset = val[i]
        })
    }
}
</script>