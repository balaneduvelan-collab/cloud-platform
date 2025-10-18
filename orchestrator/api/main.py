from fastapi import FastAPI
from backend.kvm.kvm_manager import KVMManager

app = FastAPI(title="Cloud Platform Orchestration")

# Force mock mode for now
kvm_manager = KVMManager(mock_mode=True)

@app.get("/")
def root():
    return {"message": "Cloud Platform Orchestration API running"}

@app.get("/vms")
def list_vms():
    return {"vms": kvm_manager.list_vms()}