<template>
  <div class="booking-container">
    <BookingCardTemplate class="component-class" v-for="(item, index) in items" :key="index" :Street="item.stationAddress"
      :DateBook="item.date"  :Time="item.time" :Date="item.date" :Socket="item.socketID" :BookingID="item.id"
      :Title="item.stationID"></BookingCardTemplate>
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


import { getRequest } from '~~/utils/fetchapi'
export default {
  data() {
    return {
      items: null,
    }
  },
  async created() {

    let config = useRuntimeConfig()
    let serverUrl = config.EMSP_URL
    let token = useCookie('token').value
    const r = await fetch(serverUrl + "/api/getBookings", {
      headers: {
        "Content-Type": "application/json",
        'Authorization': 'Bearer ' + token
      },
      method: 'GET',
    });

    try {
      const json = await r.json()
      this.items = json
      //for each address in items, add a string in front of it
      this.items.forEach(item => {
        item.stationAddress = "Indirizzo: " + item.stationAddress
      });
      //for each stationID in items, change it with an increasing number
      this.items.forEach(item => {
        item.stationID = this.items.indexOf(item) + 1
      });
      //add booking in front of each station ID in items
      this.items.forEach(item => {
        item.stationID = "Booking number " + item.stationID
      });
      //for each socketID in items, add a string in front of it
      this.items.forEach(item => {
        item.socketID = "Socket number: " + item.socketID
      });
      console.log(this.items)
    } catch (e) {
      throw new Error("Invalid JSON response - Server Error");
    }


  },
};


</script>

<style>
/* sets the layout of each card as a grid, default is 4 columns, changes depending on the width of the screen (see settings below)*/
.booking-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: auto;
  grid-auto-flow: row;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
 /* leave margin on the left and right of the grid */
  margin-left: 10%;
  margin-right: 10%;

}

/* this settings change the number of cards per row based on how wide is the screen, it should never "overflow" on one side*/
@media (max-width: 499px) {
  .booking-container {
    grid-template-columns: repeat(1, 1fr);
  }
}

@media (min-width: 500px) and (max-width: 819px) {
  .booking-container {
    grid-template-columns: repeat(1, 1fr);
  }
}

@media (min-width: 820px) and (max-width: 1120px) {
  .booking-container {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1121px) and (max-width: 1400px) {
  .booking-container {
    grid-template-columns: repeat(3, 1fr);
  }
}

/* IT CAN HIGHLIGHT THE BORDER OF EACH CARD, HIDDEN DUE TO COLOR SAME AS BG */
.component-class {
  border: 5px solid rgb(255, 255, 255);
  border-radius: 2%;

}
</style>