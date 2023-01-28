<template>
    <div tabindex="0" class="focus:outline-none bg-color flex">
        <div class="mx-auto container py-8">
            <div class="flex flex-wrap items-center lg:justify-between ">
                <!-- CARD TEMPLATE -->
                <div tabindex="0" class="focus:outline-none mx-2 w-72 xl:mb-0 mb-8">

                    <div class="bg-white">
                        <div class="flex items-center justify-between px-4 pt-4 bg-color">
                        </div>
                        <div class="p-4 bg-color">
                            <div class="flex items-center">
                                <h2 tabindex="0" class="focus:outline-none text-lg font-semibold" v-text="Title"></h2>
                            </div>
                            <p tabindex="0" class="focus:outline-none text-xs text-gray-600 mt-2" v-text="Street"></p>
                            <p tabindex="0" class="focus:outline-none text-xs text-gray-600 mt-2" v-text="Socket"></p>
                            <div class="flex mt-4">
                                <div>
                                    <p tabindex="0"
                                        class="focus:outline-none text-xs text-gray-600 px-2 bg-gray-200 py-1 " v-text="DateBook">
                                        </p>
                                </div>
                                <div class="pl-2">
                                    <p tabindex="0"
                                        class="focus:outline-none text-xs text-gray-600 px-2 bg-gray-200 py-1 "
                                        v-text="Time"></p>
                                </div>
                                <div class="pl-2">
                                    <button class="font-semibold" @click="handleClick1(BookingID)">
                                        <svg width="16" height="16" fill="#cc0000" class="bi bi-trash" 
                                            viewBox="0 0 16 16">
                                            <path
                                                d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z" />
                                            <path fill-rule="evenodd"
                                                d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z" />
                                        </svg>
                                    </button>
                                    <button class=" " @click="handleClick2(BookingID)" style="margin-left: 20px;">
                                    <svg width="16" height="16" fill="#fff176" stroke="#f9a825" class="bi bi-lightning-charge-fill" viewBox="0 0 16 16"> <path d="M11.251.068a.5.5 0 0 1 .227.58L9.677 6.5H13a.5.5 0 0 1 .364.843l-8 8.5a.5.5 0 0 1-.842-.49L6.323 9.5H3a.5.5 0 0 1-.364-.843l8-8.5a.5.5 0 0 1 .615-.09z"/> </svg>
                                </button>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
                <!-- END TEMPLATE -->
            </div>
        </div>
    </div>
</template>

<script>

import {deleteRequestWithToken} from '~~/utils/fetchapi'
import {postRequestWithToken} from '~~/utils/fetchapi'
const BookDate = "" //placeholder
export default {
    props: {
        BookingID: {
            type: Number,
            required: true,
        },
        Street: {
            type: String,
            required: true,
        },
        DateBook: {
            type: String,
            required: true,
        },
        Time: {
            type: String,
            required: true,
        },
        Socket: {
            type: String,
            required: true,
        },
        Title: {
            type: String,
            required: true,
        },
    },
    methods: {
        async handleClick1(BookingID) {
            await deleteRequestWithToken('emsp', 'api/removeBooking', BookingID)
            // Page refresh
            window.location.reload();
        },
        async handleClick2(BookingID) {
            const id={
                "id": BookingID
            }
            await postRequestWithToken('emsp', 'OCPI/startChargingFromBooking', id)
            // Page refresh
            
        }
        
    },
    
}
</script>

<style>
/* IF NEEDED IT CAN CHANGE THE WHOLE "CARD" BACKGROUND-COLOR, IT'S NOT PRESENT FOR THE DATE AND TIME SECTION */
.bg-color {
  background-color: rgb(255, 255, 255);
}
</style>