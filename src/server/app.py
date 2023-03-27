from fastapi import FastAPI
from routes.homehub import router as HomeHubRouter
from utils.hubcontroller import HubController

app = FastAPI(
    title="Home Hub API",
    description="API for controlling a home hub display",
    docs_url="/docs",
    openapi_url="/docs/openapi.json",
)

app.include_router(HomeHubRouter, tags=["Home Hub"], prefix="/homehub")


@app.on_event("startup")
async def startup_event():
    controller = HubController()
    controller.set_display_sleep_options()
    controller.open_url_fullscreen_detached("http://homeassistant.local:8123")


@app.get("/healthz", tags=["Health"])
async def health():
    return "Healthy"
