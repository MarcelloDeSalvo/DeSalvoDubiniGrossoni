<template>
  <article class="rounded-xl bg-white p-3 shadow-lg hover:shadow-xl hover:transform hover:scale-105 duration-300 ">
    <a href="#">
      <div class="mt-1 p-2 styling">
        <h2 class="text-slate-700">Discount - {{ id }} :</h2>
        <p class="mt-1 text-sm text-slate-400">Start: {{ start_date }}</p>
        <p class="mt-1 text-sm text-slate-400">End: {{ end_date }}</p>

        <p>
          <span class="text-lg  font-bold text-blue-500 text-center">{{ discount_amount }}%</span>
        </p>

      </div>
    </a>
  </article>
</template>

<script>

export default {
  props: {
    id: {   //contains address and civic number
      type: Number,
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
      type: Number,
      required: true,
    },
  },

}
</script>

<style>
.styling {
  text-align: center;
  align-items: center;
}

.text-center {
  text-align: center;
}
</style>