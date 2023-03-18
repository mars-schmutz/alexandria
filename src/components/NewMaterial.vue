<template>
    <div>
        <label>Tags:</label>
        <input type="text" v-model="asset_tags" />
    </div>
    <div>
        <label>Workflow</label>
        <select v-model="mat_workflow">
            <option disabled>Choose a workflow</option>
            <option value="metallic">Metallic</option>
            <option value="specular">Specular</option>
        </select>
    </div>
    <div>
        <label>Texture Maps:</label>
        <label>Diffuse</label>
        <button @click="getPath('diffuse')">Diffuse</button>
        <p>{{ asset_info.diffuse }}</p>
    </div>
</template>

<script>
export default {
    name: "NewMaterial",
    emits: ["asset_info"],
    data() {
        return {
            asset_info: {},
            asset_tags: "",
            mat_workflow: "",
        }
    },
    methods: {
        async getPath(mat_map) {
            const path = await window.alexandria.openFile()
            this.asset_info[mat_map] = path
            this.$emit("asset_info", this.asset_info)
        }
    }
}
</script>