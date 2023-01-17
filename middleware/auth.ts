import {serverUrl} from "../config";

export default defineNuxtRouteMiddleware(async (to) => {
    // Check if the user is authenticated by calling an API endpoint with nuxt 3's new fetch API
    if (useCookie('token').value == null)
        return

    let isAuthenticated = await checkToken()
    
    // If the user is not authenticated
    if (to.path == '/login' && isAuthenticated)
        document.location.href = '/'
        
    if (to.path == '/register' && isAuthenticated)
        document.location.href = '/'
})

export async function checkToken() {
    const token = useCookie('token').value
    let resp = await fetch(serverUrl + '/api/isLogged/',
    { 
        headers: {
            'Authorization': 'Bearer ' + token
        },
        method: 'POST',
    })
    .then((res) => {
        if (res.status == 200) 
            return true
        else
            return false
    })
    .catch(() => false)

    return resp
}
  