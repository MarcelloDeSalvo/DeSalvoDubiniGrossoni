<template>
    <Googlemap />

    <div class='flex items-center justify-center py-10'>
        <a href="/makebooking/0/" class="flex px-3 py-2 bg-blue-400 mr-1 text-white font-semibold rounded">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round"
                    d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
            </svg>
            <span class="ml-1">Make a booking</span>
        </a>

        <a href="/BookingList" class="flex px-3 py-2 bg-red-400 mr-1 text-white font-semibold rounded">
            <svg fill="none" viewBox="-1 -2 21 21" stroke-width="1.2" stroke="currentColor" class="w-6 h-6">
                <path
                    d="M6.146 7.146a.5.5 0 0 1 .708 0L8 8.293l1.146-1.147a.5.5 0 1 1 .708.708L8.707 9l1.147 1.146a.5.5 0 0 1-.708.708L8 9.707l-1.146 1.147a.5.5 0 0 1-.708-.708L7.293 9 6.146 7.854a.5.5 0 0 1 0-.708z" />
                <path
                    d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zM1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4H1z" />
            </svg>

            <span class="ml-1">Delete a booking</span>
        </a>

        <a href="/BookingList" class="flex px-3 py-2 bg-orange-400 mr-1 text-white font-semibold rounded">
            <svg fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round"
                    d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 012.25-2.25h13.5A2.25 2.25 0 0121 7.5v11.25m-18 0A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75m-18 0v-7.5A2.25 2.25 0 015.25 9h13.5A2.25 2.25 0 0121 11.25v7.5m-9-6h.008v.008H12v-.008zM12 15h.008v.008H12V15zm0 2.25h.008v.008H12v-.008zM9.75 15h.008v.008H9.75V15zm0 2.25h.008v.008H9.75v-.008zM7.5 15h.008v.008H7.5V15zm0 2.25h.008v.008H7.5v-.008zm6.75-4.5h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V15zm0 2.25h.008v.008h-.008v-.008zm2.25-4.5h.008v.008H16.5v-.008zm0 2.25h.008v.008H16.5V15z" />
            </svg>

            <span class="ml-1">See your bookings</span>
        </a>
    </div>
    <div class="grid grid-flow-col  gap-8 mt-8 md:mt-16 ">
        <SimpleCard class="component-class" v-for="station in stations" 
            :StationName="station.id" 
            :Address="station.address" 
            :NumberSockets="station.nSockets" 
            :NumberAvailable="station.AvailableSockets"
            :Redirect="'/makebooking/' + station.id + '/'"
            >
        </SimpleCard>
    </div >   
</template>




<script>
//let jsonString = '{"items":[{"StationName":"Station1", "NumberSockets":"4", "Address":"Via Milano 4, Napoli 69420", "Price":"€40", "CurrentDiscount":"10%"},{"StationName":"Station1", "NumberSockets":"4", "Address":"Via Milano 4, Napoli 69420", "Price":"€40", "CurrentDiscount":"10%"},{"StationName":"Station1", "NumberSockets":"4", "Address":"Via Milano 4, Napoli 69420", "Price":"€40", "CurrentDiscount":"10%"},{"StationName":"Station1", "NumberSockets":"4", "Address":"Via Milano 4, Napoli 69420", "Price":"€40", "CurrentDiscount":"10%"},{"StationName":"Station1", "NumberSockets":"4", "Address":"Via Milano 4, Napoli 69420", "Price":"€40", "CurrentDiscount":"10%"},{"StationName":"Station1", "NumberSockets":"4", "Address":"Via Milano 4, Napoli 69420", "Price":"€40", "CurrentDiscount":"10%"}]}';
export default {
    data() {
        return {
            stations: "",
        }
    },
    setup() {
        definePageMeta({
            middleware: ['auth'],
            layout: "emspnavlayout"
        })
    },
    async created() {
        try{
            let {response, json} = await getRequest('emsp', 'OCPI/getChargingStations')
            this.stations = json
            
            // count the number of elements inside 'sockets' for each station
            this.stations.forEach(station => {
                // count the number of available sockets for each
                station.AvailableSockets = station.sockets.filter(socket => socket.status == 'Y').length
                
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