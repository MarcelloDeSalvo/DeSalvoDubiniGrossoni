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
						<h3 class="pt-4 text-2xl text-center">Create an Account!</h3>
						<form  @submit.prevent="formSubmit" class="px-8 pt-6 pb-8 mb-4 bg-white rounded">
							<div class="mb-4 md:flex md:justify-between">
								<div class="mb-4 md:mr-2 md:mb-0">
									<label class="block mb-2 text-sm font-bold text-gray-700" for="firstName">
										First Name
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
										Last Name
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
									Email
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
										class="w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border border-red-500 rounded shadow appearance-none focus:outline-none focus:shadow-outline"
										required v-model="formData.password"
										type="password"
										placeholder="******************"
									/>
									<p class="text-xs italic text-red-500">Please choose a password.</p>
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
									class="w-full px-4 py-2 font-bold text-white bg-blue-500 rounded-full hover:bg-blue-700 focus:outline-none focus:shadow-outline"
									type="submit"
								>
									Register Account
								</button>
							</div>
							<hr class="mb-6 border-t" />
							<div class="text-center">
								<a
									class="inline-block text-sm text-blue-500 align-baseline hover:text-blue-800"
									href="#"
								>
									Forgot Password?
								</a>
							</div>
							<div class="text-center">
								<a
									class="inline-block text-sm text-blue-500 align-baseline hover:text-blue-800"
									href="/login"
								>
									Already have an account? Login!
								</a>
							</div>
							<div class="text-center">
								<p>
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
import {ref} from "vue";
import {serverUrl} from "../../config";
definePageMeta({
    middleware: ['auth']
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
        this.formRequest().then( (result) => {
			// Success
            console.log(result)
			if (result.status != 201)
				throw new Error(result.statusText)
			
			this.response = result.statusText
			window.location.href = "/login"
			
        }).catch( (error) => {
			this.response = error
            console.error('Registration form could not be sent', error)
        });
    },

    async formRequest() {
			return await fetch(serverUrl+"/api/register/", { 
				headers: {
					"Content-Type": "application/json",
				},
				method: 'POST',
				body: JSON.stringify(this.formData)
			} );
    	}	
	}
}
</script>