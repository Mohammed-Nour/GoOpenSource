<template>
    <Card style="width: '100%'; overflow: hidden">
      <template #header>
        <img :alt="`${contributorName}'s header`" :src="imageSrc" />
      </template>
      <template #title>
        {{ contributorName }}
      </template>
      <template #content>
      </template>
      <template #footer>
        <div class="flex gap-3 mt-1">
          <Button label="Go to Repo" class="w-full" icon="pi pi-external-link" @click="goToRepo" />
        </div>
      </template>
    </Card>
  </template>

<script>
export default {
  props: {
    contributorName: String,
    imageSrc: String,
    githubUrl: String,
  },
  methods: {
    goToRepo() {
      window.open(this.githubUrl, '_blank');
    }
  }
}
</script>
<style>
</style>