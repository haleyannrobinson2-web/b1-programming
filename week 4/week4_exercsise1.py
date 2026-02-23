login_attempts = [
("alice", "success"),
("bob", "failed"),
("bob", "failed"),
("charlie", "success"),
("bob", "failed"),
("alice", "failed")]

failed_counts = {}


print ("Checking login attempts...")


for username, status in login_attempts:
    if status == "failed":
        if username in failed_counts:
            failed_counts[username] = failed_counts[username] + 1
        else: