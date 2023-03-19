<template>
    <form @submit.prevent>
        <div>
            <label>Name:</label>
            <input type="text" v-model="name" />
        </div>
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
        <button @click="onSubmit()">Save</button>
    </form>
</template>

<script>
export default {
    name: "NewMaterial",
    props: {
        type: String,
    },
    data() {
        return {
            name: "",
            assetLocation: "default_path",
            asset_info: {
                diffuse: "",
                metallic: "",
                specular: "",
                roughness: "",
                normal: "",
                bump: "",
                displacement: "",
            },
            asset_tags: "",
            mat_workflow: "",
        }
    },
    methods: {
        async getPath(mat_map) {
            const path = await window.alexandria.openFile()
            this.asset_info[mat_map] = path
        },
        async fileEntry() {
            let entry_path = this.name.split(" ").join("_")
            try {
                this.assetLocation = await window.alexandria.createEntry(entry_path)
                console.log(`assetLocation: ${this.assetLocation}`)
            } catch (err) {
                console.log(err)
            }
            console.log(`assetLocation: ${this.assetLocation}`)
        },
        async onSubmit() {
            await this.fileEntry()

            const timestamp = Date.now().toString(36)
            const randNum = Math.random().toString(36)
            const newId = timestamp + randNum
            let currLib = await window.store.get("library-shelves") ? await window.store.get("library-shelves") : []
            let mat = {
                id: newId,
                name: this.name,
                path: "default_path",
                type: this.type,
                tags: this.asset_tags,
                workflow: this.mat_workflow,
                maps: {
                    diffuse: this.asset_info.diffuse,
                    metallic: this.asset_info.metallic,
                    specular: this.asset_info.specular,
                    roughness: this.asset_info.roughness,
                    normal: this.asset_info.normal,
                    bump: this.asset_info.bump,
                    displacement: this.asset_info.displacement,
                }
            }

            currLib.push(mat)
            console.log(`currLib: ${JSON.stringify(currLib)}`)
            window.store.set("library-shelves", currLib).then((val) => {
                console.log(`val: ${val}`)
            }).catch((err) => {
                console.log("error pushing to library-shelves")
                console.log(err)
            })

            this.$router.push("/")
        }
    }
}
</script>