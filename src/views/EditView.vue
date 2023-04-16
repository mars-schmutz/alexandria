<template>
    <template v-if="!asset">
        <p>Loading...</p>
    </template>
    <template v-else-if="asset.type == 'material'">
        <EditMaterial :asset="asset"/>
    </template>
    <template v-else-if="asset.type == 'render-settings'">
        <EditRender :asset="asset"/>
    </template>
    <template v-else>
        <p>Unrecognized: {{  asset.type }}</p>
    </template>
</template>

<script>
import EditMaterial from "../components/edit/EditMaterial.vue"
export default {
    name: "EditView",
    components: {
        EditMaterial
    },
    data() {
        return {
            id: this.$route.params.id,
            asset: null,
        }
    },
    created() {
        window.store.get("library-shelves").then((val) => {
            let i = val.findIndex(asset => asset.id == this.id)
            this.asset = val[i]
        })
    }
}
</script>