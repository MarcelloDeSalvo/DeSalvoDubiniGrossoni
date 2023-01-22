<template>
    <div class="overflow-x-auto">
        <div class="min-w-screen mt-12 bg-gray-100 flex items-center justify-center bg-gray-100 font-sans overflow-hidden">
            <div class="w-full lg:w-5/6">
                <div class="bg-white shadow-md rounded my-6">
                    <table class="min-w-max w-full table-auto">
                        <thead>
                            <tr class="bg-gray-200 text-gray-600 uppercase text-sm leading-normal">
                                <th class="p-3 text-center">Socket</th>
                                <th class="p-3 text-center">Type</th>
                                <th class="p-3 text-center">Price</th>
                                <th class="p-3 text-center">Status</th>
                            </tr>
                        </thead>
                        <tbody class="text-gray-600 text-sm font-light">
                            <tr v-for="socket in sockets" class="border-b border-gray-200 hover:bg-gray-100">
                                <td class="p-3 text-center">{{ socket.id }}</td> 
                                <td class="p-3 text-center">{{ socket.type }}</td>
                                <td class="p-3 text-center">{{ socket.price }}</td>
                                <td class="p-3 text-center">
                                    <!-- If ACTIVE make bg-green, otherwise red-->
                                    <span v-if="socket.status === 'Available'" class="bg-green-400 text-gray-50 rounded-md px-2">{{ socket.status }}</span>
                                    <span v-else class="bg-red-400 text-gray-50 rounded-md px-2">{{ socket.status }}</span>
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
        sockets: {
            type: Array,
            required: true,
            default: () => [
              {
                id: '1',
                type: 'Fast',
                price: '100',
                status: 'Available',
              },
              {
                id: '2',
                type: 'Slow',
                price: '200',
                status: 'Unavailable',
              }
            ],
        },
    },
}
</script>