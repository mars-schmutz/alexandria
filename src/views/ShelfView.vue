<template>
    <p v-if="assets.length == 0">No assets in library</p>
    <div v-else>
        <Asset v-for="asset in assets" :key="asset.name" :name="asset.name" />
    </div>
</template>

<script>
import Asset from "../components/Asset.vue"

export default {
    name: "ShelfView",
    components: {
        Asset
    },
    data() {
        return {
            assets: window.store.get("library-shelves").then((val) => {
                val ? this.assets = val : this.assets = []
            })
        }
    },
    mounted() {
    }
}
</script>