<template>
  <div class="p-card sidebar">
    <div class="filter-section">
      <h3>Filtering by: </h3>
      <div class="flex align-items-center">
        <Checkbox v-model="selectedFilters" inputId="stars" value="stars" />
        <label for="stars" class="ml-2"> Stars </label>
      </div>
      <div class="flex align-items-center">
        <Checkbox v-model="selectedFilters" inputId="contributors" value="contributors" />
        <label for="contributors" class="ml-2"> Contributors </label>
      </div>
      <div class="flex align-items-center">
        <Checkbox v-model="selectedFilters" inputId="forks" value="forks" />
        <label for="forks" class="ml-2"> Forks </label>
      </div>
    </div>

    <div class="filter-section">
      <h3>Language code: </h3>
      <InputText v-model="language" placeholder="Enter language Code..." />
    </div>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      selectedFilters: [],
      language: '',
      sortOrder: null,
      sortOptions: [
        { name: 'Stars', value: 'stars' },
        { name: 'Contributors', value: 'contributors' },
        { name: 'Forks', value: 'forks' },
        { name: 'Language', value: 'language' }
      ]
    }
  }
}
</script>

<style scoped>
.sidebar .filter-section {
  margin-bottom: 2rem;
}

.sidebar .p-field-checkbox {
  margin-bottom: 1rem;
}

.sidebar h3 {
  margin-bottom: 1rem;
}
.p-card.sidebar {
    padding: 1.5rem;
    margin-top: 1rem;
}
</style>
