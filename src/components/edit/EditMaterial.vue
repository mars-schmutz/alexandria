<template>
    <form @submit.prevent>
        <h1>Edit Material</h1>
        <div>
            <label>Name:</label>
            <input type="text" v-model="new_name" @keydown.enter.prevent/>
        </div>
        <div>
            <label>Thumbnail:</label>
            <button @click="getPath('thumbnail')">Thumbnail</button>
            <p>{{ info.thumbnail }}</p>
        </div>
        <div>
            <h3>Texture Maps:</h3>
            <div>
                <label>Diffuse</label>
                <button @click="getPath('diffuse')">Diffuse</button>
                <p>{{ info.diffuse }}</p>
            </div>
            <div>
                <label>Metallic</label>
                <button @click="getPath('metallic')">Metallic</button>
                <p>{{ info.metallic }}</p>
            </div>
            <div>
                <label>Specular</label>
                <button @click="getPath('specular')">Specular</button>
                <p>{{ info.specular }}</p>
            </div>
            <div>
                <label>Roughness</label>
                <button @click="getPath('roughness')">Roughness</button>
                <p>{{ info.roughness }}</p>
            </div>
            <div>
                <label>Normal</label>
                <button @click="getPath('normal')">Normal</button>
                <p>{{ info.normal }}</p>
            </div>
            <div>
                <label>Bump</label>
                <button @click="getPath('bump')">Bump</button>
                <p>{{ info.bump }}</p>
            </div>
            <div>
                <label>Displacement</label>
                <button @click="getPath('displacement')">Displacement</button>
                <p>{{ info.displacement }}</p>
            </div>
        </div>
        <button @click="onSubmit()">Update</button>
    </form>
</template>

<script>
export default {
    name: "EditMaterial",
    props: {
        asset: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            id: this.$route.params.id,
            new_name: this.asset.name,
            info: {
                thumbnail: this.asset.thumbnail,
                diffuse: this.asset.maps.diffuse,
                metallic: this.asset.maps.metallic,
                specular: this.asset.maps.specular,
                roughness: this.asset.maps.roughness,
                normal: this.asset.maps.normal,
                bump: this.asset.maps.bump,
                displacement: this.asset.maps.displacement,
            }
        }
    },
    methods: {
        async getPath(mat_map) {
            const path = await window.alexandria.openFile()
            this.info[mat_map] = path
            if (mat_map == "thumbnail") {
                await window.alexandria.deleteEntry(this.asset.thumbnail)
            } else {
                if (this.info[mat_map] !== this.asset.maps[mat_map] && this.asset.maps[mat_map] !== "") {
                    await window.alexandria.deleteEntry(this.asset.maps[mat_map])
                }
            }
        },
        async copyFiles() {
            for (let key in this.info) {
                if (this.info[key] != "") {
                    let new_path = await window.alexandria.copyFile(this.info[key], this.asset.path)
                    this.info[key] = new_path
                }
            }
        },
        async onSubmit() {
            await this.copyFiles()
            let currLib = await window.store.get("library-shelves")
            let toUpdate = currLib.findIndex(asset => asset.id == this.id)
            currLib[toUpdate].name = this.new_name
            currLib[toUpdate].thumbnail = this.info.thumbnail
            currLib[toUpdate].tags = this.new_tags
            currLib[toUpdate].maps.diffuse = this.info.diffuse
            currLib[toUpdate].maps.metallic = this.info.metallic
            currLib[toUpdate].maps.specular = this.info.specular
            currLib[toUpdate].maps.roughness = this.info.roughness
            currLib[toUpdate].maps.normal = this.info.normal
            currLib[toUpdate].maps.bump = this.info.bump
            currLib[toUpdate].maps.displacement = this.info.displacement
            try {
                await window.store.set("library-shelves", currLib)
            } catch (err) {
                console.log(err)
            }
            this.$router.push(`/details/${this.id}`)
        }
    }
}
</script>