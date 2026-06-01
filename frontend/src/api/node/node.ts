import { apiBaseFetch } from "../../tools/api"
import { ApiResponse } from '../response'

interface IPostNodeChild {
    name: string,
    desc: string | null,
    positionX: number,
    positionY: number,
    color: string,
    shape: string,
    creater_id: number,
}

interface IPostNodeParent {
    nodeId: string,
    spaceId: string,
    userId: string,
}



// This method should be done in database
// 1
// 2
// 3
// 4

// 5=
// 0,1,2,3,4
// 7463519295578836993,
// 7463519295578836993,
// 7463519295578836993,
// 7463519295578836993,
// 7463519295578836993,
// it will same save the request data
// I'm lazy
export const postNodeToNode = async (nodeChild: IPostNodeChild, nodeParent: IPostNodeParent): Promise<ApiResponse<any>> => {
    try {
        const data = Object.assign(nodeChild, nodeParent)


        const respond = await apiBaseFetch(`/api/node_connection`, {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)

        })

        console.log("[api/node.ts]", respond)

        // const res = await apiBaseFetch(`/api/node_relations`, {
        //     method: "POST",
        //     headers: { 'Content-Type': 'application/json' },
        //     body: JSON.stringify({
        //         nodeList: "test"
        //     })

        // })

        // if (!res.ok) throw new Error('Backend not responding')
        // const json = await res.json()
        // return json

    } catch (err: unknown) {
        return {
            error: err instanceof Error ? err.message : 'Unknown error'
        }
    }
}

