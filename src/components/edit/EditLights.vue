<template>
    <form @submit.prevent>
        <h1>Edit Light Rig</h1>
        <div>
            <label>Name:</label>
            <input type="text" v-model="new_name" @keydown.enter.prevent/>
        </div>
        <div>
            <label>Rig File:</label>
            <button @click="getPath()">Rig</button>
            <p>{{ settings }}</p>
        </div>
        <button @click="onSubmit()">Update</button>
    </form>
</template>

<script>
export default {
    name: "EditLights",
    props: {
        asset: Object,
        required: true
    },
    data() {
        return {
            new_name: this.asset.name,
            settings: this.asset.settings,
            id: this.$route.params.id,
        }
    },
    methods: {
        async getPath() {
            const path = await window.alexandria.openFile()
            if (path == "") { return }
            await window.alexandria.deleteEntry(this.asset.settings)
            this.settings = path
        },
        async onSubmit() {
            let updated = {
                name: this.new_name,
                settings: this.settings,
            }
            this.$emit("update", updated)
        }
    }
}
</script>