from fastapi import APIRouter
from backend.kvm.kvm_manager import KVMManager

router = APIRouter(prefix="/vms", tags=["Virtual Machines"])

# mock_mode=True while testing; switch to False in deployment
manager = KVMManager(mock_mode=True)

@router.get("/")
def list_vms():
    return {"vms": manager.list_vms()}

@router.post("/create/{name}")
def create_vm(name: str):
    return manager.create_vm(name)

@router.post("/start/{name}")
def start_vm(name: str):
    return manager.start_vm(name)

@router.post("/stop/{name}")
def stop_vm(name: str):
    return manager.stop_vm(name)

@router.get("/status/{name}")
def get_vm_status(name: str):
    return {"name": name, "status": manager.get_status(name)}

@router.get("/status")
def get_all_status():
    return {"statuses": manager.get_all_status()}