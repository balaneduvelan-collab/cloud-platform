cloud plaform / 
|-----backend/ 
            |---kvm/     
            |---firecracker/ 
            |---object_storage/ 
|-----orchestrator/ 
            |---api/ 
            |---scheduler/ 
            |---db/ 
            |--migrations/ 
|-----frontend/ 
            |---dashboard/ 
            |--src/ 
               |---components/ 
               |---pages/ 
               |---api/ 
               |--public/ 
|-----scripts/
|-----tests/ 
|-----README.md 
|-----STRUCTURE.md 
|-----.gitignore


updated v1
backend/ └── kvm/ ├── kvm_manager.py   
# KVMManager class, mock + real mode support └── vm_state.json    # Persistent VM state (for mock mode)

orchestrator/ └── api/ ├── main.py          
# FastAPI app entrypoint └── vm_routes.py     # VM API routes (create, start, stop, status)
