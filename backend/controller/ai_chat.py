from fastapi.routing import APIRouter
from common.response.default import CommonResponse
from common.filter.user import get_current_user
from fastapi import Response, Request
from ai_agent.ai_agent import AiAgent
from pydantic import BaseModel

class ChatRequest(BaseModel):
    prompt: str

router = APIRouter(prefix='/ai')

@router.post('/chat')
async def chat( body: ChatRequest) -> CommonResponse:
    # user = get_current_user(request)
    
    result = AiAgent.chat(prompt=body.prompt)

    return CommonResponse.success(data=result)