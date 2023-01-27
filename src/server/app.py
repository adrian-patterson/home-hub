from fastapi import FastAPI
from routes.sample import router as SampleRouter

app = FastAPI(
    title="Sample API",
    description="Sample API to perform CRUD operations",
    docs_url="/samples/docs",
    openapi_url="/samples/docs/openapi.json",
)


@app.get("/scenes/healthz", tags=["Health"])
async def health():
    return "Healthy"

app.include_router(SampleRouter, tags=["Sample"], prefix="/samples")
