<!-- AT THE MOMENT THIS COMPONENT IS NOT USED, MIGHT BE USEFUL AS TEMPLATE FOR LATER, SO IT WILL NOT BE DELETED-->
<template>
<section class="antialiased bg-gray-100 text-gray-600 h-screen px-4">
    <div class="flex flex-col justify-center flex flex-col">
        <!-- Table -->
        <div class="">
            <div class="overflow-x-auto p-3">
                <table class="table-auto w-full" id="ListOfBookings">
                    <thead class="text-xs font-semibold uppercase text-gray-400 bg-gray-50">
                        <tr>
                            <th class="p-2">
                                <div class="font-semibold text-center"></div>
                            </th>
                            <th class="p-2">
                                <div class="font-semibold text-center"></div>
                            </th>
                            <th class="p-2">
                                <div class="font-semibold text-center"></div>
                            </th>
                            <th class="p-2">
                                <div class="font-semibold text-center"></div>
                            </th>
                            <th class="p-2">
                                <div class="font-semibold text-right pl-2"></div>
                            </th>
                        </tr>
                    </thead>
                    <tbody class="text-sm divide-y divide-gray-100">
                        <tr v-for="item in myList" :key="item.id">
                            <td v-text="item[0]" class="font-semibold text-center"></td>
                            <td v-text="item[1]" class="font-semibold text-center"></td>
                            <td v-text="item[2]" class="font-semibold text-center"></td>
                            <td v-text="item[3]" class="font-semibold text-center"></td>
                            <td>
                                <div class="text-center">
                                    <button class="font-semibold" @click="handleClick(item)">
                                        <svg width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16"> 
                                            <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/> <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/> 
                                        </svg>
                                    </button>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>

            

            <div class="flex justify-end">
                <!-- send this data to backend (note: use class 'hidden' to hide this input) -->
                <input type="hidden" class="border border-black bg-gray-50" x-model="selected" />
            </div>
        </div>
    </div>
</section>
</template>

<script>
const jsonData = {
    "Booking1": {
        "Location": "Somma lombardo, via inter 3",
        "Socket": "2",
        "Date": "29/02/2023",
        "Time": "13:30"
    },
    "Booking2": {
        "Location": "value1-1",
        "Socket": "value1-2",
        "Date": "value1-3",
        "Time": "value1-4"
    },
    "Booking3": {
        "Location": "value1-1",
        "Socket": "value1-2",
        "Date": "value1-3",
        "Time": "value1-4"
    }
};

// Extract entries from JSON object
const myList = Object.entries(jsonData).map(([key, value]) => [value.Location, value.Socket, value.Date, value.Time]);
export default {
  data() {
    return {
        myList: myList
    }
  },
  methods:{
    handleClick(item){
        console.log(item)
        //delete
    }
  }
}

</script>

<style>
td:first-child {
  width: 30%; /* 30% for first cell */
}
td:not(:first-child) {
  width: 20%; /* 20% for the rest of cells */
}

td:last-child {
  margin-right: 1rem; /* or any value that works for your design */
  text-align: center;
  color: rgb(145, 39, 39);
}

.pl-2 {
  padding-right: 2rem;  /* makes the rows of the booking table a little bit taller*/
}


tr {
  height: 50px; /* makes the rows of the booking table a little bit taller*/
}


</style>