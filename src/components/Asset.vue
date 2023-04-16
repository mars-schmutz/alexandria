<template>
    <div class="asset">
        <span class="delete" @click="$emit('delete')">&#10006;</span>
        <div @click="$emit('view')">
            <h4>{{ name }}</h4>
            <template v-if="thumbnail != ''">
                <div class="thumbnail" :style="{ backgroundImage: `url('${thumbnail}')` }"></div>
            </template>
            <template v-else>
                <!-- <img class="icon" :src="icon" /> -->
                <svg class="icon">
                    <use :xlink:href="`${icon}#render`" />
                </svg>
            </template>
            <!-- <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" /> -->
        </div>
    </div>
</template>

<script>
export default {
    name: "Asset",
    props: {
        name: String,
        thumbnail: String,
        assetType: String
    },
    data() {
        return {
            icon: this.thumbnail
        }
    },
    mounted() {
        if (this.icon == "") {
            if (this.assetType == "material") {
                this.icon = "@/assets/logo.svg"
            } else if (this.assetType == "render-settings") {
                import("@/assets/render.svg").then((icon) => {
                    this.icon = icon.default
                    console.log("set icon")
                })
            } else {
                console.log(this.assetType)
            }
        }
    }
}
</script>

<style>
@import "@/assets/base.css";

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

.delete {
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

.icon {
    /* display: block; */
    width: 6rem;
    height: 6rem;
}

@media (prefers-color-scheme: dark) {
    .icon {
        fill: var(--color-highlight);
    }
}
</style>