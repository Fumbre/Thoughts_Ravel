import { apiBaseFetch } from "../../tools/api"
import { ApiResponse } from '../response'



export const getNodeById = async (node_id: string): Promise<ApiResponse<any>> => {
    try {
        const res = await apiBaseFetch(`/api/node/${node_id}`)
        if (!res.ok) throw new Error('Backend not responding')
        const json = await res.json()
        return json
    } catch (err: unknown) {
        return {
            error: err instanceof Error ? err.message : 'Unknown error'
        }
    }
}

interface IPostNodeEdge {
    name: string,
    description: string | null,
    type: string,
    shape: string,
    color: string,
    parent_id: string
}

export const postNodeEdge = async (list: Array<IPostNodeEdge>): Promise<ApiResponse<any>> => {
    try {
        const res = await apiBaseFetch('/api/node', {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(
                {
                    nodeEdgeList: list
                }
            )
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

export const updateNodePos = async (
    id: string,
    position_x: number,
    position_y: number,
): Promise<ApiResponse<any>> => {
    try {
        const res = await apiBaseFetch('/api/node', {
            method: "PATCH",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id, position_x, position_y }
            )
        })
        if (!res.ok) throw new Error('Backend not responding')
        const json = await res.json()
        console.log(json.data)
        return json
    } catch (err: unknown) {
        return {
            error: err instanceof Error ? err.message : 'Unknown error'
        }
    }
}
