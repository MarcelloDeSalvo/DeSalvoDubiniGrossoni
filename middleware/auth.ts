export default defineNuxtRouteMiddleware(async (to) => {
    

    // Check if the user is authenticated by calling an API endpoint with nuxt 3's new fetch API
    let isAuthenticated = false

/*     //If the user has a token, but the token is invalid, try to refresh the token
    if (useCookie('token').value != null) {
        isAuthenticated = await refreshToken()
        if (!isAuthenticated){
            const tokenCookie = useCookie('token')
            tokenCookie.value = null
        }
    } */
    
    // Ask the server if the user is authenticated
    isAuthenticated = await checkToken()

    const router = useRouter()

    router.beforeResolve((to, from, next) => {
        // If the user is not authenticated, filter out this routes
       // if (to.path == '/home' && !isAuthenticated)
       //     navigateTo('/')

        if (to.path == '/makebooking' && !isAuthenticated)
            navigateTo('/')

        // If the user is authenticated, filter out this routes
        if (to.path == '/login' && isAuthenticated)
            navigateTo('/')
            
        if (to.path == '/register' && isAuthenticated)
            navigateTo('/')

        next()
    });    
})

export async function checkToken() {
    let token = useCookie('token').value
    let config = useRuntimeConfig()
    let serverUrl = config.BACKEND_URL

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
    const token = useCookie('refresh').value
    let config = useRuntimeConfig()
    let serverUrl = config.BACKEND_URL

    let resp = await fetch(serverUrl + '/api/refresh/',
    { 
        headers: {
            'Authorization': 'Bearer ' + token
        },
        method: 'POST',
    })
    .then((res) => {
        return (res.status == 200) ? true : false
    })
    .catch(() => false)

    return resp
}