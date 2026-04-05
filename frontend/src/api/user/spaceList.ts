import { apiBaseFetch } from "../../tools/api"


type ApiResponse<T> = {
    data?: T
    error?: string
}

export const fetchSpacesList = async (): Promise<ApiResponse<any>> => {
    try {
        const res = await apiBaseFetch('/api/space')
        if (!res.ok) throw new Error('Backend not responding')

        const json = await res.json()
        return json
    } catch (err: unknown) {
        return {
            error: err instanceof Error ? err.message : 'Unknown error'
        }
    }
}

