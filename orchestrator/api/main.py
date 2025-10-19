from fastapi import FastAPI
from orchestrator.api.vm_routes import router as vm_router

app = FastAPI(title="Cloud Platform Orchestration API")

# Include all VM-related routes
app.include_router(vm_router)

@app.get("/")
def root():
    return {"message": "Cloud Platform API running"}