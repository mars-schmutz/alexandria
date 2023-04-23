<template>
    <form @submit.prevent>
        <div class="attr">
            <label>Name:</label>
            <input type="text" v-model="name" placeholder="Name..."/>
            <p class="err" v-if="err">* Please add a name</p>
        </div>
        <div class="attr">
            <label>Procedural Material:</label>
            <button @click="getSettings()">Open</button>
            <p>{{ fname }}</p>
        </div>
        <button @click="onSubmit()">Save</button>
    </form>
</template>

<script>
export default {
    name: "NewProcMat",
    props: {
        type: String,
    },
    data() {
        return {
            name: "",
            settings: "",
            id: "",
            assetLocation: "",
            thumbnail: "",
            err: false
        }
    },
    computed: {
        fname: function() {
            if (this.settings == "") {
                return "No file selected"
            } else {
                return this.settings.split("/").pop()
            }
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
        async getSettings() {
            let path = await window.alexandria.openFile()
            if (path == "") { return }
            this.settings = path
        },
        async fileEntry() {
            const timestamp = Date.now()
            const randString = Math.random().toString(36).substring(2, 8)
            this.id = `${timestamp}-${randString}`
            this.assetLocation = await window.alexandria.createEntry(this.id)
            let new_path = await window.alexandria.copyFile(this.settings, this.assetLocation)
            this.settings = new_path
        },
        async onSubmit() {
            if (this.nameEmpty()) { return }
            await this.fileEntry()
            let mat = {
                id: this.id,
                name: this.name,
                settings: this.settings,
                path: this.assetLocation,
                thumbnail: this.thumbnail,
                type: this.type
            }
            this.$emit("save", mat)
        }
    }
}
</script>