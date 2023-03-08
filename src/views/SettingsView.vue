<template>
    <h1>Settings</h1>
    <input type="text" v-model="location" />
    <button @click="saveSettings()">Save</button>
</template>

<script>
export default {
    name: "Settings",
    data() {
        return {
            location: ""
        }
    },
    methods: {
        saveSettings() {
            console.log("Saving settings")
            window.store.get("test").then((val) => {
                console.log("Got value: " + val)
            })
        }
    },
}
</script>