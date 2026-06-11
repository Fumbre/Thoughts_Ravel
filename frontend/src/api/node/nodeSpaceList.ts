import { apiBaseFetch } from "../../tools/api"
import { ApiResponse } from '../response'

interface IPostSpaceList {
    name: string,
    parent_id: string,
    description: string | null,
    type: string,
    position_x: number,
    position_y: number,
    shape: string,
    color: string,
}

// post node space list
export const postNodeSpaceList = async (list: Array<IPostSpaceList>): Promise<ApiResponse<any>> => {
    try {
        const res = await apiBaseFetch('/api/space', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                nodeSpaceList: list
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

export const getNodeSpaceList = async (parent_id: string): Promise<ApiResponse<any>> => {
    try {
        const res = await apiBaseFetch(`/api/space?parent_id=${parent_id}`)
        if (!res.ok) throw new Error('Backend not responding')
        const json = await res.json()
        return json
    } catch (err: unknown) {
        return {
            error: err instanceof Error ? err.message : 'Unknown error'
        }
    }
}