<template>
    <article class="rounded-xl bg-white-200 p-3 shadow-lg hover:shadow-xl hover:transform hover:scale-105 duration-300 ">
        <div class="mt-1 p-2">
          <h2 class="text-slate-700">User: {{ booking.user }}</h2>
          <p class="mt-1 text-sm text-slate-400">Id: {{ booking.id }}</p>
          <p class="mt-1 text-sm text-slate-400">Station: {{ booking.chargingStation }}</p>
          <p class="mt-1 text-sm text-slate-400">Socket: {{ booking.socket }}</p>
          <p class="mt-1 text-sm text-slate-400">Date: {{ booking.date }}</p>
          <p class="mt-1 text-sm text-slate-400">Time: {{ booking.time }}</p>
        </div>
    </article>
</template>

<script>
export default {
    // fields: ( 'user', 'station ', 'socket', 'date', 'time' ),
    props: {
        booking: {
            type: Object,
            required: true,
        }
    },    
}
</script>
