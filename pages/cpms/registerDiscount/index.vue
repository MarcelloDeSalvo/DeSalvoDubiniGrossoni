<template>
	<div class="flex items-center justify-center p-12">
	  <!-- Author: FormBold Team -->
	  <!-- Learn More: https://formbold.com -->
	  <div class="mx-auto w-full max-w-[550px]">
		<form @submit.prevent="formSubmit" id="bookingform" method="POST">
  
		  <div class="mb-5">
			  <div class="mb-5">
				  <label for="stations" class="mb-3 block text-base font-medium text-blue">Select a charging station</label>
				  <select multiple v-model="formData.applied_stations" required @change="onSelectionStationChange"
					form="bookingform" id="stations" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-grey-900 dark:focus:ring-blue-500 dark:focus:border-blue-500">
					<!-- TODO: Generate a list of selection based on the incoming json file from the OCPI-->
					<option v-for="station in stations" :value="station.id">{{ station.address }}</option>
				  </select>
			  </div>
		  </div>

		  <div class="-mx-3 flex flex-wrap">
			<div class="w-full px-3 sm:w-1/2">
			  <div class="mb-5">
				<label
				  for="start_date"
				  class="mb-3 block text-base font-medium text-blue"
				>
				  Initial Date
				</label>
				<input
				  v-model = "formData.start_date"
				  type="date"
				  name="start_date"
				  id="start_date"
				  class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md"
				/>
			  </div>
			</div>
			<div class="w-full px-3 sm:w-1/2">
			  <div class="mb-5">
				<label
				  for="end_date"
				  class="mb-3 block text-base font-medium text-blue"
				>
				  Final Date
				</label>
				<input
				  v-model = "formData.end_date"
				  type="date"
				  name="end_date"
				  id="end_date"
				  class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md"
				/>
			  </div>
			</div>
			<div class="w-full px-3 sm:w-1/2">
				<div class="mb-5">
					<label
					for="discount_amount"
					class="mb-3 block text-base font-medium text-blue"
					>
					discount_amount
					</label>
					<input
					v-model = "formData.discount_amount"
					type="number"
					name="discount_amount"
					id="discount_amount"
					class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md"
					/>
				</div>
			</div>
	
		  </div>
		  <div>
			<button
			  type="submit"
			  class="hover:shadow-form rounded-md bg-[#6A64F1] py-3 px-8 text-center text-base font-semibold text-white outline-none"
			>
			  Submit
			</button>
			<div class="text-center mt-20">
				<p class="w-full px-3 py-2 mb-3 text-lm leading-tight text-red-700 rounded appearance-none focus:outline-none focus:shadow-outline">
					{{response}}
				</p>
			</div>
		  </div>
		</form>

	  </div>
	</div>
  </template>
  
  <script>
  definePageMeta({
	middleware: ['auth']
  })
  // Export default data with a sample of the incoming json file from the OCPI, and a method to generate the list of selection for the form
  export default {
	  data() {
		return {
		  stationIDs: null,
  
		  formData: {
			applied_stations: null,
			start_date: null,
			end_date: null,
			discount_amount: null
		  },
  
		  response: null,

  		  stations: null,

		}
	  },
  
	  methods: {
		onSelectionStationChange(e) {
		  console.log(e.target.value)
		},
  
		formSubmit() {
  
		  this.formRequest()
			.then((r) => {
			  let status = r.response.status
			  let json = r.json
  
			  if (status!= 201 && status != 200) {
				let errors = json
				let error_str = ""
				for (let key in errors) {
				  error_str += errors[key] + "\n"
				}
				throw new Error(error_str)
			  }
  
			  this.response = "Account created successfully"
			  document.location.href = "/cpms/viewDiscounts"
  
			}).catch((error) => {
			  console.log(error.message)
			  this.response = error.message
			})
		},
  
		async formRequest() {
		  let config = useRuntimeConfig()
		  let serverUrl = config.CPMS_URL
		  let token = useCookie('token').value
		  const r = await fetch(serverUrl+"/api/registerDiscount/", { 
			headers: {
			  "Content-Type": "application/json",
			  'Authorization': 'Bearer ' + token
			},
			method: 'POST',
			body: JSON.stringify(this.formData)
		  } );
  
		  try{
			const json = await r.json()
			return { response: r, json: json }
		  }catch(e){
			throw new Error("Invalid JSON response - Server Error");
		  }
	  	}	
	},
	async created() {
        try{
            let {response, json} = await getRequest('CPMS', 'api/getChargingStations')
            this.stations = json
        } catch (error) {
            this.response = error
            console.error(error)
        }
    }
  
  }
  </script>