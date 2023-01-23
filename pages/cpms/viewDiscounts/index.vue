<template>
    <h1 class="text-center text-5xl mt-8 tracking-wide relative">Discounts</h1>
    <div class="grid grid-flow-col mx-64 mt-8 md:mt-16 ">
        <DiscountCard v-for="item in items" :id="item.id" :start_date="item.start_date" :end_date="item.end_date" :discount_amount="item.discount_amount" :applied_stations="item.applied_stations" />
    </div >
    <div class="text-center mt-20">
        <p class="w-full px-3 py-2 mb-3 text-lm leading-tight text-red-700 rounded appearance-none focus:outline-none focus:shadow-outline">
            {{response}}
        </p>
	</div>
</template>

<script>
import { getRequest } from '~~/utils/fetchapi';

export default {
    data() {
        return {
            items: null,
            response: null
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
            let {response, json} = await getRequest('CPMS', 'api/discounts')
            this.items = json
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