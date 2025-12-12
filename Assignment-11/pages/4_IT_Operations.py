import streamlit as st
from services.database_manager import DatabaseManager
from models.it_ticket import ITTicket

st.title("💻 IT Operations")

# Connect to database
db = DatabaseManager("database/platform.db")
db.connect()

# Fetch IT tickets
rows = db.fetch_all(
    "SELECT id, title, priority, status, assigned_to FROM it_tickets"
)

tickets: list[ITTicket] = []

for row in rows:
    ticket = ITTicket(
        ticket_id=row[0],
        title=row[1],
        priority=row[2],
        status=row[3],
        assigned_to=row[4],
    )
    tickets.append(ticket)

st.subheader("IT Support Tickets")

if not tickets:
    st.info("No IT tickets found.")
else:
    for ticket in tickets:
        st.write(ticket)
        st.caption(f"Status: {ticket.get_status()}")

db.close()