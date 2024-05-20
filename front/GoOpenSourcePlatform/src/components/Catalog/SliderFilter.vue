
<template>
    <div class="card flex justify-content-center">
        <div class="w-14rem">
            <InputText v-model.number="value" class="w-full mb-3" />
            <Slider v-model="value" class="w-full" />
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            value: 50
        }
    }
};
</script>
<style>
span.p-slider-handle {
    top: -8px;

}
</style>