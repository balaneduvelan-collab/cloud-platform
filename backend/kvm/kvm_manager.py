import libvirt

class KVMManager:
    def __init__(self, mock_mode=False):
        self.mock_mode = mock_mode
        self.conn = None

        if self.mock_mode:
            print("[INFO] KVMManager running in MOCK mode — libvirt not required")
            self._mock_vms = ["mock-vm1", "mock-vm2"]
            return

        try:
            self.conn = libvirt.open("qemu:///system")
            if self.conn is None:
                print("[WARN] Could not connect to libvirt: returned None")
        except libvirt.libvirtError as e:
            print(f"[WARN] Could not connect to libvirt: {e}")
            self.conn = None

    def list_vms(self):
        if self.mock_mode:
            return self._mock_vms

        if not self.conn:
            return []
        domains = self.conn.listAllDomains()
        return [dom.name() for dom in domains]