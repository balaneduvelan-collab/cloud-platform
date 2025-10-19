#cloud platform 
> modular cloud platform imspired from existing oss .
> starting with ec2 and s3 storage . .
    - we use kvm , libvert , firecracker , and miniIO and ceph oss.

## project overview 
the  **cloud platform** aims to provide scable , modular , and easily deployable cloud infra . 
It uses more battle tested oss as base and built over it.

### tech stack 
backend fastAPI (python), sQlite ,and postgresQl, react 

version 0.0.0 
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


## Phase 1 – KVM Virtualization & API

### Overview
This phase implements a minimal EC2-like IaaS layer for compute (VMs) using KVM/QEMU/Firecracker + Libvirt.  
VMs can be created, started, stopped, and queried via a FastAPI REST API.  

The system supports both:
- Mock mode (for local development or hardware without virtualization)
- Real mode (on KVM-enabled hardware)

### Folder Structure

### Features
- Create VM (POST /vms/create/{name})
- Start VM (POST /vms/start/{name})
- Stop VM (POST /vms/stop/{name})
- Get single VM status (GET /vms/status/{name})
- Get all VM statuses (GET /vms/status)
- Persistent mock state stored in vm_state.json
- Toggle mock/real mode via mock_mode parameter
- Fully ready for future EC2-style metadata and dashboard integration

### Next Steps
- Add EC2-like instance metadata (ID, type, CPU, RAM, timestamp)
- Integrate Object Storage (Ceph + MinIO)
- Add IAM/Auth integration (Keycloak/Syncope)
- Extend real KVM XML creation and cloud-init support
