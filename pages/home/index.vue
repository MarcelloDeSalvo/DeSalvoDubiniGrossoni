<template>
    <Googlemap />

    <div class="flex flex-col items-center justify-center w-full h-full pt-2 mt-12">
        <h1 class="text-3xl font-bold">Charging Stations</h1>
        <p class="mt-2 text-gray-600">Select a station to make a booking</p>
    </div>
    <div class="grid grid-flow-col  gap-8 mt-4 md:mt-6 ">
        <SimpleCard class="component-class" v-for="station in stations" 
            :StationName="station.id" 
            :Address="station.address" 
            :NumberSockets="station.nSockets" 
            :NumberAvailable="station.AvailableSockets"
            :Redirect="'/stationDetails/' + station.id + '/'"
            >
        </SimpleCard>
    </div >
    <div class="text-center mt-20">
        <p class="w-full px-3 py-2 mb-3 text-lm leading-tight text-red-700 rounded appearance-none focus:outline-none focus:shadow-outline">
            {{response}}
        </p>
	</div> 
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