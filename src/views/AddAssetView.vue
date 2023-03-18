<template>
    <h3>New Asset</h3>
    <form @submit.prevent>
        <label>Asset Name:</label>
        <input type="text" v-model="assetName" />
        <label>Asset Type:</label>
        <select v-model="assetType">
            <option disabled>Select asset type</option>
            <option value="material">Material</option>
            <option value="render-settings">Render Settings</option>
        </select>
        <template v-if="assetType == 'material'">
            <NewMaterial
            @asset_info="assetInfo = $event"
            />
        </template>
        <template v-if="assetType == 'render-settings'">
            <label>Render Settings JSON export:</label>
        </template>
        <button @click="onSubmit()">Save</button>
    </form>
</template>

<script>
// TODO: Emit asset info as single object from each asset component
// TODO: COPY assets to entry. DO NOT MOVE.
import NewMaterial from "../components/NewMaterial.vue"
export default {
    name: "AddAsset",
    components: {
        NewMaterial
    },
    data() {
        return {
            assetName: "",
            assetType: "",
            assetInfo: {},
            assetLocation: ""
        }
    },
    methods: {
        fileEntry() {
            let entry_path = this.assetName.split(" ").join("_")
            this.assetLocation = window.alexandria.createEntry(entry_path)
            for (let key in this.assetInfo) {
                let newurl = window.alexandria.copyFile(this.assetInfo[key])
                this.assetInfo[key] = newurl
            }
        },
        async onSubmit() {
            // this.fileEntry()

            const timestamp = Date.now().toString(36)
            const randNum = Math.random().toString(36)
            const newId = timestamp + randNum
            let currLib = await window.store.get("library-shelves") ? await window.store.get("library-shelves") : []
            let asset = {
                id: newId,
                name: this.assetName,
                type: this.assetType,
                path: this.assetLocation,
                assets: this.assetInfo
            }
            console.log(currLib)
            currLib.push(asset)
            window.store.set("library-shelves", currLib).then((val) => {
                console.log(JSON.stringify(this.assetInfo))
            })

            this.$router.push("/")
        }
    }
}
</script>