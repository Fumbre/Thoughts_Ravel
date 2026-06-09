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
        console.log(list)
        console.log("fasdfas fkashdf lkjahsdf lk")
        const res = await apiBaseFetch('/api/space', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                nodeSpaceList: list
            }),
            credentials: 'include'
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