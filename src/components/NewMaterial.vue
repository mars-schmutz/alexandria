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
            <label>Thumbnail:</label>
            <button @click="getPath('thumbnail')">Thumbnail</button>
            <p>{{ asset_info.thumbnail }}</p>
        </div>
        <div>
            <h3>Texture Maps:</h3>
            <div>
                <label>Diffuse</label>
                <button @click="getPath('diffuse')">Diffuse</button>
                <p>{{ asset_info.diffuse }}</p>
            </div>
            <div>
                <label>Metallic</label>
                <button @click="getPath('metallic')">Metallic</button>
                <p>{{ asset_info.metallic }}</p>
            </div>
            <div>
                <label>Specular</label>
                <button @click="getPath('specular')">Specular</button>
                <p>{{ asset_info.specular }}</p>
            </div>
            <div>
                <label>Roughness</label>
                <button @click="getPath('roughness')">Roughness</button>
                <p>{{ asset_info.roughness }}</p>
            </div>
            <div>
                <label>Normal</label>
                <button @click="getPath('normal')">Normal</button>
                <p>{{ asset_info.normal }}</p>
            </div>
            <div>
                <label>Bump</label>
                <button @click="getPath('bump')">Bump</button>
                <p>{{ asset_info.metallic }}</p>
            </div>
            <div>
                <label>Displacement</label>
                <button @click="getPath('displacement')">Displacement</button>
                <p>{{ asset_info.displacement }}</p>
            </div>
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
            id: "",
            name: "",
            assetLocation: "default_path",
            asset_info: {
                thumbnail: "",
                diffuse: "",
                metallic: "",
                specular: "",
                roughness: "",
                normal: "",
                bump: "",
                displacement: "",
            },
            asset_tags: "",
        }
    },
    methods: {
        async getPath(mat_map) {
            const path = await window.alexandria.openFile()
            this.asset_info[mat_map] = path
        },
        async fileEntry() {
            const timestamp = Date.now()
            const randString = Math.random().toString(36).substring(2, 8)
            this.id = `${timestamp}-${randString}`
            this.assetLocation = await window.alexandria.createEntry(this.id)
            await this.copyFiles()
        },
        async copyFiles() {
            for (let key in this.asset_info) {
                if (this.asset_info[key] != "") {
                    let new_path = await window.alexandria.copyFile(this.asset_info[key], this.assetLocation)
                    this.asset_info[key] = new_path
                }
            }
        },
        async onSubmit() {
            await this.fileEntry()

            let currLib = await window.store.get("library-shelves") ? await window.store.get("library-shelves") : []
            let mat = {
                id: this.id,
                name: this.name,
                thumbnail: this.asset_info.thumbnail,
                path: this.assetLocation,
                type: this.type,
                tags: this.asset_tags,
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
            try {
                await window.store.set("library-shelves", currLib)
            } catch (err) {
                console.log("error pushing to library-shelves")
                console.log(err)
            }

            this.$router.push("/")
        }
    }
}
</script>