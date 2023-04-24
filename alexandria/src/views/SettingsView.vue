<template>
    <h1>Settings</h1>
    <label>Library Location:</label>
    <input type="text" v-model="location" />
    <button @click="openPath()">Select Location</button>
    <button @click="saveSettings()" id="save-btn">Save</button>
    <button @click="prefPath()">Get My Settings</button>
    <p>{{ this.prefs }}</p>
    <div class="attributions">
        <p>Credits for licensing requirements</p>
        <p>https://www.flaticon.com/free-icons/photography - Photography icons created by Freepik - Flaticon</p>
    </div>
</template>

<script>
export default {
    name: "Settings",
    data() {
        return {
            location: window.store.get("library-location").then((val) => {
                val ? this.location = val : this.location = ""
            }),
            prefs: ""
        }
    },
    methods: {
        saveSettings() {
            window.store.set("library-location", this.location).then((val) => {})
        },
        async openPath() {
            const path = await window.alexandria.openFile(true)
            this.location = path
        },
        prefPath() {
            window.alexandria.getPrefPath().then((val) => {
                this.prefs = val
                navigator.clipboard.writeText(val)
            })
        }
    },
}
</script>

<style scoped>
input[type="text"] {
    width: 100%;
}

.attributions {
    margin-top: 5rem;
}

#save-btn {
}
</style>