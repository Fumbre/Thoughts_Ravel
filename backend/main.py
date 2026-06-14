import os
from dotenv import load_dotenv
import uvicorn
from controller.user import router as routerUser
from controller.node import router as routerNode
from controller.ai_chat import router as routerAI
from controller.graph_render import router as routerGraph
# from controller.space import router as routerSpace
# from controller.node_relations import router as routerNodeRelations
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from common.config.life_span import lifespan
from common.filter.api_filter import ApiFilter


load_dotenv()

app = FastAPI(lifespan=lifespan)
app.include_router(routerUser)
app.include_router(routerNode)
app.include_router(routerAI)
app.include_router(routerGraph)
# app.include_router(routerSpace)
# app.include_router(routerNodeRelations)

# Get the string from .env and split it by the comma into a list
origins_str = os.getenv("ALLOWED_ORIGINS", "http://localhost:50000")
origins = origins_str.split(",")

app.add_middleware(
    ApiFilter
)

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



if __name__ == "__main__" :
    uvicorn.run("app:main", host="0.0.0.0", port=3000, reload=True)