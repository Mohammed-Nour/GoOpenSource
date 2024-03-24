
<template>
    <div class="card flex justify-content-center">
        <Button label="Contributors" severity="secondary" @click="visible = true" />
        <Dialog v-model:visible="visible" modal header="Contributors" :style="{ width: '50%' }">
            <template #footer>
                <Button label="Close" text severity="secondary" @click="visible = false" autofocus />
            </template>
        </Dialog>
    </div>
</template>

<script>
export default {
    data() {
        return {
            visible: false
        };
    }
};
</script>
