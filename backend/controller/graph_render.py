from fastapi.routing import APIRouter
from representation_engin.main import generate_graph


router = APIRouter(prefix='/api')

@router.get("/graph")
def get_graph():
    return generate_graph()