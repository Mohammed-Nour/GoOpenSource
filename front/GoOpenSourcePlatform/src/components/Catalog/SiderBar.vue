<template>
  <Sidebar v-model:visible="visible" header="Filtering">
      <div class="filter-section">
      <h3>Sorting by: </h3>
      <div class="flex align-items-center">
        <Checkbox v-model="selectedFilters" inputId="stars" value="stars" />
        <label for="stars" class="ml-2"> Stars </label>
      </div>
      <!-- <div class="flex align-items-center">
        <Checkbox v-model="selectedFilters" inputId="contributors" value="contributors" />
        <label for="contributors" class="ml-2"> Contributors </label>
      </div> -->
      <div class="flex align-items-center">
        <Checkbox v-model="selectedFilters" inputId="forks" value="forks" />
        <label for="forks" class="ml-2"> Forks </label>
      </div>
  </div>
   

    <div class="filter-section mb-3">
      <h3>Language code: </h3>
      <InputText v-model="language" placeholder="Enter language Code..." />
      <h3>Limit of Projects:</h3>
      <InputText v-model="limit" placeholder="Enter the Limit of products..." />
      <h3>Page offset: </h3>
      <InputText v-model="page" placeholder="Enter the page offset..." />
    </div>
    <Button class="mt-3" label="Apply Filter" icon="pi pi-arrow-right" name="Filtering" title="Filtering" @click="sendFilterRequest" />
  </Sidebar> 
  <Button icon="pi pi-arrow-right" name="Filtering" title="Filtering" @click="visible = true" />
</template>

<script>
import Axios from 'axios';
import { ref, defineExpose } from 'vue'
export default {
  expose: ['sendFilterRequest'],
  props: {
    searchQuery : String,
  },
  components: {},
  data() {
    return {
      visible: false,
      selectedFilters: [],
      language: '',
      sortOptions: [
        { name: 'Stars', value: 'stars' },
        { name: 'Forks', value: 'forks' },
        { name: 'Language', value: 'language' }
      ]
    }
  },
  methods: {
    generateQueryParams() {
      const params = new URLSearchParams();

      // Append 'query=name' as it seems to be a constant requirement
      params.append('query', this.searchQuery);

      // Check and append filters based on selectedFilters
      this.selectedFilters.forEach(filter => {
        if (filter === 'forks' || filter === 'stars') {
          params.append(filter, filter); // Assuming the API expects 'forks=forks' & 'stars=stars'
        }
      });

      // Append language if selected
      if (this.language) {
        params.append('lang', this.language);
      }

      // You can add other parameters like limit and page in a similar manner
      if (this.limit) {
        params.append('limit', this.limit);
      }
      if (this.page) {
        params.append('page', this.page);
      }

      return params;
    },
    sendFilterRequest() {
      console.log("hello")
      const queryParams = this.generateQueryParams();
      const url = `http://91.107.124.108:5173/v1/search?${queryParams.toString()}`;
      console.log(url);
      this.$emit('loading');
      
      Axios.get(url)
        .then(response => {
          // Handle the response from the server
          console.log(response.data.data);
          const productCatalog = response.data.data;
          this.$emit('fetched', productCatalog);
          this.$emit('loading');

        })
        .catch(error => {
          // Handle errors here
          console.error('There was an error with the request:', error);
        });
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

.filter-section {
    display: flex;
    justify-content: flex-start;
    align-items: flex-start;
    flex-direction: column;
    gap: 0.5rem;
}
p-sidebar-content {
    display: flex;
    justify-content: flex-start;
    flex-direction: column;
    gap: 3rem;
}
button.p-button.p-component.p-button-icon-only{ 
  width:  fit-content;
    height: fit-content;
    padding: 1rem 1.5rem;
    margin: 1.2rem 0;
}
</style>
