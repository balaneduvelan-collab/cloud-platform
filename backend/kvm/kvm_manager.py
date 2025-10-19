import json
import os
import libvirt

class KVMManager:
    STATE_FILE = os.path.join(os.path.dirname(__file__), "vm_state.json")

    def __init__(self, mock_mode=True):
        self.mock_mode = mock_mode
        self.vms = self._load_state()
        self.conn = None

        if not mock_mode:
            try:
                self.conn = libvirt.open("qemu:///system")
                print("[INFO] Connected to real KVM environment")
            except libvirt.libvirtError as e:
                print(f"[WARN] Could not connect to libvirt: {e}")
        else:
            print("[INFO] KVMManager running in MOCK mode — persistence active")

    # ----------------------------------------------------------------------
    # State persistence (for mock mode)
    # ----------------------------------------------------------------------
    def _load_state(self):
        if not os.path.exists(self.STATE_FILE):
            return {}
        try:
            with open(self.STATE_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return {}

    def _save_state(self):
        with open(self.STATE_FILE, "w") as f:
            json.dump(self.vms, f, indent=2)

    # ----------------------------------------------------------------------
    # Core VM operations
    # ----------------------------------------------------------------------
    def list_vms(self):
        if self.mock_mode:
            return list(self.vms.keys())
        if not self.conn:
            return []
        return [dom.name() for dom in self.conn.listAllDomains()]

    def create_vm(self, name):
        if self.mock_mode:
            if name in self.vms:
                return {"error": f"VM '{name}' already exists."}
            self.vms[name] = {"status": "stopped"}
            self._save_state()
            return {"message": f"VM '{name}' created (mock)."}
        # Placeholder for real creation
        return {"error": "Real VM creation logic not yet implemented."}

    def start_vm(self, name):
        if self.mock_mode:
            if name not in self.vms:
                return {"error": "VM not found."}
            self.vms[name]["status"] = "running"
            self._save_state()
            return {"message": f"VM '{name}' started (mock)."}
        dom = self._get_domain(name)
        if dom:
            dom.create()
            return {"message": f"VM '{name}' started."}
        return {"error": "VM not found."}

    def stop_vm(self, name):
        if self.mock_mode:
            if name not in self.vms:
                return {"error": "VM not found."}
            self.vms[name]["status"] = "stopped"
            self._save_state()
            return {"message": f"VM '{name}' stopped (mock)."}
        dom = self._get_domain(name)
        if dom:
            dom.shutdown()
            return {"message": f"VM '{name}' stopped."}
        return {"error": "VM not found."}

    def get_status(self, name):
        if self.mock_mode:
            return self.vms.get(name, {}).get("status", "unknown")
        dom = self._get_domain(name)
        if not dom:
            return "not found"
        state, _ = dom.state()
        states = {
            libvirt.VIR_DOMAIN_RUNNING: "running",
            libvirt.VIR_DOMAIN_SHUTOFF: "stopped",
            libvirt.VIR_DOMAIN_PAUSED: "paused",
            libvirt.VIR_DOMAIN_CRASHED: "crashed",
        }
        return states.get(state, "unknown")

    def get_all_status(self):
        if self.mock_mode:
            return {name: data["status"] for name, data in self.vms.items()}
        if not self.conn:
            return {}
        return {dom.name(): self.get_status(dom.name()) for dom in self.conn.listAllDomains()}

    def _get_domain(self, name):
        if not self.conn:
            return None
        try:
            return self.conn.lookupByName(name)
        except libvirt.libvirtError:
            return None