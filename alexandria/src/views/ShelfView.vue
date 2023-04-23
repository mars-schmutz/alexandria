<template>
    <p v-if="assets.length == 0">No assets in library</p>
    <template v-else>
        <div class="sort">
            <select v-model="viewType">
                <option value="all">All</option>
                <option value="material">Materials</option>
                <option value="render">Render Settings</option>
                <option value="compositor">Compositor Settings</option>
                <option value="lights">Lights</option>
            </select>
            <input type="text" v-model="search" placeholder="Search">
        </div>
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
            search: "",
            viewType: "all"
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
            if (this.viewType != "all") {
                return this.assets.filter((asset) => {
                    return asset.type == this.viewType && asset.name.toLowerCase().includes(this.search.toLowerCase())
                })
            } else if (this.viewType == "material" || this.viewType == "proc_mat") {
                return this.assets.filter((asset) => {
                    return asset.type == "material" || asset.type == "proc_mat" && asset.name.toLowerCase().includes(this.search.toLowerCase())
                })
            } else {
                return this.assets.filter((asset) => {
                    return asset.name.toLowerCase().includes(this.search.toLowerCase())
                })
            }
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
.sort {
    display: flex;
    margin-top: 1rem;
    padding: 1rem;
}

.shelf {
    overflow: auto;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-content: flex-start;
    padding: 1rem;
}
</style>