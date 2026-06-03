const BASE = import.meta.env.VITE_API_BASE_URL;

export async function apiBaseFetch(
    endpoint: string,
    options: RequestInit = {},
    token?: string
): Promise<Response> {

    const headers = new Headers(options.headers);

    if (!headers.has("Content-Type")) {
        headers.set("Content-Type", "application/json");
    }

    if (token) {
        headers.set("Authorization", `${token}`);
    }

    return fetch(`${BASE}${endpoint}`, {
        ...options,
        headers: headers
    });
}