<template>
    <h3>New Asset</h3>
    <form @submit.prevent="onSubmit">
        <label>Asset Name:</label>
        <input type="text" v-model="assetName" />
        <label>Asset Type:</label>
        <select v-model="assetType">
            <option disabled>Select asset type</option>
            <option value="material">Material</option>
            <option value="render-settings">Render Settings</option>
        </select>
        <template v-if="assetType == 'material'">
            <label>Material Type:</label>
            <select v-model="materialType">
                <option disabled>Select material type</option>
                <option value="diffuse">Diffuse</option>
                <option value="normal">Normal</option>
                <option value="roughness">Roughness</option>
                <option value="metallic">Metallic</option>
                <option value="emissive">Emissive</option>
                <option value="ao">AO</option>
            </select>
        </template>
        <template v-if="assetType == 'render-settings'">
            <label>Render Settings JSON export:</label>
        </template>
        <button>Save</button>
    </form>
</template>

<script>
export default {
    name: "AddAsset",
    data() {
        return {
            assetName: "",
            assetType: ""
        }
    },
    methods: {
        async onSubmit() {
            const timestamp = Date.now().toString(36)
            const randNum = Math.random().toString(36)
            const newId = timestamp + randNum
            let currLib = await window.store.get("library-shelves") ? await window.store.get("library-shelves") : []
            const asset = {
                id: newId,
                name: this.assetName,
                type: this.assetType
            }
            console.log(currLib)
            currLib.push(asset)
            window.store.set("library-shelves", currLib).then((val) => {
                console.log("Saved asset to library")
            })

            this.assetName = ""
            this.assetType = ""
        }
    }
}
</script>