import streamlit as st
from services.database_manager import DatabaseManager
from models.dataset import Dataset

st.title("📊 Data Science")

# Connect to database
db = DatabaseManager("database/platform.db")
db.connect()

# Fetch datasets from database
rows = db.fetch_all(
    "SELECT id, name, size_bytes, rows, source FROM datasets_metadata"
)

datasets: list[Dataset] = []

for row in rows:
    dataset = Dataset(
        dataset_id=row[0],
        name=row[1],
        size_bytes=row[2],
        rows=row[3],
        source=row[4],
    )
    datasets.append(dataset)

# Display datasets
st.subheader("Available Datasets")

if not datasets:
    st.info("No datasets found.")
else:
    for ds in datasets:
        st.write(ds)
        st.caption(f"Source: {ds.get_source()}")

db.close()