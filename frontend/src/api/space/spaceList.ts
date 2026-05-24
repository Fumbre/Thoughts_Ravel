import { apiBaseFetch } from "../../tools/api"
import { ApiResponse } from '../response'


// get space list
export const fetchSpaceList = async (): Promise<ApiResponse<any>> => {
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

interface IPostSpaceList {
    userId: string,
    title: string
    desc: string | null
}

// post space list
export const postSpaceList = async (list: Array<IPostSpaceList>): Promise<ApiResponse<any>> => {
    try {
        const res = await apiBaseFetch('/api/space', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                spaceList: list
            })
        })
        if (!res.ok) throw new Error('Backend not responding')
        const json = await res.json()
        return json
    } catch (err: unknown) {
        return {
            error: err instanceof Error ? err.message : 'Unknown error'
        }
    }
}