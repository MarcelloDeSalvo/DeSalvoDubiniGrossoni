<template>


            <div class="border-2 card1 border-gray-50 shadow-lg m-4 p-2">
                <a :href="Redirect" class="leading-10">
                    <div class="flex justify-between items-center">
                        <div>
                            <p class="text-2xl leading-10">Station - {{  StationName }}</p>
                            <p class="text-lg leading-10">N° Sockets: {{ NumberSockets }}</p>
                            <p class="text-lg leading-10">Currently Avaliable: {{ NumberAvailable }}</p>
                        </div>
                    
                    </div>
                    <div class="border-t-2 border-white"></div>
                    <div class="flex justify-between items-center">
                        <p class="text-sm leading-10" v-text="Address"></p>
                        <i>
                            <svg  width="17" height="17" fill="currentColor" class="bi bi-pin-map-fill" viewBox="1 -2 18 18">
                                <path fill-rule="evenodd" d="M3.1 11.2a.5.5 0 0 1 .4-.2H6a.5.5 0 0 1 0 1H3.75L1.5 15h13l-2.25-3H10a.5.5 0 0 1 0-1h2.5a.5.5 0 0 1 .4.2l3 4a.5.5 0 0 1-.4.8H.5a.5.5 0 0 1-.4-.8l3-4z"/> <path fill-rule="evenodd" d="M4 4a4 4 0 1 1 4.5 3.969V13.5a.5.5 0 0 1-1 0V7.97A4 4 0 0 1 4 3.999z"/>
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
            //set type to int
            type: Number,
            required: true,
        },
        NumberSockets: {
            type: Number,
            required: true,
        },
        NumberAvailable: {
            type: Number,
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
    background-color: #ffab91;
    transition: all .3s;
    scale: .98;
    outline: none;
}

.card1:hover {
    border-radius: 20px;
    background: linear-gradient(145deg, #ff8a65, #e6855c);
    box-shadow: 7px 7px 2px #99593d,
        -5px -5px 2px #ffcf8f;
    scale: 1;
    outline: none;

}
</style>