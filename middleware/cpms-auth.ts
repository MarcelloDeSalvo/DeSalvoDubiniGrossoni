// to do cpms authentication later to filter normal users from accessing cpow registration.
export default defineNuxtRouteMiddleware(async (to) => {
    // Check if the user is authenticated by calling an API endpoint with nuxt 3's new fetch API
    let isAuthenticated = false

    // Ask the server if the user is authenticated
    isAuthenticated = await checkToken()

    if (!isAuthenticated) {
        // If the user has not a valid token, try to refresh the token
        isAuthenticated = await refreshToken()
    }

    // If the user is not authenticated, redirect to the login page and remove already set cookies
    if (!isAuthenticated) {
        useCookie('tokenCPMS').value = ''
        useCookie('refreshCPMS').value = ''
    }

    const router = useRouter()

    router.beforeResolve((to, from, next) => {
        // If the user is not authenticated, filter out these routes
        if ((to.path == '/cpms/home' || to.path == '/cpms/registerDiscount' || to.path == '/cpms/viewDiscounts' || to.path == '/cpms/viewStationDetails' ) && !isAuthenticated)
            navigateTo('/')

        // If the user is authenticated, filter out this routes
        if (to.path == '/' && isAuthenticated)
            navigateTo('/cpms/home')

        if (to.path == '/cpms/login' && isAuthenticated)
            navigateTo('/cpms/home')
            
        if (to.path == '/cpms/register' && isAuthenticated)
            navigateTo('/cpms/home')

        next()
    });    
})

export async function checkToken() {
    let token = useCookie('tokenCPMS').value
    let config = useRuntimeConfig()
    let serverUrl = config.CPMS_URL


    let resp = await fetch(serverUrl + '/api/isLogged/',
    {
        headers: {
            'Authorization': 'Bearer ' + token
        },
        method: 'POST',
    }).then((res) => {
        return (res.status == 200) ? true : false
    }
    ).catch(() => false)

    return resp
}
  
export async function refreshToken() {
    const refresh = useCookie('refreshCPMS').value
    let config = useRuntimeConfig()
    let serverUrl = config.EMSP_URL

    let resp = await fetch(serverUrl + '/api/token/refresh/',
    { 
        headers: {
            "Content-Type": "application/json",
        },
        method: 'POST',
        body: JSON.stringify({refresh: refresh})
    })
    .then(async (res) => {
       if (res.status == 200){
            const jsonResp = await res.json()
            const token = jsonResp.access
            //console.log(token)
            useCookie('token').value = token
            return true
        } else {
            return false
       }
    })
    .catch(() => false)

    return resp
}