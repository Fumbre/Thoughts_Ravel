from sqlalchemy import select
from request.space_request import SpaceRequest, SpaceListRequest
from decorators.decor import Transactional
from model.space import Space
from common.db.session import AsyncSession
from common.response.default import CommonResponse

from response.space_response import SpaceResponse, SpaceListResponse

@Transactional
async def insert(request: SpaceListRequest, db: AsyncSession) -> CommonResponse:
    emptyList = []
    for space in request.spaceList :
        emptyList.append(Space(**space.model_dump()))

    db.add_all(emptyList)

    return CommonResponse.success()

async def get(id: str, userId: str, db: AsyncSession) -> CommonResponse[SpaceResponse]:
    data = await db.scalar(select(Space).where(Space.id == int(id), Space.userId == int(userId)))

    result = SpaceResponse.model_validate(data)
    result.id = str(result.id)

    return CommonResponse.success(data=result)


async def get_all(userId: str, db: AsyncSession) -> CommonResponse[SpaceListResponse]:
    data = await db.scalars(select(Space).where(Space.userId == int(userId)))
    results = data.all()
    results = [SpaceResponse.model_validate(row) for row in results]
    for result in results:
        result.id = str(result.id)

    return CommonResponse.success(data=SpaceListResponse(spaceList=results))
