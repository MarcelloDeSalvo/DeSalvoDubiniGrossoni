export function fetchApi(method='POST', endpoint, onOk, onKo) {
    if (method == 'POST') {
        return postRequest(endpoint, onOk, onKo).then((r) => {
            let status = r.response.status
            let json = r.json 
            
            if (status!= 201 && status != 200)
                onKo(r, json)
            else
                onOk(r, json)
            
        }).catch( (error) => {
            console.error('login form could not be sent', error.message)
        });
                
    }else if (method == 'GET') {
        return getRequest(endpoint, onOk, onKo).then((r) => {
            let status = r.response.status
            let json = r.json

            if (status!= 201 && status != 200)
                onKo(r, json)
            else
                onOk(r, json)
            
        }).catch( (error) => {
            console.error('login form could not be sent', error.message)
        }); 
    }
}

export async function postRequest( endpoint, formData) {
    let config = useRuntimeConfig()
    let serverUrl = config.BACKEND_URL
    const r = await fetch(serverUrl+endpoint, { 
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

export async function getRequest( endpoint ) {
    let config = useRuntimeConfig()
    let serverUrl = config.BACKEND_URL
    const r = await fetch(serverUrl+endpoint, { 
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
