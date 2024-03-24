
<template>
    <div class="card">
        <div class="carousel-title">Most Projects by Stars</div>
        <Carousel :value="products" :numVisible="3" :numScroll="1" :responsiveOptions="responsiveOptions" circular :autoplayInterval="3000">
            <template  #item="slotProps">
                <div class="   border-1 surface-border border-round m-2  p-3">
                    <div class="mb-3">
                        <div class="relative mx-auto">
                            <img :src="slotProps.data.avatarURL" :alt="slotProps.data.repositoryName" class=" image border-round" />
                        </div>
                    </div>
                    <div class="BLACK mb-3 font-medium text-xl">{{slotProps.data.repositoryName}}</div>
                    <div class="BLACK flex justify-content-between align-items-center">
                        <div class="mt-0 font-regular text-m">{{slotProps.data.descriptions}}</div>
                        <span>
                            <Button icon="pi pi-heart" severity="secondary" outlined />
                            <Button icon="pi pi-shopping-cart" class="ml-2"/>
                        </span>
                    </div>
                </div>
            </template>
        </Carousel>
    </div>
</template>

<script>
import Axios from 'axios'
export default {

    data() {
        return {
            products: [],
            responsiveOptions: [/* Your responsive options here */],
            currentPage: 1,
            limit: 21, // Assuming you want to fetch 3 items at a time
        };
    },async mounted() {
        await this.fetchData();
    },
    methods: {
        async fetchData() {
            try {
                const response = await Axios.get(`http://91.107.124.108:5173/v1/home/star?limit=${this.limit}&page=${this.currentPage}`);
                this.products = response.data.data;
                this.currentPage++;
                console.log(this.products)
            } catch (error) {
                console.error("Error fetching products:", error);
                // Handle error (e.g., show error message)
            }
        },
        async updateCarousel() {
            await this.fetchData();
            // Implement logic here if needed to update carousel or manage state
        }
    },
    // watch: {
    //     // Watcher to detect changes in carousel (you need to define how to detect this)
    //     // This example won't work as-is because you need a way to detect carousel changes.
    //     // Consider using a carousel event or a method to change slides to trigger this.
    //     currentPage(newValue, oldValue) {
    //         if (newValue !== oldValue) {
    //             this.updateCarousel();
    //         }
    //     },
    // },

    // data() {
    //     return {
            
    //         products: null,
    //         responsiveOptions: [
    //             {
    //                 breakpoint: '1400px',
    //                 numVisible: 2,
    //                 numScroll: 1
    //             },
    //             {
    //                 breakpoint: '1199px',
    //                 numVisible: 3,
    //                 numScroll: 1
    //             },
    //             {
    //                 breakpoint: '767px',
    //                 numVisible: 2,
    //                 numScroll: 1
    //             },
    //             {
    //                 breakpoint: '575px',
    //                 numVisible: 1,
    //                 numScroll: 1
    //             }
    //         ]
    //     };
    // },
    // mounted() {
    //     ProductService.getProductsSmall().then((data) => (this.products = data.slice(0, 9)));
    // },
    // methods: {
    //     getSeverity(status) {
    //         switch (status) {
    //             case 'INSTOCK':
    //                 return 'success';

    //             case 'LOWSTOCK':
    //                 return 'warning';

    //             case 'OUTOFSTOCK':
    //                 return 'danger';

    //             default:
    //                 return null;
    //         }
    //     }
    // }
};
</script>


<style scoped>
.carousel-title {
    color: #333; /* Dark text color for better readability */
    font-size: 2em; /* Large font size */
    font-weight: bold; /* Make the title bold */
    text-align: center; /* Center-align the title */
    margin-bottom: 2rem; /* Add some space between the title and the carousel */
}
.BLACK {
    color: black;

}
.flex.align-items-center {
    flex-direction: column;
    flex-wrap: wrap;
    display: flex;
    justify-content: flex-start !important;
    align-items: flex-start !important;
    gap: 1.5rem;
}
.image {
    width: 100%;
    height: 300px;
    object-fit: cover;
}
.card {
    margin: 6rem 0 0 0;
}
.surface-border { 
    height: 600px;
    max-height: 100%;
}
@media (max-width: 767px) {
    .carousel-title {
        font-size: 1.5em; /* Smaller font size on narrow screens */
        margin-bottom: 1rem; /* Less space on smaller screens */
    }
}


</style>
