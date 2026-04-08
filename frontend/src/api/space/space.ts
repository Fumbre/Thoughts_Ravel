import { apiBaseFetch } from "../../tools/api"
import { ApiResponse } from '../response'

export const fetchSpaceId = async (spaceId: string): Promise<ApiResponse<any>> => {
    try {
        const res = await apiBaseFetch(`/api/space/${spaceId}`)
        if (!res.ok) throw new Error('Backend not responding')
        const json = await res.json()
        return json
    } catch (err: unknown) {
        return {
            error: err instanceof Error ? err.message : 'Unknown error'
        }
    }
}
