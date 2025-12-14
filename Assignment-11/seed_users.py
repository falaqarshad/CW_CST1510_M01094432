from services.database_manager import DatabaseManager
from services.auth_manager import SimpleHasher

db = DatabaseManager("database/platform.db")
db.connect()

db.execute_query(
    "INSERT OR IGNORE INTO users (username, password_hash, role) VALUES (?, ?, ?)",
    ("admin", SimpleHasher.hash_password("admin123"), "admin"),
)

print("✅ Test user created (admin / admin123)")