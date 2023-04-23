<template>
    <form @submit.prevent>
        <div>
            <label>Name:</label>
            <input type="text" v-model="name" />
        </div>
        <div>
            <label>Settings File:</label>
            <button @click="getPath('settings')">Settings</button>
            <p>{{ settings }}</p>
        </div>
        <button @click="onSubmit()">Save</button>
    </form>
</template>

<script>
export default {
    name: "NewRender",
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
    methods: {
        async getPath(map) {
            let path = await window.alexandria.openFile()
            if (path == "") { return }
            this[map] = path
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
            let render = {
                id: this.id,
                name: this.name,
                settings: this.settings,
                path: this.assetLocation,
                thumbnail: this.thumbnail,
                type: this.type
            }
            this.$emit("save", render)
        }
    }
}
</script>