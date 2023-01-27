from fastapi import FastAPI
from routes.homehub import router as HomeHubRouter

app = FastAPI(
    title="Home Hub API",
    description="API for controlling a home hub display",
    docs_url="/docs",
    openapi_url="/docs/openapi.json",
)


@app.get("/scenes/healthz", tags=["Health"])
async def health():
    return "Healthy"


app.include_router(HomeHubRouter, tags=["Home Hub"], prefix="/homehub")
