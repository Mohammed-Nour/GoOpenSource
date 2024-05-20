<template>
    <Card style="width: '100%'; overflow: hidden">
      <template #header>
        <img :alt="`${contributorName}'s header`" :src="imageSrc" />
      </template>
      <template #title>
        {{ this.contributorName }}
      </template>
      <template #content>
      </template>
      <template #footer>
        <div class="flex gap-3 mt-1">
          <Button label="Check Github" class="w-full" icon="pi pi-external-link" @click="checkbug"  />
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
    },
    checkbug () {
      console.log(this.name);
      console.log(this.contributorName);
      console.log(this.imageSrc);
      console.log(this.githubUrl);
    }
  }
}
</script>
<style>
</style>