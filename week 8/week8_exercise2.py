#Iot device mgmt system

import logging
from datetime import datetime, timedelta

# Logging Configuration

logging.basicConfig(
    filename="device_management.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Simple User Class
class User:
    def __init__(self, username, role="user"):
        if role not in ["user", "admin"]:
            raise ValueError("Role must be 'user' or 'admin'")
        self.username = username
        self.role = role


# Device Class
class Device:
    def __init__(self, device_id, device_type, firmware_version, owner):
        # Validation
        if not device_id:
            raise ValueError("Device ID cannot be empty")
        if not firmware_version:
            raise ValueError("Firmware version required")

        self.device_id = device_id
        self.device_type = device_type
        self.firmware_version = firmware_version
        self.owner = owner
        self.last_security_scan = datetime.now()
        self.compliance_status = True
        self.is_active = True
        self.is_quarantined = False

    # Compliance Check
    def check_compliance(self):
        if datetime.now() - self.last_security_scan > timedelta(days=30):
            self.compliance_status = False
        return self.compliance_status

    # Authorise Access
    def authorise_access(self, user):
        self.check_compliance()

        if not self.is_active or self.is_quarantined:
            logging.warning(f"Access denied to {self.device_id} (inactive/quarantined)")
            return False

        if self.compliance_status and user.username == self.owner:
            logging.info(f"Access granted to {user.username} for {self.device_id}")
            return True

        if user.role == "admin":
            logging.info(f"Admin override access by {user.username} for {self.device_id}")
            return True

        logging.warning(f"Unauthorized access attempt by {user.username} for {self.device_id}")
        return False

    # Firmware Update
    def update_firmware(self, new_version, user):
        if self.authorise_access(user):
            self.firmware_version = new_version
            logging.info(f"{self.device_id} firmware updated to {new_version}")
        else:
            print("Access denied. Cannot update firmware.")

    # Run Security Scan
    def run_security_scan(self):
        self.last_security_scan = datetime.now()
        self.compliance_status = True
        logging.info(f"Security scan completed for {self.device_id}")

    # Quarantine Device
    def quarantine(self):
        self.is_quarantined = True
        self.is_active = False
        logging.critical(f"{self.device_id} has been quarantined!")


# Device Manager Class
class DeviceManager:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
        logging.info(f"Device added: {device.device_id}")

    def remove_device(self, device_id):
        self.devices = [d for d in self.devices if d.device_id != device_id]
        logging.info(f"Device removed: {device_id}")

    def generate_security_report(self):
        print("\n--- Security Report ---")
        for device in self.devices:
            device.check_compliance()
            print(f"Device: {device.device_id}")
            print(f"  Owner: {device.owner}")
            print(f"  Firmware: {device.firmware_version}")
            print(f"  Compliant: {device.compliance_status}")
            print(f"  Active: {device.is_active}")
            print(f"  Quarantined: {device.is_quarantined}")
            print("----------------------")


# Demo Section
if __name__ == "__main__":

    manager = DeviceManager()

    admin = User("Alice", "admin")
    user1 = User("Bob", "user")

    device1 = Device("D1001", "Smart Camera", "1.0", "Bob")

    manager.add_device(device1)

    # User access
    print("User trying access:", device1.authorise_access(user1))

    # Update firmware
    device1.update_firmware("1.1", user1)

    # Simulate non-compliance (manually adjust date for demo)
    device1.last_security_scan = datetime.now() - timedelta(days=31)

    print("Compliance status:", device1.check_compliance())

    # Admin override
    print("Admin trying access:", device1.authorise_access(admin))

    # Quarantine device
    device1.quarantine()

    # Generate report
    manager.generate_security_report()