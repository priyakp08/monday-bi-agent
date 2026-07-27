# Monday.com Business Intelligence Agent

## Project Overview

The Monday.com Business Intelligence Agent is an AI-powered application that enables founders and business leaders to ask natural language questions about their business data stored in monday.com.

The application retrieves live data from monday.com boards, cleans and processes the information, calculates business metrics, and generates meaningful insights using a hybrid approach that combines deterministic Python analytics with AI-generated summaries.

This solution was developed as part of the Skylark Drones Full Stack Technical Assignment.

---

## Features

- Live integration with monday.com using the GraphQL API
- Dynamic retrieval of Deals and Work Orders data
- Automatic data cleaning and normalization
- Graceful handling of missing and incomplete data
- Natural language question answering
- Executive business summaries
- Business metrics generation
- Data quality reporting
- Modern React-based conversational interface

---

## Tech Stack

### Frontend
- React
- Vite
- Axios
- CSS

### Backend
- FastAPI
- Python
- Pandas
- Requests

### AI
- Hugging Face Inference API (Qwen Model)

### External Platform
- monday.com GraphQL API

---

## Architecture

```
                 React Frontend
                       │
                 Axios HTTP Client
                       │
                 FastAPI Backend
                       │
     ┌─────────────────┴─────────────────┐
     │                                   │
Monday.com API                    AI Module
     │                                   │
Deals & Work Orders          Hugging Face API
     │                                   │
     └───────────────┬───────────────────┘
                     │
            Business Intelligence
                 Response
```

---

## Project Structure

```
backend/
│
├── main.py
├── monday_client.py
├── data_cleaner.py
├── metrics.py
├── ai_agent.py
├── requirements.txt

frontend/
│
├── src/
│   ├── App.jsx
│   ├── App.css
│   ├── api.js
│   └── main.jsx
│
├── package.json
```

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
```

---

### Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Health Check |
| GET | /deals | Fetch Deals data |
| POST | /ask | Ask business questions |

---

## Sample Questions

- How many deals are there?
- How many work orders are there?
- Which sector has the highest number of deals?
- What is the execution status?
- What is the billing status?
- Summarize the business for the CEO.
- Are there any data quality issues?
- What should leadership focus on?

---

## Data Handling

The application automatically:

- Cleans inconsistent data
- Handles missing values
- Normalizes text fields
- Reports data quality issues
- Generates business metrics

The Deals and Work Orders datasets are retrieved dynamically from monday.com. Since they do not contain a reliable common unique identifier for record-level joins, the application analyzes each dataset independently while combining insights where appropriate using shared business dimensions.

---

## Assumptions

- monday.com API credentials are valid.
- Required boards are accessible.
- Users ask business-related questions in natural language.

---

## Future Improvements

- Advanced cross-board analytics
- Interactive dashboards and charts
- Authentication and role-based access
- Conversation history
- Export business reports
- Multi-board scalability

---

## Author

**Priya K P**

B.E. Information Science & Engineering

BNM Institute of Technology