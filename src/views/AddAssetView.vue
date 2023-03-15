<template>
    <h3>New Asset</h3>
    <form>
        <label>Asset Name:</label>
        <input type="text" v-model="assetName" />
        <label>Asset Type:</label>
        <select v-model="assetType">
            <option disabled>Select asset type</option>
            <option value="material">Material</option>
            <option value="render-settings">Render Settings</option>
        </select>
    </form>
</template>

<script>
export default {
    name: "AddAsset",
    data() {
        return {
            name: ""
        }
    },
}
</script>