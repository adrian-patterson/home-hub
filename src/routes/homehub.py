from fastapi import APIRouter, Response
from fastapi.encoders import jsonable_encoder
from utils.hubcontroller import HubController


router = APIRouter()
hub_controller = HubController()


@router.post(
    "/url", summary="Set display to given URL", response_description="The set URL"
)
async def display_url(url: str):
    hub_controller.open_url(url)
    return jsonable_encoder(url)


@router.get(
    "/close", summary="Close browser if open", response_description="Success message"
)
async def close_display():
    hub_controller.close_browser()
    return Response("Success")
