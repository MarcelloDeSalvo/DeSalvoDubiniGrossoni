<template>
  <div class="mx-auto flex w-full max-w-sm flex-col">
    <div class="mx-auto flex lg:hidden">
      <NuxtLogo />
    </div>
    <h1 class="mt-8 text-2xl font-semibold text-gray-700 lg:mt-0">
      Welcome back
    </h1>
    <form @submit.prevent="formSubmit" >
      <p class="mt-2 text-sm text-gray-400">Please sign in below</p>
      <p class="mt-5 text-sm font-semibold text-gray-500">Email</p>
      <input class="mt-1 rounded border py-1 px-3 text-sm shadow text-gray-900"
        v-model="formData.email" 
        required/>
      <p class="mt-5 text-sm font-semibold text-gray-500">Password</p>
      <input
        class="mt-1 rounded border py-1 px-3 text-sm text-sm shadow text-gray-900"
        type="password"
        required
        v-model="formData.password"
      />
      <div class="mt-5 flex items-center">
        <input class="mr-2 align-middle text-sm text-sm" type="checkbox" />
        <p class="text-sm font-semibold text-gray-500">Remember me</p>
        <span class="flex-1" />
        <a
          href="#"
          class="text-sm font-semibold text-indigo-400 hover:text-indigo-500"
          >Forgot password?</a
        >
      </div>
      <button
        type ="submit"
        class="mt-5 rounded border bg-indigo-400 py-2 px-5 text-sm text-sm font-semibold text-gray-50 shadow hover:bg-indigo-500"
      >
        Sign in
      </button>

      <div class="mt-8 flex items-center space-x-1">
        <p class="text-sm font-semibold text-gray-500">Don't have an account?</p>
        <a
          href="/register"
          class="text-sm font-semibold text-indigo-400 hover:text-indigo-500"
          >Sign up</a
        >
      </div>
      <div class="mt-5 flex items-center">
        <p class="text-sm font-semibold text-red-500">{{response}}</p>
        <span class="flex-1" />
      </div>
    </form>
  </div>
</template>

<script>
import Cookies from 'js-cookie'

export default {
  data() {
    return {
      formData: {
        email: '',
		    password: ''
      },
      response: ''
    }
  },
  methods: {
    formSubmit() {
        this.formRequest()
        .then((r) => {
            let status = r.response.status
            let json = r.json

            if (status!= 201 && status != 200) {
              // Redirect to home page
              let errors = json
              let error_str = ""
              for (let key in errors) {
                error_str += errors[key] + "\n"
              }
              throw new Error(error_str)
            }

            console.log("Tokens received: ", r.response);
            Cookies.set('token', json.access);
            Cookies.set('refresh', json.refresh);
            document.location.href = "/home";

        }).catch( (error) => {
            // Print every error message by deserializing every json field in response
            this.response = error.message
            console.error('login form could not be sent', error.message)
        });
    },

    async formRequest() {
        let config = useRuntimeConfig()
        let serverUrl = config.BACKEND_URL
        const r = await fetch(serverUrl+"/api/token/", { 
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
          throw new Error("Invalid JSON response - Server error");
        }
    }
	}
}
</script>