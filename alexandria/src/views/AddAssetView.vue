<template>
    <template v-if="location === ''">
        <p>Please set a library location before creating assets</p>
    </template>
    <template v-else>
        <h3>New Asset</h3>
        <label>Asset Type:</label>
        <select class="add-type" v-model="assetType">
            <option disabled>Select asset type</option>
            <option value="material">Material</option>
            <option value="render">Render Settings</option>
            <option value="proc_mat">Procedural Material</option>
            <option value="compositor">Compositor Settings</option>
            <option value="lights">Light Rig</option>
        </select>
        <template v-if="assetType == 'material'">
            <NewMaterial
            :type="assetType"
            />
        </template>
        <template v-if="assetType == 'render'">
            <NewRender
            :type="assetType"
            @save="saveAsset"
            />
        </template>
        <template v-if="assetType == 'proc_mat'">
            <NewProcMat
            :type="assetType"
            @save="saveAsset"
            />
        </template>
        <template v-if="assetType == 'compositor'">
            <NewCompositor
            :type="assetType"
            @save="saveAsset"
            />
        </template>
        <template v-if="assetType == 'lights'">
            <NewLights
            :type="assetType"
            @save="saveAsset"
            />
        </template>
    </template>
</template>

<script>
import NewMaterial from "../components/NewMaterial.vue"
import NewRender from "../components/NewRender.vue"
import NewProcMat from "../components/NewProcMat.vue"
import NewCompositor from "../components/NewCompositor.vue"
import NewLights from "../components/NewLights.vue"
export default {
    name: "AddAsset",
    components: {
        NewMaterial,
        NewRender,
        NewProcMat,
        NewCompositor,
        NewLights
    },
    data() {
        return {
            assetType: "",
            location: window.store.get("library-location").then((val) => {
                val ? this.location = val : this.location = ""
            })
        }
    },
    methods: {
        async saveAsset(value) {
            let currLib = await window.store.get("library-shelves") ? await window.store.get("library-shelves") : []
            currLib.push(value)
            await window.store.set("library-shelves", currLib)
            this.$router.push("/")
        }
    }
}
</script>