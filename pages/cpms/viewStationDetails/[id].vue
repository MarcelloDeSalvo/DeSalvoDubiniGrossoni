<template>
    <h1 v-text="station.address" class="text-center text-5xl mt-16 tracking-wide relative"></h1>
    <div class="flex mt-4 justify-center items-center">
        <button @click="refreshStation"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full">
            Select automatically the best Energy Providers
        </button>
    </div>
    <div>
        <StationSocketDetail :sockets="station.sockets" />
    </div>
    <div class="text-center mt-20">
        <p
            class="w-full px-3 py-2 mb-3 text-lm leading-tight text-red-700 rounded appearance-none focus:outline-none focus:shadow-outline">
            {{ response }}
        </p>
    </div>
    <h1 class="text-center text-4xl tracking-wide relative">Station Battery</h1>
    <!-- if station.connected_bss is null print something, otherwise display a card-->
    <div v-if="station.connected_bss == null" class="text-center mt-20">
        <p
            class="w-full px-3 py-2 mb-3 text-lm leading-tight text-red-700 rounded appearance-none focus:outline-none focus:shadow-outline">
            No Battery Connected
        </p>
    </div>
    <div v-else>
        <div class="flex mt-12 mb-32 justify-center items-center">
            <BatteryCard :battery="station.connected_bss" />
        </div>
    </div>

    <h1 class="text-center text-4xl mt-16 tracking-wide relative">Energy Providers</h1>
    <div class="grid grid-flow-col mb-32 mx-64 mt-8 md:mt-16 ">
        <DsoCard v-for="dso in station.connected_dsos" :stationId="station.id" :id="dso.id"
            :availability="dso.availability" :name="dso.name" :price="dso.price" :is_active="dso.is_active" />
    </div>
    <h1 class="text-center text-4xl mt-16 tracking-wide relative">Bookings</h1>
    <!-- if station.bookings is null print something, otherwise display a card-->
    <div v-if="bookingLength == 0" class="text-center mt-20">
        <p
            class="w-full px-3 py-2 mb-3 mb-64 text-lm leading-tight text-red-700 rounded appearance-none focus:outline-none focus:shadow-outline">
            No Bookings for this Station
        </p>
    </div>
    <div v-else>
        <div class="grid grid-flow-col mb-64 mt-8 mb-64 md:mt-16 ">
            <BookingCard v-for="booking in station.bookings" :booking="booking" />
        </div>
    </div>
    <h1 class="text-center text-4xl mt-16 tracking-wide relative">Active Discounts</h1>
    <div class="grid grid-flow-col mb-32 mx-64 mt-8 md:mt-16 ">
        <DiscountCard v-for="discount in discounts" :id="discount.id" :start_date="discount.start_date"
            :end_date="discount.end_date" :discount_amount="discount.discount_amount"
            :applied_stations="discount.applied_stations" />
    </div>
</template>

<script>
import { request, getRequestWithToken } from '~~/utils/fetchapi'
export default {
    data() {
        return {
            station: "",
            id: "",
            bookingLength: 0,
            response: "",
            discounts: "",
        }
    },
    setup() {
        definePageMeta({
            middleware: ['cpms-auth'],
            layout: "cpmsnavlayout"
        })
        const route = useRoute()// When accessing /posts/1, route.params.id will be 1

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

                let { response, json } = await getRequestWithToken('CPMS', 'api/getChargingStation/' + this.id + '/')

                this.station = json.station
                this.discounts = json.discounts
                let today = new Date();
                let activeDiscounts = this.discounts.filter(discount => {
                    let start = new Date(discount.start_date);
                    let end = new Date(discount.end_date);
                    return today >= start && today <= end;
                });
                this.discounts = activeDiscounts;


                // append is_active to each dso in the list if station.active_dso == dso.id
                for (let i = 0; i < this.station.connected_dsos.length; i++) {
                    if (this.station.connected_dsos[i].id == this.station.active_dso)
                        this.station.connected_dsos[i].is_active = true
                    else
                        this.station.connected_dsos[i].is_active = false
                }

                // count bookings
                this.bookingLength = this.station.bookings.length


            } catch (error) {
                this.response = error
                console.error(error)
            }
        },
        async refreshStation() {
            try {
                this.id = this.$route.params.id
                console.log("ID", this.id)
                if (this.id == null)
                    throw new Error("No ID provided")

                let { response, json } = await request('PUT', 'CPMS', 'api/selectBestProviderAuto/' + this.id + '/', { "id": this.id })
                if (response.status == 200)
                    this.response = "Best Providers Selected"
                else
                    throw new Error("Error selecting best provider")

                window.location.reload()

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