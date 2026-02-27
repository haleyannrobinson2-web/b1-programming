import json
import os

class UserStore:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, "r") as file:
            try:
                return json.load(file)
            except:
                return []

    def save(self, users):
        with open(self.file_path, "w") as file:
            json.dump(users, file, indent=4)

    def find_by_id(self, user_id):
        users = self.load()
        for user in users:
            if user["id"] == user_id:
                return user
        return None

    def get_next_id(self):
        users = self.load()
        if not users:
            return 1
        return max(user["id"] for user in users) + 1

    def create_user(self, user_data):
        users = self.load()
        new_user = {
            "id": self.get_next_id(),
            "name": user_data.name,
            "email": user_data.email
        }
        users.append(new_user)
        self.save(users)
        return new_user

    def update_user(self, user_id, updated_data):
        users = self.load()
        for user in users:
            if user["id"] == user_id:
                user["name"] = updated_data.name
                user["email"] = updated_data.email
                self.save(users)
                return True
        return False

    def delete_user(self, user_id):
        users = self.load()
        for user in users:
            if user["id"] == user_id:
                users.remove(user)
                self.save(users)
                return True
        return False
