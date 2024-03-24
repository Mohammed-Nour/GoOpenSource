<template>
    <div class="grid">
      <ContributorCard
        v-for="contributor in contributors"
        :key="contributor.id"
        :contributorName="contributor.ContributorName"
        :imageSrc="contributor.ContributorPhoto"
        :githubUrl="contributor.ContributorAccount"
      />
    </div>
  </template>
  
  <script>
  import ContributorCard from './ContributorCard.vue'; 
  
  export default {
    components: {
      ContributorCard
    },
    data() {
    return {
      contributors: [
        {
          id: 1,
          ContributorName: 'John Doe',
          ContributorAccount: 'https://github.com/johndoe',
          ContributorPhoto: 'https://primefaces.org/cdn/primevue/images/usercard.png'
        },
        {
          id: 2,
          ContributorName: 'Noor Shahin ',
          ContributorAccount: 'https://github.com/johndoe',
          ContributorPhoto: 'https://primefaces.org/cdn/primevue/images/usercard.png'
        },
        {
          id: 3,
          ContributorName: 'John Doe',
          ContributorAccount: 'https://github.com/johndoe',
          ContributorPhoto: 'https://primefaces.org/cdn/primevue/images/usercard.png'
        },        {
          id: 4,
          ContributorName: 'John Doe',
          ContributorAccount: 'https://github.com/johndoe',
          ContributorPhoto: 'https://primefaces.org/cdn/primevue/images/usercard.png'
        },        {
          id: 5,
          ContributorName: 'John Doe',
          ContributorAccount: 'https://github.com/johndoe',
          ContributorPhoto: 'https://primefaces.org/cdn/primevue/images/usercard.png'
        },
      ],
    }
  },
  methods: {
    showdata() {
      console.log(JSON.stringify(this.contributors));
    }
  },
  mounted() {
    this.showdata();
  }

  }
  </script>
  
  <style scoped>

  .grid{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
  }
  /* Add styles here */
  </style>
  