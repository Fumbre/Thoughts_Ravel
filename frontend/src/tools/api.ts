const BASE_URL = import.meta.env.VITE_API_BASE_URL;

export const apiBaseFetch = (url: string, options: RequestInit = {}): Promise<Response> => {
    return fetch(`${BASE_URL}${url}`, {
        credentials: 'include',  // send cookies
        ...options,
    })
}
