<template>
    <p v-if="assets.length == 0">No assets in library</p>
    <template v-else>
        <input type="text" v-model="search" placeholder="Search">
        <div class="shelf">
            <!-- :data-id? -->
            <Asset v-for="asset in filtered"
            :key="asset.id" 
            :name="asset.name" 
            :thumbnail="asset.thumbnail"
            :assetType="asset.type"
            :data-id="asset.id" 
            @delete="deleteAsset(asset.id)"
            @view="view(asset.id)"/>
        </div>
    </template>
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
            assets: "",
            search: ""
        }
    },
    methods: {
        view(id) {
            this.$router.push(`/details/${id}`)
        },
        deleteAsset(id) {
            if (confirm("Are you sure you want to delete this asset?") == false) {
                return
            }
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
    },
    computed: {
        filtered: function() {
            console.log(this.assets)
            return this.assets.filter((asset) => {
                return asset.name.toLowerCase().includes(this.search.toLowerCase())
            })
        }
    },
    created() {
        window.store.get("library-shelves").then((val) => {
            val ? this.assets = val : this.assets = []
        })
    }
}
</script>

<style scoped>
input[type="text"] {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 0.25rem;
    margin-bottom: 0.5rem;
    margin-top: 2rem;
}

.shelf {
    overflow: auto;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-content: flex-start;
}
</style>