from fastapi import APIRouter

from api.v1.endpoints import excel_file

api_router = APIRouter()
api_router.include_router(excel_file.router, prefix = "/v1")
