
<template>
    <Card style="width: '100%'; overflow: hidden">
        <template #header>
            <img alt="user header" src="https://primefaces.org/cdn/primevue/images/usercard.png" />
        </template>
        <template #title>Advanced Card</template>
         <template #subtitle>
            <div class="flex align-items-center">
                <i color="#fbbf24" class="pi pi-star-fill"></i> 
                <span>Stars numbers: {{ stars }}</span>
            </div>
            <div class="flex align-items-center">
                <i color="#fbbf24" class="pi pi-share-alt"></i> 
                <span>Forks numbers: {{ forks }}</span>
            </div>
        </template>

        <template #content>
            <p class="m-0">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate neque
                quas!
            </p>
        </template>
        <template #footer>
            <div class="flex gap-3 mt-1">
                <Button label="Go to Repo" class="w-full" icon="pi pi-external-link" @click="goToRepo" />
                <!-- <Button label="Cancel" severity="secondary" outlined class="w-full" /> -->
            </div>
        </template>
    </Card>
</template>

<script>
</script>
<style>
.flex.align-items-center {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    gap: 0.5rem;
}
.pi{ 
    color: #fbbf24;
}
</style>