<template>
  <div class="projects-catalog">
    <div class="container_filtering_projects">
      <SiderBar></SiderBar>
      <div class="container_search_products">
        <header class="projects-header">
          <h1>Projects Catalog</h1>
          <div class="search-bar">
            <input
              type="text"
              v-model="searchQuery"
              placeholder="Search for a product by AI..."
              class="search-input"
            />
            <button @click="performSearch" class="search-button">Search</button>
          </div>
        </header>
        <section class="product-list product-grid">
          <CatalogCard
            v-for="product in filteredProducts"
            :key="product.id"
            :bigTitle="product.big_title"
            :small-title="product.small_title"
            :description="product.description"
            :features="product.features"
            :primary-color="product.primary_color"
            :secondary-color="product.secondary_color"
          ></CatalogCard>
          <div class="no-products-container" v-if="filteredProducts.length === 0">
            <p class="no-products">Such project is not available...</p>
          </div>
        </section>
      </div>
    </div>
  </div>
</template>

<script>
import CatalogCard from '@/components/Catalog/CatalogCard.vue'
import SiderBar from '@/components/Catalog/SiderBar.vue'

export default {
  components: {
    CatalogCard,
    SiderBar
  },
  data() {
    return {
      products: [
        // Example JSON Data
        {
          id: 1,
          big_title: 'Code QA',
          small_title: 'Code Understanding AI',
          description:
            "Boost your coding experience: Code Expert LLM analyzes for bugs, suggests improvements, ensuring flawless, efficient projects—your code's best friend!",
          features: [
            'Ensuring smooth projects: Keep projects running smoothly with efficient issue resolution.',
            'Identifying problems: Find and fix bugs and code standard violations.',
            'Suggesting improvements: Offer valuable tips for code readability and efficiency.',
            'Suggesting improvements: Offer valuable tips for code readability and efficiency.'
          ],
          primary_color: '#308FFE',
          secondary_color: '#B0E3FF'
        },
        {
          id: 2,
          big_title: 'IU Code generator',
          small_title: 'YOUR CODING ASSISTANT',
          description:
            "Boost your coding experience: Code Expert LLM analyzes for bugs, suggests improvements, ensuring flawless, efficient projects—your code's best friend!",
          features: [
            'Ensuring smooth projects: Keep projects running smoothly with efficient issue resolution.',
            'Identifying problems: Find and fix bugs and code standard violations.',
            'Suggesting improvements: Offer valuable tips for code readability and efficiency.',
            'Suggesting improvements: Offer valuable tips for code readability and efficiency.'
          ],
          primary_color: '#8FE036',
          secondary_color: '#DAFFB1'
        },
        {
          id: 3,
          big_title: 'Beluga LLM',
          small_title: 'YOUR NEW FRIEND',
          description:
            "Boost your coding experience: Code Expert LLM analyzes for bugs, suggests improvements, ensuring flawless, efficient projects—your code's best friend!",
          features: [
            'Ensuring smooth projects: Keep projects running smoothly with efficient issue resolution.',
            'Identifying problems: Find and fix bugs and code standard violations.',
            'Suggesting improvements: Offer valuable tips for code readability and efficiency.',
            'Suggesting improvements: Offer valuable tips for code readability and efficiency.'
          ],
          primary_color: '#8A2FE3',
          secondary_color: '#BBB0FF'
        },
        {
          id: 4,
          big_title: 'Method Messages',
          small_title: 'Enhances code documentation',
          description:
            "Boost your coding experience: Code Expert LLM analyzes for bugs, suggests improvements, ensuring flawless, efficient projects—your code's best friend!",
          features: [
            'Ensuring smooth projects: Keep projects running smoothly with efficient issue resolution.',
            'Identifying problems: Find and fix bugs and code standard violations.',
            'Suggesting improvements: Offer valuable tips for code readability and efficiency.',
            'Suggesting improvements: Offer valuable tips for code readability and efficiency.'
          ],
          primary_color: '#FF8811',
          secondary_color: '#FFDCB9'
        }
      ],
      filteredProducts: [],
      searchQuery: ''
    }
  },
  created() {
    // Initialize filteredProducts with all products on creation
    this.filteredProducts = this.products
  },
  watch: {
    searchQuery(newVal, oldVal) {
      this.performSearch()
    }
  },
  methods: {
    performSearch() {
      if (this.searchQuery) {
        this.filteredProducts = this.products.filter(
          (product) =>
            product.big_title.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
            product.small_title.toLowerCase().includes(this.searchQuery.toLowerCase())
        )
      } else {
        // If search query is empty, show all products
        this.filteredProducts = this.products
      }
    }
  }
}
</script>

<style scoped>
.projects-catalog {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-image: url('../assets/images/main-page/pattern-bg.svg');
}
.container_filtering_projects {
  display: flex;
  justify-content: space-between;
  margin: 0;
  gap: 5rem;
  width: 80%;
}
.container_search_products {
  padding: 0 0;
  margin: 0 10% 0 0;
}
.product-header {
  display: flex;
  justify-content: flex-start;
  align-items: center;
}
.search-bar[data-v-e5ae2966] {
  position: relative;
  width: 100%;
  max-width: 70%;
  border-radius: 2.5rem;
  border: 1px solid #000000b8;
}

.product-grid[data-v-e5ae2966] {
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  width: 100%;
  margin-right: 5%;
}

.projects-header > h1 {
  color: Black;
  font-family: Raleway;
  font-weight: bold;
  font-size: 30px;
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(350px, 1fr));
  grid-column-gap: 35px;
  grid-row-gap: 35px;
  padding: 20px;
  margin-bottom: 50px;
}

.background {
  position: absolute;
  z-index: 0;
  top: 0;
  left: 0;
}

h1 {
  font-size: larger;
  color: black;
}

.projects-header {
  width: 70vw;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 20px;
  margin-bottom: 20px;
}

.no-products-container {
  grid-column: span 2;
  width: 70vw;
  height: 60vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.no-products {
  text-align: center;
  margin-top: 20px;
  font-family: IBM Plex Mono;
  font-weight: 500;
  font-size: 30px;
  color: black;
}

.search-bar {
  position: relative;
  width: 100%;
  max-width: 436px;
  /* background-color: #000; Adjust the color to match your theme */
}

.search-input {
  flex-grow: 1;
  width: 436px;
  height: 42px;
  border: none;
  /* Hide the right border */
  padding: 20px;
  border-radius: 30px;
  color: #fbbf24;
  /* border-top-left-radius: 30px;
    border-bottom-left-radius: 20px; */
  outline: none;
  background: transparent;
  /* Set the placeholder color */
}

.search-input::placeholder {
  font-family: IBM Plex Mono;
  font-size: 14px;
  color: #aaa;
}

.search-button {
  position: absolute;
  top: 51%;
  right: 3px; /* Adjust as needed */
  transform: translateY(-50%);
  padding: 9px 22px;
  text-align: center;
  border: 2px solid #fbbf24;
  border-radius: 30px;
  background-color: #fbbf24; /* Adjust the button background color if needed */
  color: white; /* Adjust the text color if needed */
  cursor: pointer;
  outline: none;
  transition: all 0.3s ease-in-out;
}

.search-button:hover {
  background: transparent;
  color: #fbbf24;
}

@media (max-width: 768px) {
  .projects-catalog {
    /* background: black; */
    background-image: url('../assets/images/main-page/pattern-bg.svg');
  }
  .projects-header {
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  .search-bar {
    margin-top: 1rem;
    width: auto;
  }
  .search-input {
    width: 90vw;
  }

  .product-grid {
    grid-template-columns: 1fr;
  }
  .container_filtering_projects {
    flex-wrap: wrap;
  }
  .p-card.sidebar {
    height: fit-content;
    width: 100%;
  }
  .container_search_products {
    margin: 0 5%;
  }
}
</style>
