<template>
    <div class="asset" @click="$emit('view')">
        <span class="delete" @click.stop="$emit('delete')">&#10006;</span>
        <div class="info">
            <p>{{ name }}</p>
            <template v-if="thumbnail != ''">
                <div class="thumbnail" :style="{ backgroundImage: `url('${thumbnail}')` }"></div>
            </template>
            <template v-else>
                <!-- <img class="icon" :src="icon" /> -->
                <svg class="icon">
                    <use :xlink:href="`${icon}#icon`" />
                </svg>
            </template>
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
                import("@/assets/material.svg").then((icon) => {
                    this.icon = icon.default
                })
            } else if (this.assetType == "render") {
                import("@/assets/render.svg").then((icon) => {
                    this.icon = icon.default
                })
            } else if (this.assetType == "lights") {
                import("@/assets/lightbulb.svg").then((icon) => {
                    this.icon = icon.default
                })
            } else if (this.assetType == "proc_mat") {
                import("@/assets/material.svg").then((icon) => {
                    this.icon = icon.default
                })
            } else if (this.assetType == "compositor") {
                import("@/assets/compositor.svg").then((icon) => {
                    this.icon = icon.default
                })
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
    height: 10rem;
    padding-bottom: 0.75rem;
    border-radius: 0.5rem;
    position: relative;
    margin: 0.5rem;

    box-shadow: 4px 4px 10px 0 rgba(0, 0, 0, 0.25),
        -2px -2px 15px 0 rgba(0, 0, 0, 0.25);
}

.info {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 0.6rem;
}

.delete {
    cursor: pointer;
    position: absolute;
    top: 10px;
    right: 10px;
    margin-bottom: 0.25rem;
}

.thumbnail {
    margin-top: 0.5rem;
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;
    width: 6rem;
    height: 6rem;
    border-radius: 0.5rem;
}

.icon {
    /* display: block; */
    width: 6rem;
    height: 6rem;
}

@media (prefers-color-scheme: dark) {
    .asset {
        background-color: var(--cards);
        box-shadow: unset;
    }

    .icon {
        fill: var(--color-highlight);
    }
}
</style>