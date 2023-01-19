
<template>
<section class="antialiased bg-gray-100 text-gray-600 h-screen px-4">
    <div class="flex flex-col justify-center flex flex-col">
        <!-- Table -->
        <div class="">
            <header class="px-5 py-4 border-b border-gray-100">
                <div class="font-semibold text-gray-800">Manage Carts</div>
            </header>

            <div class="overflow-x-auto p-3">
                <table class="table-auto w-full">
                    <thead class="text-xs font-semibold uppercase text-gray-400 bg-gray-50">
                        <tr>
                            <th></th>
                            <th class="p-2">
                                <div class="font-semibold text-left">Location</div>
                            </th>
                            <th class="p-2">
                                <div class="font-semibold text-left">Socket</div>
                            </th>
                            <th class="p-2">
                                <div class="font-semibold text-left">Date - Time</div>
                            </th>
                            <th class="p-2">
                                <div class="font-semibold text-center">Delete</div>
                            </th>
                        </tr>
                    </thead>

                    <tbody class="text-sm divide-y divide-gray-100">
                        <!-- record 1 -->
                        <tr>
                            <td class="p-2">
                            </td>
                            <td class="p-2">
                                <div class="font-medium text-gray-800">
                                    Samsung Galaxy Note 4
                                </div>
                            </td>
                            <td class="p-2">
                                <div class="text-left">1</div>
                            </td>
                            <td class="p-2">
                                <div class="text-left font-medium text-green-500">
                                    RM 2,890.66
                                </div>
                            </td>
                            <td class="p-2">
                                <div class="flex justify-center">
                                    <button>
                                        <svg class="w-8 h-8 hover:text-blue-600 rounded-full hover:bg-gray-100 p-1"
                                            fill="none" stroke="currentColor" viewBox="0 0 24 24"
                                            xmlns="http://www.w3.org/2000/svg">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16">
                                            </path>
                                        </svg>
                                    </button>
                                </div>
                            </td>
                        </tr>

                        <!-- record 2 -->
                        <tr>
                            <td class="p-2">
                            </td>
                            <td class="p-2">
                                <div>
                                    <div class="font-medium text-gray-800">Logitech Keyboard</div>
                                </div>
                            </td>
                            <td class="p-2">
                                <div class="text-left">1</div>
                            </td>
                            <td class="p-2">
                                <div class="text-left font-medium text-green-500">
                                    RM 120.50
                                </div>
                            </td>
                            <td class="p-2">
                                <div class="flex justify-center">
                                    <button>
                                        <svg class="w-8 h-8 hover:text-blue-600 rounded-full hover:bg-gray-100 p-1"
                                            fill="none" stroke="currentColor" viewBox="0 0 24 24"
                                            xmlns="http://www.w3.org/2000/svg">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16">
                                            </path>
                                        </svg>
                                    </button>
                                </div>
                            </td>
                        </tr>

                        <!-- record 3 -->
                        <tr>
                            <td class="p-2">
                            </td>
                            <td class="p-2">
                                <div>
                                    <div class="font-medium text-gray-800">Earphone</div>
                                </div>
                            </td>
                            <td class="p-2">
                                <div class="text-left">1</div>
                            </td>
                            <td class="p-2">
                                <div class="text-left font-medium text-green-500">RM 15.00</div>
                            </td>
                            <td class="p-2">
                                <div class="flex justify-center">
                                    <button>
                                        <svg class="w-8 h-8 hover:text-blue-600 rounded-full hover:bg-gray-100 p-1"
                                            fill="none" stroke="currentColor" viewBox="0 0 24 24"
                                            xmlns="http://www.w3.org/2000/svg">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16">
                                            </path>
                                        </svg>
                                    </button>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- total amount -->
            <div class="flex justify-end font-bold space-x-4 text-2xl border-t border-gray-100 px-5 py-4">
                <div>Total</div>
                <div class="text-blue-600">RM <span x-text="total.toFixed(2)"></span></div>
            </div>

            <div class="flex justify-end">
                <!-- send this data to backend (note: use class 'hidden' to hide this input) -->
                <input type="hidden" class="border border-black bg-gray-50" x-model="selected" />
            </div>
        </div>
    </div>
</section>
</template>

