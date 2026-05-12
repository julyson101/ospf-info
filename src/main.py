import yaml
from ospf_info import show_ip_ospf
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = BASE_DIR.parent

INVENTORY_FILE = ROOT_DIR / "inventory" / "ocnos-devices.yml"
OUTPUT_FILE = "output/ospf_info.txt"


def load_devices():
    with open(INVENTORY_FILE, "r") as f:
        return yaml.safe_load(f)["devices"]

def main():
    devices = load_devices()

    with open(OUTPUT_FILE, "w") as outfile:
        for device in devices:
            ospf_info_output = show_ip_ospf(device)

            outfile.write(f"\n===== {device['name']} =====\n")
            outfile.write(ospf_info_output)
            outfile.write("\n")

    print("OSPF info retrieval completed successfully")

if __name__ == "__main__":
    main()

