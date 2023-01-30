<template>
    <div class="overflow-x-auto">
        <div class="min-w-screen mt-12 flex items-center justify-center  font-sans overflow-hidden">
            <div class="w-full lg:w-5/6">
                <div class="bg-white shadow-md rounded my-6">
                    <table class="min-w-max w-full table-auto">
                        <thead>
                            <tr class="bg-gray-200 text-gray-600 uppercase text-sm leading-normal">
                                <th class="p-3 text-center">Socket</th>
                                <th class="p-3 text-center">Type</th>
                                <th class="p-3 text-center">Price</th>
                                <th class="p-3 text-center">Status</th>
                                <th class="p-3 text-center">Book</th>
                                <th class="p-3 text-center">Start Charge</th>
                            </tr>
                        </thead>
                        <tbody class="text-gray-600 text-sm font-light">
                            <tr v-for="socket in sockets" class="border-b border-gray-200 ">
                                <td class="p-3 text-center">{{ socket.id }}</td>
                                <td class="p-3 text-center">{{ socket.type }}</td>
                                <td class="p-3 text-center">{{ socket.price }}</td>
                                <td class="p-3 text-center">
                                    <!-- If ACTIVE make bg-green, otherwise red-->
                                    <span v-if="socket.status === 'Y'"
                                        class="bg-green-400 text-gray-50 rounded-md px-2">Available</span>
                                    <span v-else-if="socket.status === 'C'"
                                        class="bg-orange-400 text-gray-50 rounded-md px-2">Occupied</span>
                                    <span v-else class="bg-red-400 text-gray-50 rounded-md px-2">Unavailable</span>
                                </td>
                                <td class="p-3 text-center">
                                    <button class="button" @click="book(id)">
                                        <svg  width="16" height="16"
                                            fill="currentColor" class="bi bi-bookmark-plus-fill" viewBox="0 0 16 16">
                                            <path fill-rule="evenodd"
                                                d="M2 15.5V2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.74.439L8 13.069l-5.26 2.87A.5.5 0 0 1 2 15.5zm6.5-11a.5.5 0 0 0-1 0V6H6a.5.5 0 0 0 0 1h1.5v1.5a.5.5 0 0 0 1 0V7H10a.5.5 0 0 0 0-1H8.5V4.5z" />
                                        </svg>
                                    </button>
                                </td>
                                <td class="p-3 text-center">
                                    <button class="button" @click="startcharge(socket.id)">
                                        <svg  width="16" height="16"
                                            fill="currentColor" class="bi bi-lightning-fill" viewBox="0 0 16 16">
                                            <path
                                                d="M5.52.359A.5.5 0 0 1 6 0h4a.5.5 0 0 1 .474.658L8.694 6H12.5a.5.5 0 0 1 .395.807l-7 9a.5.5 0 0 1-.873-.454L6.823 9.5H3.5a.5.5 0 0 1-.48-.641l2.5-8.5z" />
                                        </svg>
                                    </button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <div v-if="errorMessage" class="error-mex">{{ errorMessage }}</div>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
export default {
    props: {
        sockets: {
            type: Array,
            required: true,
        },
        stationid: {
            type: String,
            required: true,
        },
    },
    data() {
        return {
            errorMessage: ''
        }
    },
    methods: {
        book(id) {
            this.$router.push('/makebooking/' + this.stationid);
        },
        async startcharge(id) {
            const socketID = {
                "socketID": id
            }
            const result = await postRequestWithToken('emsp', 'OCPI/startCharge', socketID)
            if (result.response.status == 200) {
                console.log(result.json)
                this.$router.push('/chargingStatus/' + result.json.socket)
            }
            else {
                this.errorMessage = result.json
                setTimeout(() => {
                    this.errorMessage = ''
                }, 10000)
            }
            // Page refresh   
        
        },
    },
}
</script>

<style>
.button {
    background-color: #ffffff;
    /* Green */
    border: none;
    color: rgb(0, 0, 0);
    text-align: center;
    text-decoration: none;
    cursor: pointer;
    transition: transform 0.3s;
}

.button:hover {
    transform: scale(1.5);
}

.error-mex {
    color: rgb(211, 0, 0);
    /**set the outside to black */
    font-weight: 600;
    font-size: 15px;
    margin-top: 5px;
    margin-left: 10px;
    margin-right: 10px;
    text-align: right;
}
</style>