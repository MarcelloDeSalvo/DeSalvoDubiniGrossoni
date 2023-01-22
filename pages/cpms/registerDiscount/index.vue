<template>
	<div class="flex items-center justify-center p-12">
	  <!-- Author: FormBold Team -->
	  <!-- Learn More: https://formbold.com -->
	  <div class="mx-auto w-full max-w-[550px]">
		<form @submit.prevent="formSubmit" id="bookingform" method="POST">
  
		  <div class="mb-5">
			  <div class="mb-5">
				  <label for="stations" class="mb-3 block text-base font-medium text-blue">Select a charging station</label>
				  <select multiple v-model="stationIDs" required @change="onSelectionStationChange"
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
				  for="initialDate"
				  class="mb-3 block text-base font-medium text-blue"
				>
				  Initial Date
				</label>
				<input
				  v-model = "formData.initialDate"
				  type="date"
				  name="initialDate"
				  id="initialDate"
				  class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md"
				/>
			  </div>
			</div>
			<div class="w-full px-3 sm:w-1/2">
			  <div class="mb-5">
				<label
				  for="finalDate"
				  class="mb-3 block text-base font-medium text-blue"
				>
				  Final Date
				</label>
				<input
				  v-model = "formData.finalDate"
				  type="date"
				  name="finalDate"
				  id="finalDate"
				  class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md"
				/>
			  </div>
			</div>
			<div class="w-full px-3 sm:w-1/2">
				<div class="mb-5">
					<label
					for="amount"
					class="mb-3 block text-base font-medium text-blue"
					>
					Amount
					</label>
					<input
					v-model = "formData.amount"
					type="number" step="0.01"
					name="amount"
					id="amount"
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
			stationID: null,
			initialDate: null,
			finalDate: null,
			amount: null
		  },
  
		  response: null,
  
		  // Make a JSON example for the OCPI charging stations that contains sockets with their id
		  stations: [
			{
			  id: 'S1',
			  cpmsID: 'CPMS1',
			  address: 'Station 1 address',
			  sockets: [
				{
				  id: 'So1',
				  status: 'available'
				},
				{
				  id: 'So2',
				  status: 'unavailable'
				},
				{
				  id: 'So3',
				  status: 'available'
				}
			  ]
			},
			{
			  id: 'S2',
			  address: 'Station 2 address',
			  cpmsID: 'CPMS2',
			  sockets: [
				{
				  id: 'So1',
				  status: 'available'
				},
				{
				  id: 'So2',
				  status: 'available'
				},
				{
				  id: 'So3',
				  status: 'available'
				}
			  ]
			},
			{
			  id: 'S3',
			  address: 'Station 3 address',
			  cpmsID: 'CPMS13',
			  sockets: [
				{
				  id: 'So1',
				  status: 'available'
				},
				{
				  id: 'So2',
				  status: 'available'
				},
				{
				  id: 'So3',
				  status: 'available'
				}
			  ]
			}
		  ]
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
			  document.location.href = "/BookingList"
  
			}).catch((error) => {
			  console.log(error.message)
			  this.response = error.message
			})
		},
  
		async formRequest() {
		  let config = useRuntimeConfig()
		  let serverUrl = config.BACKEND_URL
		  let token = useCookie('token').value
		  const r = await fetch(serverUrl+"/api/registerbooking/", { 
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
  
  }
  </script>