<template>
    <div class="font-semibold">
		<!-- Container -->
		<div class="container mx-auto">
			<div class="flex justify-center px-6 my-12">
				<!-- Row -->
				<div class="w-full xl:w-3/4 lg:w-11/12 flex">
					<!-- Col -->
					<div
						class="w-full h-auto bg-gray-400 hidden lg:block lg:w-5/12 bg-cover rounded-l-lg"
						style="background-image: url('https://source.unsplash.com/Mv9hjnEUHR4/600x800')"
					></div>
					<!-- Col -->
					<div class="w-full lg:w-7/12 bg-white p-5 rounded-lg lg:rounded-l-none">
						<h3 class="pt-4 text-2xl text-center">This page would admin only</h3>
						<h3 class="pt-4 text-1xl text-center">(accessible just for the demo)</h3>
						<form  @submit.prevent="formSubmit" class="px-8 pt-6 pb-8 mb-4 bg-white rounded">
							<div class="mb-4 md:flex md:justify-between">
								<div class="mb-4 md:mr-2 md:mb-0">
									<label class="block mb-2 text-sm font-bold text-gray-700" for="firstName">
										CPOW first Name
									</label>
									<input
										class="w-full px-3 py-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
										required v-model="formData.first_name"
										type="text"
										placeholder="First Name"
									/>
								</div>
								<div class="md:ml-2">
									<label class="block mb-2 text-sm font-bold text-gray-700" for="lastName">
										CPOW last Name
									</label>
									<input
										class="w-full px-3 py-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
										required v-model="formData.last_name"
										type="text"
										placeholder="Last Name"
									/>
								</div>
							</div>
							<div class="mb-4">
								<label class="block mb-2 text-sm font-semibold text-gray-700" for="email">
									Institutional email
								</label>
								<input
									class="w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
									required v-model="formData.email"
									type="email"
									placeholder="Email"
								/>
							</div>
							<div class="mb-4 md:flex md:justify-between">
								<div class="mb-4 md:mr-2 md:mb-0">
									<label class="block mb-2 text-sm font-bold text-gray-700" for="password">
										Password
									</label>
									<input
										class="w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
										required v-model="formData.password"
										type="password"
										placeholder="******************"
									/>
							
								</div>
								<div class="md:ml-2">
									<label class="block mb-2 text-sm font-bold text-gray-700" for="c_password">
										Confirm Password
									</label>
									<input
										class="w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
										required v-model="formData.password2"
										type="password"
										placeholder="******************"
									/>
								</div>
							</div>
							<div class="mb-6 text-center submit">
								<button
									class="w-full px-4 py-2 font-bold text-white bg-orange-500 rounded-full hover:bg-orange-500 focus:outline-none focus:shadow-outline"
									type="submit"
								>
									Register Account
								</button>
							</div>
							<hr class="mb-6 border-t" />
							<div class="text-center">
								<p class="w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 rounded shadow appearance-none focus:outline-none focus:shadow-outline">
									{{response}}
								</p>
							</div>
						</form>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>
  
<script>
definePageMeta({
    middleware: ['cpms-auth'],
	layout: "cpmsnavlayout"
})
export default {
  data() {
    return {
      formData: {
		first_name:'',
        last_name: '',
        email: '',
		password: '',
		password2: ''
      },
	  response: "" 
    }
  },
  methods: {
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
			document.location.href = "/cpms/login"

		}).catch((error) => {
			console.log(error.message)
			this.response = error.message
		})
    },

    async formRequest() {
		let config = useRuntimeConfig()
		let serverUrl = config.CPMS_URL
		const r = await fetch(serverUrl+"/api/register/", { 
			headers: {
				"Content-Type": "application/json",
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
  }
}
</script>