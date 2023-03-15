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
            let currLib = await window.store.get("library-shelves") ? await window.store.get("library-shelves") : []
            const asset = {
                name: this.assetName,
                type: this.assetType
            }
            console.log(currLib)
            currLib.push(asset)
            window.store.set("library-shelves", currLib).then((val) => {
                console.log("Saved asset to library")
            })
        }
    }
}
</script>