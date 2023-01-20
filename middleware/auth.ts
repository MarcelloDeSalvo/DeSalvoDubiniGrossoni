export default defineNuxtRouteMiddleware(async (to) => {
    // Check if the user is authenticated by calling an API endpoint with nuxt 3's new fetch API
    let isAuthenticated = false
    
    // Ask the server if the user is authenticated
    isAuthenticated = await checkToken()

    const router = useRouter()

    router.beforeResolve((to, from, next) => {
        // If the user is not authenticated, filter out these routes
        if (to.path == '/home' && !isAuthenticated)
            navigateTo('/')
        // If the user is authenticated, filter out these routes
        if (to.path == '/login' && isAuthenticated)
            navigateTo('/')
            
        if (to.path == '/register' && isAuthenticated)
            navigateTo('/')

        next()
    });
})

export async function checkToken() {
    const token = useCookie('token').value
    let config = useRuntimeConfig()
    let serverUrl = config.EMSP_URL


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
  