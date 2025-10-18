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
