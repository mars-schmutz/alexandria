<template>
    <form @submit.prevent>
        <div class="attr">
            <label>Name:</label>
            <input type="text" v-model="name" placeholder="Name..."/>
        </div>
        <div class="attr">
            <label>Compositor Settings:</label>
            <button @click="getSettings()">Open</button>
            <p>{{ fname }}</p>
        </div>
        <button @click="onSubmit()">Save</button>
    </form>
</template>

<script>
export default {
    name: "NewCompositor",
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
            await this.fileEntry()
            let asset = {
                id: this.id,
                name: this.name,
                settings: this.settings,
                path: this.assetLocation,
                thumbnail: this.thumbnail,
                type: this.type
            }
            this.$emit("save", asset)
        }
    }
}
</script>