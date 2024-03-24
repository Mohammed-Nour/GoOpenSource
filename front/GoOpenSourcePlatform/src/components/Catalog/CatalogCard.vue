
<template>
    <Card style="width: '100%'; overflow: hidden">
        <template #header>
            <!-- <img alt="user header" :src="avatarURL" /> -->
        </template>
        <template #title>{{ repositoryName }}</template>
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
                {{ descriptions }}
            </p>
        </template>
        <template #footer>
            <div class="flex gap-3 mt-1">
                <Button label="Go to Repo" class="w-full" icon="pi pi-external-link" @click="goToRepo" />
                <DialogContributors></DialogContributors>
                <!-- <Button label="Fork" class="w-full" icon="pi pi-code" @click="goToFork"/> -->
                <!-- <Button label="Cancel" severity="secondary" outlined class="w-full" /> -->
            </div>
        </template>
    </Card>
</template>

<script>
import DialogContributors from '../Catalog/DialogContributors.vue'

export default {
  
  components: {
    DialogContributors,
  },
  props: {
    repositoryID : String,
    repositoryName: String,
    forks: String,
    stars: String,
    descriptions: String,
    avatarURL: String,
    contributorAccount: String
  },
  data() {
    return {
     
    }
  },
  methods: {
    goToFork(){
        window.open('https://www.github.com', '_blank');
    }
  }
}
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