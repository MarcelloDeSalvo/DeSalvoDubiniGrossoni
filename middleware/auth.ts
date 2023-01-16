import {serverUrl} from "../config";

export default defineNuxtRouteMiddleware(async (to) => {
    // Check if the user is authenticated by calling an API endpoint with nuxt 3's new fetch API
    const isAuthenticated = await fetch(serverUrl + '/isLogged/')
        .then((res) => {
            console.log('res', res)
            return res.json()
        })
        .catch(() => false)

    // If the user is not authenticated
    if (to.path == '/login' && isAuthenticated) {
        // redirect to home page
        return navigateTo('/')
    }

    return true
})
  