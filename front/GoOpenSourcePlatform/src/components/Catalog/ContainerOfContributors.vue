<template>
    <div>
      <ContributorCard
        v-for="contributor in contributors"
        :key="contributor.id"
        :contributorName="contributor.contributorName"
        :imageSrc="contributor.contributorPhoto"
        :githubUrl="contributor.contributorAccount"
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
          ContributorName: 'John Doe',
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
      ]
    }
  },

  }
  </script>
  
  <style>
  /* Add styles here */
  </style>
  