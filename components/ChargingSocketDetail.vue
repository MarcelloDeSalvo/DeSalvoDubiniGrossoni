<template>
    <div class="overflow-x-auto">
        <div class="min-w-screen mt-12 flex items-center justify-center font-sans overflow-hidden">
            <div class="w-full lg:w-5/6">
                <div class="bg-white shadow-md rounded my-6">
                    <table class="min-w-max w-full table-auto">
                        <thead>
                            <tr class="bg-gray-200 text-gray-600 uppercase text-sm leading-normal">
                                <th class="p-3 text-center">Socket</th>
                                <th class="p-3 text-center">Speed</th>
                                <th class="p-3 text-center">Price</th>
                                <th class="p-3 text-center">Status</th>
                            </tr>
                        </thead>
                        <tbody class="text-gray-600 text-sm font-light">
                            <tr class="border-b border-gray-200 hover:bg-gray-100">
                                <td class="p-3 text-center">{{ ChargeSocket.id }}</td>
                                <td class="p-3 text-center">{{ ChargeSocket.type }}</td>
                                <td class="p-3 text-center">{{ ChargeSocket.price }}</td>
                                <td class="p-3 text-center">
                                    <!-- If ACTIVE make bg-green, otherwise red-->
                                    <span v-if="ChargeSocket.status === 'C'"
                                        class="bg-green-400 text-gray-50 rounded-md px-2">Charging</span>
                                    <span v-else class="bg-red-400 text-gray-50 rounded-md px-2">Finished
                                        Charging</span>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
export default {
    props: {
        ChargeSocket: {
            type: Object,
            required: true,
        },
    },
}
</script>

<style>
    /* default styles */
    .table-header {
        background-color: #ddd;
    }

    /* styles for small screens */
    @media (max-width: 768px) {
        .table-header {
            display: flex;
            width: 100%;
        }

        .table-header th {
            width: 100%;
            display: block;
        }
    }
</style>