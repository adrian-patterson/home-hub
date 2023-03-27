from fastapi import APIRouter, Response
from fastapi.encoders import jsonable_encoder
from utils.hubcontroller import HubController


router = APIRouter()
hub_controller = HubController()


@router.post(
    "/browser/open",
    summary="Open browser to given URL",
    response_description="The opened URL",
)
async def open_url(url: str):
    hub_controller.open_url_kiosk_attached(url)
    return jsonable_encoder(url)


@router.get(
    "/browser/close",
    summary="Close browser if open",
    response_description="Success message",
)
async def close_browser():
    hub_controller.close_browser()
    return Response("Success")


@router.get(
    "/sleep", summary="Turn off display", response_description="Success message"
)
async def sleep_display():
    hub_controller.sleep_display()
    return Response("Success")


@router.get("/wake", summary="Wake up display", response_description="Success message")
async def wake_up_display():
    hub_controller.wake_up_display()
    return Response("Success")
