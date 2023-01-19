<template>
  <div class="flex items-center justify-center p-12">
    <!-- Author: FormBold Team -->
    <!-- Learn More: https://formbold.com -->
    <div class="mx-auto w-full max-w-[550px]">
      <form id="bookingform" method="POST">

        <div class="mb-5">
            <div class="mb-5">
                <label for="stations" class="mb-3 block text-base font-medium text-blue">Select a charging station</label>
                <select v-model="selectedStations" @change="onSelectionStationChange"
                  form="bookingform" id="stations" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-grey-900 dark:focus:ring-blue-500 dark:focus:border-blue-500">
                  <!-- TODO: Generate a list of selection based on the incoming json file from the OCPI-->
                  <option v-for="station in stations" :value="station.address">{{ station.address }}</option>
                </select>
            </div>
            <div class="mb-5">
                <label for="sockets" class="mb-3 block text-base font-medium text-blue">Select a socket</label>
                <select v-model="selectedSockets" @change="onSelectionSocketChange"
                  form="bookingform" id="sockets" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-grey-900 dark:focus:ring-blue-500 dark:focus:border-blue-500">
                  <!-- TODO: Generate a list of selection based on the incoming json file from the OCPI-->
                  <option v-for="socket in selectableSockets" :value="socket.id">{{ socket.id }}</option>
                </select>
            </div>
        </div>

        <div class="-mx-3 flex flex-wrap">
          <div class="w-full px-3 sm:w-1/2">
            <div class="mb-5">
              <label
                for="date"
                class="mb-3 block text-base font-medium text-blue"
              >
                Date
              </label>
              <input
                type="date"
                name="date"
                id="date"
                class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md"
              />
            </div>
          </div>
          <div class="w-full px-3 sm:w-1/2">
            <div class="mb-5">
              <label
                for="time"
                class="mb-3 block text-base font-medium text-blue"
              >
                Time
              </label>
              <input
                type="time"
                name="time"
                id="time"
                class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md"
              />
            </div>
          </div>
        </div>
        <div>
          <button
            type="submit"
            class="hover:shadow-form rounded-md bg-[#6A64F1] py-3 px-8 text-center text-base font-semibold text-white outline-none"
          >
            Submit
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
definePageMeta({
  middleware: ['auth']
})
// Export default data with a sample of the incoming json file from the OCPI, and a method to generate the list of selection for the form
export default {
    data() {
      return {
        selectedStations: null,
        selectableSockets: null,
        selectedSockets: null,

        // Make a JSON example for the OCPI charging stations that contains sockets with their id
        stations: [
          {
            id: 'S1',
            address: 'Station 1 address',
            sockets: [
              {
                id: 'So1',
                status: 'available'
              },
              {
                id: 'So2',
                status: 'unavailable'
              },
              {
                id: 'So3',
                status: 'available'
              }
            ]
          },
          {
            id: 'S2',
            address: 'Station 2 address',
            sockets: [
              {
                id: 'So1',
                status: 'available'
              },
              {
                id: 'So2',
                status: 'available'
              },
              {
                id: 'So3',
                status: 'available'
              }
            ]
          },
          {
            id: 'S3',
            address: 'Station 3 address',
            sockets: [
              {
                id: 'So1',
                status: 'available'
              },
              {
                id: 'So2',
                status: 'available'
              },
              {
                id: 'So3',
                status: 'available'
              }
            ]
          }
        ]
      }
    },
    methods: {
      onSelectionStationChange(e) {
        // Update the selected station and give it also the sockets
        this.selectedStations = e.target.value
        this.selectableSockets = this.stations.find(station => station.address === e.target.value).sockets
        // Filter the sockets that are available
        this.selectableSockets = this.selectableSockets.filter(socket => socket.status === 'available')
        console.log(e.target.value)
      },
      onSelectionSocketChange(e) {
        this.selectedSockets = e.target.value
        console.log(e.target.value)
      }
    }    
}
</script>