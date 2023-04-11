<template>
    <div class="asset">
        <span class="delete" @click="$emit('delete')">&#10006;</span>
        <div @click="$emit('view')">
            <h4>{{ name }}</h4>
            <div class="thumbnail" :style="{ backgroundImage: `url('${thumbnail}')` }"></div>
        </div>
    </div>
</template>

<script>
export default {
    name: "Asset",
    props: {
        name: String,
        thumbnail: String
    },
    mounted() {
        if (this.thumbnail == "") {
            this.thumbnail = "../assets/logo.svg"
        }
    }
}
</script>

<style scoped>
.asset {
    align-self: flex-start;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    width: 9rem;
    height: 9rem;
    padding-bottom: 0.75rem;
    border: 1px solid #ccc;
    position: relative;
}

span {
    cursor: pointer;
    position: absolute;
    top: 10px;
    right: 10px;
}

.thumbnail {
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;
    width: 6rem;
    height: 6rem;
}
</style>