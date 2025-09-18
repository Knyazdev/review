from fastapi import APIRouter, Depends, status
from async_lru import alru_cache

from core.database.repositories.blog import BlogRepository
from core.api.dependencies.depends import get_blog_repository

router = APIRouter()


@alru_cache()
@router.get("/get_blogs", status_code=status.HTTP_200_OK)
async def get_blogs(repository: BlogRepository = Depends(get_blog_repository)):
    """
    Get blogs counter

    :return: blogs counter
    """
    return {"status": status.HTTP_200_OK, "blogs": await repository.get_all()}
