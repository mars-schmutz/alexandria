<template>
    <div>
        <h3>Details</h3>
        <template v-if="asset">
            <h4>{{ asset.name }}</h4>
            <button @click="editEntry()">Edit</button>
            <button @click="retrieveEntry()">View on disk</button>
        </template>
        <template v-else>
            <p>Loading...</p>
        </template>
    </div>
</template>

<script>
export default {
    name: "DetailView",
    data() {
        return {
            id: this.$route.params.id,
            asset: null,
        }
    },
    methods: {
        async retrieveEntry() {
            try {
                console.log(`Opening ${this.asset.path}...`)
                await window.alexandria.openEntry(this.asset.path)
            } catch (err) {
                console.log(err)
            }
        },
        editEntry() {
            this.$router.push(`/edit/${this.asset.id}`)
        }
    },
    created() {
        window.store.get("library-shelves").then((val) => {
            let i = val.findIndex(asset => asset.id == this.id)
            this.asset = val[i]
        })
    }
}
</script>