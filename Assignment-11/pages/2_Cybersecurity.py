import streamlit as st

from services.database_manager import DatabaseManager
from models.security_incident import SecurityIncident

st.title("🛡 Cybersecurity Incidents")

# Connect to database
db = DatabaseManager("database/platform.db")
db.connect()

# Fetch incidents
rows = db.fetch_all(
    "SELECT id, incident_type, severity, status, description FROM cyber_incidents"
)

incidents: list[SecurityIncident] = []

for row in rows:
    incident = SecurityIncident(
        incident_id=row[0],
        incident_type=row[1],
        severity=row[2],
        status=row[3],
        description=row[4],
    )
    incidents.append(incident)

# Display incidents
if not incidents:
    st.info("No incidents found.")
else:
    for incident in incidents:
        with st.expander(str(incident)):
            st.write("Severity level:", incident.get_severity_level())
            st.write("Status:", incident.get_status())
            st.write("Description:", incident.get_description())