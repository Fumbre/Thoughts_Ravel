from fastapi.routing import APIRouter
from fastapi import Request
from common.response.default import CommonResponse
from common.filter.user import get_current_user
from fastapi import Response, Request
from ai_agent.ai_agent import AiAgent
from pydantic import BaseModel

class ChatRequest(BaseModel):
    prompt: str

router = APIRouter(prefix='/ai')

@router.post('/chat/{root_node_id}')
async def chat(req: Request, body: ChatRequest, root_node_id: str) -> CommonResponse:
    user = get_current_user(req)
    root_node_id = root_node_id

    if user is None:
        return CommonResponse.faild(message="user not found")

    body.prompt = f"{body.prompt} The user_id:{user["id"]}, rood_node_id: {root_node_id}"
    
    result = await AiAgent.chat(prompt=body.prompt)

    return CommonResponse.success(data=result)