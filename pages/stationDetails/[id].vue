<template>
    <h1 v-text="station.address" class="text-center text-5xl mt-16 tracking-wide relative"></h1>
    <div>
        <StationDetails :sockets="station.sockets" :stationid="id" />
    </div>
    <div class="text-center mt-20">
        <p
            class="w-full px-3 py-2 mb-3 text-lm leading-tight text-red-700 rounded appearance-none focus:outline-none focus:shadow-outline">
            {{ response }}
        </p>
    </div>
    <h1 class="text-center text-4xl mt-16 tracking-wide relative">Active Discounts</h1>
    <div class="grid grid-flow-col mb-32 mx-64 mt-8 md:mt-16 ">
        <DiscountCardForEMSP v-for="discount in discounts" :id="discount.id" :start_date="discount.start_date"
            :end_date="discount.end_date" :discount_amount="discount.discount_amount"
             />
    </div>
</template>


<script>
export default {
    data() {
        return {
            station: "",
            id: "",
            bookingLength: 0,
            discounts: "",
        }
    },
    setup() {
        definePageMeta({
            middleware: ['auth'],
            layout: "emspnavlayout"
        })
        const route = useRoute()// When accessing /posts/1, route.params.id will be 1

    },
    mounted() {
        setInterval(() => {
            location.reload()
        }, 60000) // reload every 60 seconds
    },
    created() {
        this.updateStation()
    },

    methods: {
        async updateStation() {
            try {
                this.id = this.$route.params.id
                console.log("ID", this.id)
                if (this.id == null)
                    throw new Error("No ID provided")

                let { response, json } = await getRequestWithToken('emsp', 'OCPI/getChargingStationById/' + this.id + '/')
                this.station = json.station
                this.discounts = json.discounts
                let today = new Date();
                let activeDiscounts = this.discounts.filter(discount => {
                    let start = new Date(discount.start_date);
                    let end = new Date(discount.end_date);
                    return today >= start && today <= end;
                })
                .sort((a, b) => b.discount_amount - a.discount_amount);
                
                this.discounts = activeDiscounts;
                
            } catch (error) {
                this.response = error
                console.error(error)
            }
        },
    }
};
</script>

<style>
.grid-flow-col {
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: auto;
    grid-auto-flow: row;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    /* leave margin on the left and right of the grid */
    margin-left: 10%;
    margin-right: 10%;
}

/* this settings change the number of cards per row based on how wide is the screen, it should never "overflow" on one side*/
@media (max-width: 700px) {
    .grid-flow-col {
        grid-template-columns: repeat(1, 1fr);
    }
}

@media (min-width: 701px) and (max-width: 1000px) {
    .grid-flow-col {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (min-width: 1001px) and (max-width: 1400px) {
    .grid-flow-col {
        grid-template-columns: repeat(3, 1fr);
    }
}
</style>