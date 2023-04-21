<template>
    <template v-if="!asset">
        <p>Loading...</p>
    </template>
    <template v-else-if="asset.type == 'material'">
        <EditMaterial :asset="asset"/>
    </template>
    <template v-else-if="asset.type == 'render-settings'">
        <EditRender
        :asset="asset"
        @update="updateAsset"
        />
    </template>
    <template v-else-if="asset.type == 'lights'">
        <EditLights
        :asset="asset"
        @update="updateAsset"
        />
    </template>
    <template v-else-if="asset.type == 'compositor'">
        <EditCompositor
        :asset="asset"
        @update="updateAsset"
        />
    </template>
    <template v-else-if="asset.type == 'proc-mat'">
        <EditProcMat
        :asset="asset"
        @update="updateAsset"
        />
    </template>
    <template v-else>
        <p>Unrecognized: {{  asset.type }}</p>
    </template>
</template>
<script>
import EditMaterial from "../components/edit/EditMaterial.vue"
import EditRender from "../components/edit/EditRender.vue"
import EditLights from "../components/edit/EditLights.vue"
import EditCompositor from "../components/edit/EditCompositor.vue"
import EditProcMat from "../components/edit/EditProcMat.vue"
export default {
    name: "EditView",
    components: {
        EditMaterial,
        EditRender,
        EditCompositor,
        EditLights,
        EditProcMat
    },
    data() {
        return {
            id: this.$route.params.id,
            asset: null,
        }
    },
    methods: {
        async updateAsset(updated) {
            let currLib = await window.store.get("library-shelves")
            let toUpdate = currLib.findIndex(asset => asset.id == this.id)
            currLib[toUpdate].name = updated.name
            currLib[toUpdate].settings = updated.settings
            try {
                await window.store.set("library-shelves", currLib)
                this.$router.push(`/details/${this.asset.id}`)
            } catch (err) {
                console.log(err)
            }
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