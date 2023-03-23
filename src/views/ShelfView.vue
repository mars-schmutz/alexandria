<template>
    <p v-if="assets.length == 0">No assets in library</p>
    <div v-else>
        <!-- :data-id? -->
        <Asset v-for="asset in assets"
        :key="asset.id" 
        :name="asset.name" 
        :thumbnail="asset.thumbnail"
        :data-id="asset.id" 
        @delete="deleteAsset(asset.id)"
        @view="view(asset.id)"/>
    </div>
</template>

<script>
import Asset from "../components/Asset.vue"
// necessary to convert reactive object to raw object
import { toRaw } from "vue"

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
    methods: {
        view(id) {
            this.$router.push(`/details/${id}`)
        },
        deleteAsset(id) {
            let asset = this.assets.find(asset => asset.id == id)
            let asset_entry = asset.path
            window.alexandria.deleteEntry(asset_entry).then(() => {
                console.log("File deleted")
                let i = this.assets.findIndex(asset => asset.id == id)
                this.assets.splice(i, 1)
                window.store.set("library-shelves", toRaw(this.assets)).then(() => {
                    console.log("Asset removed from library")
                }).catch((err) => {
                    console.log(err)
                })
            }).catch((err) => {
                console.log(err)
            })
        }
    }
}
</script>