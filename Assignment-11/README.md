# Multi-Domain Intelligence Platform – Week 11 (OOP Refactor)

## Overview
This project is the Week 11 Object-Oriented Programming (OOP) refactor of the
Multi-Domain Intelligence Platform for CST1510.

The focus of Week 11 is improving software architecture by:
- Introducing entity classes (models)
- Separating business logic into service classes
- Refactoring procedural code into clean OOP design

The application is built using Python, Streamlit, and SQLite.

---

## Project Structure

multi_domain_platform/
├── models/
│   ├── user.py
│   ├── security_incident.py
│   ├── dataset.py
│   └── it_ticket.py
│
├── services/
│   ├── database_manager.py
│   ├── auth_manager.py
│   └── ai_assistant.py
│
├── database/
│   └── platform.db
│
├── pages/
│   ├── 1_Login.py
│   ├── 2_Cybersecurity.py
│   ├── 3_Data_Science.py
│   ├── 4_IT_Operations.py
│   └── 5_AI_Assistant.py
│
├── Home.py
├── requirements.txt
├── README.md
└── .gitignore

---

## OOP Design

### Models
Each domain entity is implemented as a Python class using:
- Private attributes
- Constructors
- Getter methods
- __str__() for readable output

Entities:
- User
- SecurityIncident
- Dataset
- ITTicket

---

### Services
Service classes handle application logic:

- DatabaseManager  
  Manages all SQLite connections and queries.

- AuthManager  
  Handles user authentication and password verification.

- AIAssistant  
  Encapsulates AI logic and separates it from the Streamlit UI.

---

## Streamlit Refactor
All Streamlit pages use:
- Model objects instead of raw database tuples
- Service classes instead of direct SQL queries
- Session state for authentication and AI chat

---

## How to Run

1. Install dependencies:
   pip install streamlit pandas matplotlib

2. Run the application:
   streamlit run Home.py

---

## Notes
- AI Assistant uses a placeholder implementation (Week 11 requirement).
- The architecture is designed for scalability and maintainability.
- This project demonstrates core OOP principles taught in Week 11.

