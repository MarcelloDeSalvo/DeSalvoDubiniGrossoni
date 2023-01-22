<template>
    <h1 class="text-center text-5xl mt-8 tracking-wide relative">Discounts</h1>
    <div class="grid grid-flow-col mx-64 mt-8 md:mt-16 ">
        <DiscountCard v-for="item in items" :key="item.discountID" :discountID="item.discountID" :start_date="item.start_date" :end_date="item.end_date" :discount_amount="item.discount_amount" :applied_stations="item.applied_stations" />
    </div >   
</template>

<script>
let jsonString = '{"items":[{"discountID":"1", "start_date":"4/4/4", "end_date":"5/5/5", "discount_amount":"10%", "applied_stations" : [{"station_id": "1"}, {"station_id":"2"}]}, {"discountID":"1", "start_date":"4/4/4", "end_date":"5/5/5", "discount_amount":"30%", "applied_stations" : [{"station_id": "1"}, {"station_id":"2"}]}]}';
let parsedObject = JSON.parse(jsonString);
export default {
    data() {
        return {
            items: parsedObject.items
        }
    },
    setup() {
        definePageMeta({
            middleware: ['auth']
        })
    }
};
</script>

<style>
/* sets the layout of each card as a grid, default is 4 columns, changes depending on the width of the screen (see settings below)*/
.grid-flow-col {
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: auto;
  grid-auto-flow: row;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
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
</style>