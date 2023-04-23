<template>
    <form @submit.prevent>
        <div class="attr">
            <label>Name:</label>
            <input type="text" v-model="name" placeholder="Name..."/>
            <p class="err" v-if="err">* Please add a name</p>
        </div>
        <div class="attr">
            <label>Thumbnail:</label>
            <button @click="getPath('thumbnail')">Open</button>
            <p>{{ asset_info.thumbnail.split("/").pop() }}</p>
        </div>
        <div>
            <h3>Texture Maps:</h3>
            <div class="attr">
                <label>Diffuse</label>
                <button @click="getPath('diffuse')">Open</button>
                <p>{{ asset_info.diffuse.split("/").pop() }}</p>
            </div>
            <div class="attr">
                <label>Metallic</label>
                <button @click="getPath('metallic')">Open</button>
                <p>{{ asset_info.metallic.split("/").pop() }}</p>
            </div>
            <div class="attr">
                <label>Specular</label>
                <button @click="getPath('specular')">Open</button>
                <p>{{ asset_info.specular.split("/").pop() }}</p>
            </div>
            <div class="attr">
                <label>Roughness</label>
                <button @click="getPath('roughness')">Open</button>
                <p>{{ asset_info.roughness.split("/").pop() }}</p>
            </div>
            <div class="attr">
                <label>Normal</label>
                <button @click="getPath('normal')">Open</button>
                <p>{{ asset_info.normal.split("/").pop() }}</p>
            </div>
            <div class="attr">
                <label>Bump</label>
                <button @click="getPath('bump')">Open</button>
                <p>{{ asset_info.metallic.split("/").pop() }}</p>
            </div>
            <div class="attr">
                <label>Displacement</label>
                <button @click="getPath('displacement')">Open</button>
                <p>{{ asset_info.displacement.split("/").pop() }}</p>
            </div>
        </div>
        <button @click="onSubmit()">Save</button>
        <p class="err" v-if="err">Please fix the errors</p>
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
            err: false
        }
    },
    methods: {
        nameEmpty() {
            if (this.name == "") {
                this.err = true
                return true 
            } else {
                this.err = false
                return false 
            }
        },
        async getPath(mat_map) {
            const path = await window.alexandria.openFile()
            if (path == "") { return }
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
            if (this.nameEmpty()) { return }
            await this.fileEntry()

            let currLib = await window.store.get("library-shelves") ? await window.store.get("library-shelves") : []
            let mat = {
                id: this.id,
                name: this.name,
                thumbnail: this.asset_info.thumbnail,
                path: this.assetLocation,
                type: this.type,
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