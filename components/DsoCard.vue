<template>

    <article class="rounded-xl bg-white-200 p-3 shadow-lg hover:shadow-xl hover:transform hover:scale-105 duration-300 ">
      <a href="#">
        <div class="mt-1 p-2">
          <h2 class="text-slate-700">DSO - {{ name }} :</h2>
          <p class="mt-1 text-sm text-slate-400">Available: {{ availability }}</p>
          <span v-if="is_active" class="bg-green-400 text-gray-50 rounded-md px-2">Active</span>
          <span v-else class="bg-red-400 text-gray-50 rounded-md px-2">Inactive</span>

          <div class="mt-3 flex items-end justify-between">
            <p>
              <span class="text-lg font-bold text-blue-500">{{ price }} Kw/h</span>
            </p>

            <div class="flex items-center space-x-1.5 rounded-lg bg-blue-500 px-4 py-1.5 text-white duration-100 hover:bg-blue-600">
<!--                 <svg class="w-8 h-8 hover:text-blue-600 rounded-full hover:bg-gray-100 p-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                </svg> -->
              <button @click="activateDSO" class="text-sm">{{ is_active ? '' : 'Activate' }}</button>
            </div>
          </div>
        </div>
      </a>
    </article>
</template>

<script>
import { postRequest } from '~~/utils/fetchapi';
export default {
    data() {
      return {
        formData: {
          id: '',
        },
        response: ''
      }
    },
    props: {
        // ('id', 'name', 'availability', 'price')
        id: {   //contains address and civic number
            type: String,
            required: true,
        },
        name: {
            type: String,
            required: true,
        },
        availability: {
            type: String,
            required: true,
        },
        price: { 
            type: String,
            required: true,
        },
        is_active: {
            type: String,
            required: true,
        },
    },
    methods: {
        async activateDSO() {
            await postRequest('CPMS', 'api/switchActiveDSO', this.formData)
            // Page refresh
            window.location.reload();
      
        }
    }
}
</script>