import hashlib
import logging

# Configure Logging
logging.basicConfig(
    filename="auth.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# User Class
class User:
    MAX_FAILED_ATTEMPTS = 3

    def __init__(self, username, password, privilege="user"):
        self.set_username(username)
        self.__password_hash = self.__hash_password(password)
        self.set_privilege(privilege)
        self.__failed_attempts = 0
        self.__is_locked = False

    # Private Password Hasher
    def __hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    # -------------------------
    # Username Setter (Validation)
    # -------------------------
    def set_username(self, username):
        if not username or len(username) < 3:
            raise ValueError("Username must be at least 3 characters long.")
        self.__username = username

    def get_username(self):
        return self.__username

    # Privilege Setter (Validation)
    def set_privilege(self, privilege):
        allowed_roles = ["user", "admin"]
        if privilege not in allowed_roles:
            raise ValueError("Invalid privilege level.")
        self.__privilege = privilege

    def get_privilege(self):
        return self.__privilege

    # Authentication Method
    def authenticate(self, password):
        if self.__is_locked:
            logging.warning(f"Locked account login attempt: {self.__username}")
            return False

        if self.__password_hash == self.__hash_password(password):
            self.__failed_attempts = 0
            logging.info(f"Successful login: {self.__username}")
            return True
        else:
            self.__failed_attempts += 1
            logging.warning(f"Failed login attempt {self.__failed_attempts} for {self.__username}")

            if self.__failed_attempts >= User.MAX_FAILED_ATTEMPTS:
                self.__is_locked = True
                logging.critical(f"Account locked: {self.__username}")

            return False

    # Safe User Info Display
    def display_info(self):
        return {
            "username": self.__username,
            "privilege": self.__privilege,
            "account_locked": self.__is_locked
        }

    # Prevent Direct Password Access
    @property
    def password(self):
        raise AttributeError("Password is private and cannot be accessed directly.")

    # Unlock with Validation
    def unlock_account(self, admin_user):
        if admin_user.get_privilege() == "admin":
            self.__failed_attempts = 0
            self.__is_locked = False
            logging.info(f"Account unlocked by admin: {admin_user.get_username()}")
        else:
            logging.warning(f"Unauthorized unlock attempt by: {admin_user.get_username()}")
            raise PermissionError("Only admin users can unlock accounts.")

# Demo Section
if __name__ == "__main__":

    # Creating multiple users
    admin = User("adminUser", "AdminPass123", "admin")
    user1 = User("johnDoe", "UserPass123", "user")

    print("=== Authentication Demo ===")

    # Correct login
    print("Correct password:", user1.authenticate("UserPass123"))

    # Incorrect login attempts
    print("Wrong password:", user1.authenticate("wrong1"))
    print("Wrong password:", user1.authenticate("wrong2"))
    print("Wrong password (locks account):", user1.authenticate("wrong3"))

    # Attempt login after lock
    print("Attempt after lock:", user1.authenticate("UserPass123"))

    # Unlock account (admin)
    admin.authenticate("AdminPass123")
    user1.unlock_account(admin)

    print("Login after unlock:", user1.authenticate("UserPass123"))

    # Safe display
    print("Safe user info:", user1.display_info())

    # Attempt privilege escalation
    try:
        user1.set_privilege("admin")
    except ValueError as e:
        print("Privilege escalation prevented:", e)