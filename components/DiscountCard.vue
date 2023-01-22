<template>
    <article class="rounded-xl bg-white p-3 shadow-lg hover:shadow-xl hover:transform hover:scale-105 duration-300 ">
      <a href="#">
        <div class="mt-1 p-2">
          <h2 class="text-slate-700">Discount - {{ id }} :</h2>
          <p class="mt-1 text-sm text-slate-400">Start: {{ start_date }}</p>
          <p class="mt-1 text-sm text-slate-400">End: {{ end_date }}</p>

          <!-- Loop every station inside applied_stations and print their ID-->
          <p class="mt-1 text-sm text-slate-400">Stations: </p>
          <p v-for="station in applied_stations" class="mt-1 text-sm text-slate-400"> - ID: {{ station }}</p>
          
          <div class="mt-3 flex items-end justify-between">
            <p>
              <span class="text-lg font-bold text-blue-500">{{ discount_amount }}%</span>
            </p>

            <div class="flex items-center space-x-1.5 rounded-lg bg-blue-500 px-4 py-1.5 text-white duration-100 hover:bg-blue-600">
                <svg class="w-8 h-8 hover:text-blue-600 rounded-full hover:bg-gray-100 p-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                </svg>

              <button class="text-sm">Delete</button>
            </div>
          </div>
        </div>
      </a>
    </article>
</template>

<script>
export default {
    props: {
        id: {   //contains address and civic number
            type: String,
            required: true,
        },
        start_date: {
            type: String,
            required: true,
        },
        end_date: {
            type: String,
            required: true,
        },
        discount_amount: { 
            type: String,
            required: true,
        },
        applied_stations: {
            type: String,
            required: true,
        },
    },
}
</script>