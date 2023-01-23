<template>
    <div class='flex items-center justify-center py-10'>
        <a href="/cpms/registerDiscount" class="flex px-3 py-2 bg-blue-400 mr-1 text-white font-semibold rounded">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round"
                    d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
            </svg>
            <span class="ml-1">Add new discount</span>
        </a>

        <a href="/cpms/viewDiscounts" class="flex px-3 py-2 bg-red-400 mr-1 text-white font-semibold rounded">
            <svg fill="none" viewBox="-1 -2 21 21" stroke-width="1.2" stroke="currentColor" class="w-6 h-6">
                <path
                    d="M6.146 7.146a.5.5 0 0 1 .708 0L8 8.293l1.146-1.147a.5.5 0 1 1 .708.708L8.707 9l1.147 1.146a.5.5 0 0 1-.708.708L8 9.707l-1.146 1.147a.5.5 0 0 1-.708-.708L7.293 9 6.146 7.854a.5.5 0 0 1 0-.708z" />
                <path
                    d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zM1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4H1z" />
            </svg>

            <span class="ml-1">View active discount</span>
        </a>
    </div>
    <div class="grid grid-flow-col mx-32 gap-8 mt-8 md:mt-16 ">
        <SimpleCard class="component-class" v-for="station in stations" 
            :StationName="station.id" 
            :Address="station.address" 
            :NumberSockets="station.nSockets" 
            :NumberAvailable="station.AvaliableSockets" 
            :Redirect="'/cpms/viewStationDetails/' + station.id">
        </SimpleCard>
    </div >
</template>

<script>
import { getRequest } from '~~/utils/fetchapi';
export default {
    data() {
        return {
            stations: null,
        }
    },
    setup() {
        definePageMeta({
            middleware: ['auth'],
            layout: "cpmsnavlayout"
        })
    },
    async created() {
        try{
            let {response, json} = await getRequest('CPMS', 'api/getChargingStations')
            this.stations = json
            // count the number of elements inside 'sockets' for each station
            this.stations.forEach(station => {
                station.AvaliableSockets = station.sockets.filter(socket => socket.status == 'Y').length
                station.nSockets = station.sockets.length
            });


        } catch (error) {
            this.response = error
            console.error(error)
        }
    }
};

</script>

<style>
/* sets the layout of each card as a grid, default is 4 columns, changes depending on the width of the screen (see settings below)*/

.grid-flow-col {
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: auto;
  grid-auto-flow: row;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
}

/* this settings change the number of cards per row based on how wide is the screen, it should never "overflow" on one side*/
@media (max-width: 499px) {
    .grid-flow-col {
  grid-template-columns: repeat(1, 1fr);
}
}

@media (min-width: 500px) and (max-width: 819px) {
    .grid-flow-col {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (min-width: 820px) and (max-width: 1120px) {
    .grid-flow-col {
        grid-template-columns: repeat(3, 1fr);
    }
}

/* IT CAN HIGHLIGHT THE BORDER OF EACH CARD, HIDDEN DUE TO COLOR SAME AS BG */

</style>