export async function request(method, backend, endpoint, formData) {
    let config = useRuntimeConfig()
    let serverUrl = null
    if (backend == 'emsp' || backend == 'EMSP')
        serverUrl = config.EMSP_URL
    else if (backend == 'cpms' || backend == 'CPMS')
        serverUrl = config.CPMS_URL
    else
        throw new Error("Invalid backend request");
    
    const r = await fetch(serverUrl+ "/" +endpoint, { 
      headers: {
        "Content-Type": "application/json",
      },
      method: method,
      body: JSON.stringify(formData)
    } );

    try {
        const json = await r.json()
        return { response: r, json: json }
    }catch(e){
        throw new Error("Invalid JSON request");
    }
      
}

export async function postRequest(backend, endpoint, formData) {
    let config = useRuntimeConfig()
    let serverUrl = null
    if (backend == 'emsp' || backend == 'EMSP')
        serverUrl = config.EMSP_URL
    else if (backend == 'cpms' || backend == 'CPMS')
        serverUrl = config.CPMS_URL
    else
        throw new Error("Invalid backend request");
    
    const r = await fetch(serverUrl+ "/" +endpoint, { 
      headers: {
        "Content-Type": "application/json",
      },
      method: 'POST',
      body: JSON.stringify(formData)
    } );

    try {
        const json = await r.json()
        return { response: r, json: json }
    }catch(e){
        throw new Error("Invalid JSON request");
    }
      
}

export async function deleteRequest(backend, endpoint, id) {
    let config = useRuntimeConfig()
    let serverUrl = null
    if (backend == 'emsp' || backend == 'EMSP')
        serverUrl = config.EMSP_URL
    else if (backend == 'cpms' || backend == 'CPMS')
        serverUrl = config.CPMS_URL
    else
        throw new Error("Invalid backend request");
    
    
    const r = await fetch(serverUrl+ "/" +endpoint, { 
      headers: {
        "Content-Type": "application/json",
      },
      method: 'DELETE',
      body: JSON.stringify({id: id})
    } );

    try {
        const json = await r.json()
        return { response: r, json: json }
    }catch(e){
        throw new Error("Invalid JSON request");
    }
      
}

export async function getRequest( backend , endpoint ) {
    let config = useRuntimeConfig()
    let serverUrl = null
    if (backend == 'emsp' || backend == 'EMSP')
        serverUrl = config.EMSP_URL
    else if (backend == 'cpms' || backend == 'CPMS')
        serverUrl = config.CPMS_URL
    else
        throw new Error("Invalid backend request");
    
    console.log("URL: " + serverUrl+ "/" +endpoint)
    
    const r = await fetch(serverUrl+ "/" +endpoint, { 
      headers: {
        "Content-Type": "application/json",
      },
      method: 'GET',
    } );

    try{
        const json = await r.json()
        return { response: r, json: json }
    }catch(e){
      throw new Error("Invalid JSON request");
    }
}

export async function deleteRequestWithToken(backend, endpoint, id) {
    let config = useRuntimeConfig()
    let serverUrl = null
    let token = useCookie('token').value
    if (backend == 'emsp' || backend == 'EMSP')
        serverUrl = config.EMSP_URL
    else if (backend == 'cpms' || backend == 'CPMS')
        serverUrl = config.CPMS_URL
    else
        throw new Error("Invalid backend request");
    
    
    const r = await fetch(serverUrl+ "/" +endpoint, { 
      headers: {
        "Content-Type": "application/json",
        'Authorization': 'Bearer ' + token
      },
      method: 'DELETE',
      body: JSON.stringify({id: id})
    } );

    try {
        const json = await r.json()
        return { response: r, json: json }
    }catch(e){
        throw new Error("Invalid JSON request");
    }
      
}

//post with token
export async function postRequestWithToken(backend, endpoint, formData) {
    let config = useRuntimeConfig()
    let serverUrl = null
    let token = useCookie('token').value
    if (backend == 'emsp' || backend == 'EMSP')
        serverUrl = config.EMSP_URL
    else if (backend == 'cpms' || backend == 'CPMS')
        serverUrl = config.CPMS_URL
    else
        throw new Error("Invalid backend request");
    
    const r = await fetch(serverUrl+ "/" +endpoint, { 
      headers: {
        "Content-Type": "application/json",
        'Authorization': 'Bearer ' + token
      },
      method: 'POST',
      body: JSON.stringify(formData)
    } );

    try {
        const json = await r.json()
        return { response: r, json: json }
    }catch(e){
        throw new Error("Invalid JSON request");
    }
      
}