<template>


            <div class="border-2 card1 border-gray-50 shadow-lg m-4 p-2">
                <a :href="Redirect" class="leading-10">
                    <div class="flex justify-between items-center">
                        <div>
                            <p class="text-2xl leading-10">Station - {{  StationName }}</p>
                            <p class="text-lg leading-10">N° Sockets: {{ NumberSockets }}</p>
                            <p class="text-lg leading-10">Currently Avaliable: {{ NumberAvailable }}</p>
                        </div>
                        <div>

                            <svg fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
                                class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M2.25 18L9 11.25l4.306 4.307a11.95 11.95 0 015.814-5.519l2.74-1.22m0 0l-5.94-2.28m5.94 2.28l-2.28 5.941" />
                            </svg>

                        </div>
                    </div>
                    <div class="border-t-2 border-white"></div>
                    <div class="flex justify-between items-center">
                        <p class="text-sm leading-10" v-text="Address"></p>
                        <i>
                            <svg fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
                                class="w-4 h-4">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                        </i>
                    </div>
                </a>
            </div>
    

    <!--End Cards-->
</template>

<script>

export default {
    props: {
        StationName: {   //contains address and civic number
            type: String,
            required: true,
        },
        NumberSockets: {
            type: String,
            required: true,
        },
        NumberAvailable: {
            type: String,
            required: true,
        },
        Address: { //Contains the date, Date was already present and might give errors due to ambiguity
            type: String,
            required: true,
        },
        Redirect: {
            type: String,
            required: true,
            default: "/BookingList"
        },
    },
}
</script>

<style>
.card1 {
    border-radius: 20px;
    background-color: #ff9e6d;
    transition: all .3s;
    scale: .98;
    outline: none;
}

.card1:hover {
    border-radius: 20px;
    background: linear-gradient(145deg, #ff9e6d, #e6855c);
    box-shadow: 10px 10px 20px #99593d,
        -5px -5px 10px #ffcf8f;
    scale: 1;
    outline: none;

}
</style>