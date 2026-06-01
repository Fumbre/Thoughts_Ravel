const BASE = import.meta.env.VITE_API_BASE_URL;

export async function apiBaseFetch(endpoint: string, options: RequestInit = {}): Promise<Response> {
    return fetch(`${BASE}${endpoint}`, options);
}
