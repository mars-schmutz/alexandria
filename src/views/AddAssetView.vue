<template>
    <h3>New Asset</h3>
    <label>Asset Type:</label>
    <select v-model="assetType">
        <option disabled>Select asset type</option>
        <option value="material">Material</option>
        <option value="render-settings">Render Settings</option>
    </select>
    <template v-if="assetType == 'material'">
        <NewMaterial
        :type="assetType"
        />
    </template>
    <template v-if="assetType == 'render-settings'">
        <label>Render Settings JSON export:</label>
    </template>
</template>

<script>
import NewMaterial from "../components/NewMaterial.vue"
export default {
    name: "AddAsset",
    components: {
        NewMaterial
    },
    data() {
        return {
            assetType: "",
        }
    },
}
</script>