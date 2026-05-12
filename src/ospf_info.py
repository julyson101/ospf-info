from netmiko import ConnectHandler


def show_ip_ospf(device):
    """
    Connects to a device and retrieves OSPF information
    """
    print(f"Connecting to {device['name']} ({device['host']})")

    connection = ConnectHandler(
            device_type=device["device_type"],
            host=device["host"],
            username=device["username"],
            password=device["password"],

    )

    output = connection.send_command("show ip ospf")
    connection.disconnect()

    return output

