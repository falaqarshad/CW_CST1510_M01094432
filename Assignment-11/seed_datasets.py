from services.database_manager import DatabaseManager

db = DatabaseManager("database/platform.db")
db.connect()

db.execute_query("""
INSERT INTO datasets (name, size_bytes, rows, source)
VALUES
    ('Customer Sales Data', 5242880, 100000, 'Internal'),
    ('Website Logs', 10485760, 250000, 'Web Server'),
    ('Marketing Campaign Results', 2097152, 50000, 'Marketing Team')
""")

print("✅ Sample datasets inserted")