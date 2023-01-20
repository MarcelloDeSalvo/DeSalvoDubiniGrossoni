<template>
        <div class="booking-container">
          <BookingCardTemplate class="component-class" v-for="(item, index) in items" :key="index" :Street="item.Street" :DateBook="item.Date" :City="item.City"
            :Time="item.Time" :Date="item.Date" :Socket="item.Socket" :Title="item.Title"></BookingCardTemplate>
        </div>
</template>

<script>
/*
the structure of the json is the following
items:[
  {Street:
   City:
   Time:
   Date:
   Socket
   Title:
  },
  {...}
]
*/

//ideally we get the data (complete list of bookings) as a JSON object, parse it, then we can just feed them to the 
let jsonString = '{"items":[{"Street":"Via Napoli 66","City":"Milano","Time":"14:00","Date":"21/02/2022","Socket":"2","Title":"kek"},{"Street":"Via Milan 3","City":"Somma Lombardo","Time":"13:00","Date":"11/02/2022","Socket":"2","Title":"kek"},{"Street":"Via Milan 3","City":"Somma Lombardo","Time":"13:00","Date":"11/02/2022","Socket":"2","Title":"kek"},{"Street":"Via Milan 3","City":"Somma Lombardo","Time":"13:00","Date":"11/02/2022","Socket":"2","Title":"kek"},{"Street":"Via Milan 3","City":"Somma Lombardo","Time":"13:00","Date":"11/02/2022","Socket":"2","Title":"kek"}]}';
let parsedObject = JSON.parse(jsonString);

export default {
  data() {
    return {
      items: parsedObject.items
    }
  },
};


</script>

<style>
/* sets the layout of each card as a grid, default is 4 columns, changes depending on the width of the screen (see settings below)*/
.booking-container {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-template-rows: repeat(3, 1fr);
  grid-column-gap: 0px;
  grid-row-gap: 0px;

}

/* this settings change the number of cards per row based on how wide is the screen, it should never "overflow" on one side*/ 
@media (max-width: 499px) {
    .booking-container {
      grid-template-columns: repeat(1, 1fr);
    }
  }
  @media (min-width: 500px) and (max-width: 819px) {
    .booking-container {
      grid-template-columns: repeat(2, 1fr);
    }
  }
  @media (min-width: 820px) and (max-width: 1120px) {
    .booking-container {
      grid-template-columns: repeat(3, 1fr);
    }
  }
  @media (min-width: 1121px) and (max-width: 1400px) {
    .booking-container {
      grid-template-columns: repeat(4, 1fr);
    }
  }

/* IT CAN HIGHLIGHT THE BORDER OF EACH CARD, HIDDEN DUE TO COLOR SAME AS BG */
  .component-class {
  border: 5px solid rgb(255, 255, 255);
  border-radius: 2%;
  
}

</style>