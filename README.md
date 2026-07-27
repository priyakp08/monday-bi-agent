# Monday.com Business Intelligence Agent

## Project Overview

The Monday.com Business Intelligence Agent is an AI-powered web application that enables founders and business leaders to ask natural language questions about their business data stored in monday.com.

The application retrieves live data from monday.com boards, cleans and processes the information, calculates business metrics, and generates meaningful insights using a hybrid approach that combines deterministic Python analytics with AI-generated summaries.

This solution was developed as part of the **Skylark Drones Full Stack Technical Assignment**.

---

# Features

- Live integration with monday.com using the GraphQL API
- Dynamic retrieval of Deals and Work Orders data
- Automatic data cleaning and normalization
- Graceful handling of missing and incomplete data
- Natural language business question answering
- Executive business summaries
- Business metrics generation
- Data quality reporting
- Modern React-based conversational interface
- Suggested business questions
- Responsive frontend

---

# Tech Stack

## Frontend

- React
- Vite
- Axios
- CSS

## Backend

- FastAPI
- Python
- Pandas
- Requests
- Pydantic

## AI

- Hugging Face Inference API (Qwen Model)

## External Platform

- monday.com GraphQL API

---

# Architecture

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

# Project Structure

```
monday-bi-agent/

│
├── backend/
│   ├── app.py
│   ├── monday_client.py
│   ├── data_cleaner.py
│   ├── metrics.py
│   ├── ai_agent.py
│   ├── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── api.js
│   │   └── main.jsx
│   ├── package.json
│
├── README.md
└── Decision_Log.md
```

---

# Installation

## Clone the Repository

```bash
git clone <repository-url>
```

---

## Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Health Check |
| GET | /deals | Fetch Deals Data |
| POST | /ask | Ask Business Questions |
| GET | /board-info/deals | Deals Board Information |
| GET | /board-info/workorders | Work Orders Board Information |

---

# Sample Questions

- How many deals are there?
- How many work orders are there?
- Which sector has the highest number of deals?
- What is the execution status?
- What is the billing status?
- Summarize the business for the CEO.
- Are there any data quality issues?
- What should leadership focus on?

---

# Approach

The application follows these steps:

1. Connect to monday.com using the GraphQL API.
2. Retrieve data from the Deals and Work Orders boards.
3. Clean and normalize the retrieved data.
4. Compute business metrics using Python and Pandas.
5. Send the processed business context along with the user's question to the AI model.
6. Generate concise business insights.
7. Display the response through the React frontend.

---

# Data Handling

The application automatically:

- Cleans inconsistent data
- Handles missing values
- Normalizes text fields
- Reports data quality issues
- Generates business metrics

The Deals and Work Orders datasets are retrieved dynamically from monday.com. Since they do not contain a reliable common unique identifier for record-level joins, the application analyzes each dataset independently while combining insights where appropriate using shared business dimensions.

---

# Assumptions

- monday.com API credentials are valid.
- Required boards are accessible.
- Users ask business-related questions.
- Network connectivity is available.
- API responses follow the expected schema.

---

# Trade-offs

Several design decisions were made to keep the application simple and maintainable.

- Business data is processed in memory using Pandas instead of storing it in a database.
- Real-time data is fetched from monday.com for each request to ensure fresh information, although this increases API calls.
- AI-generated summaries are combined with deterministic Python calculations to provide both flexibility and reliable business metrics.
- The frontend and backend are deployed separately on Render, improving modularity while requiring CORS configuration.

---

# AI Tools Used

The following AI tools were used during development:

- **Hugging Face Inference API (Qwen Model)** for generating business insights and answering natural language questions.
- **ChatGPT** for debugging deployment issues, refining project architecture, troubleshooting API integration, and improving project documentation.

---

# Challenges Faced

Some of the key challenges encountered during development include:

- Understanding monday.com GraphQL responses.
- Cleaning nested and inconsistent business data.
- Designing prompts that generate useful business insights.
- Integrating React with FastAPI.
- Configuring CORS between separately deployed frontend and backend services.
- Deploying both applications on Render and resolving deployment-related issues.
- Connecting the deployed frontend to the deployed backend successfully.

---

# Deployment

## Frontend

- React application deployed on **Render**.

## Backend

- FastAPI application deployed on **Render**.

---

# Future Improvements

- Advanced cross-board analytics
- Interactive dashboards and visualizations
- Authentication and role-based access control
- Conversation history
- Export reports as PDF or Excel
- Caching frequently requested business metrics
- Multi-board scalability
- Improved AI prompt optimization
- Enhanced error handling and logging

---

# Conclusion

The Monday.com Business Intelligence Agent demonstrates how AI can be integrated with monday.com to provide natural language access to business data. By combining deterministic analytics with AI-generated summaries, the application delivers meaningful business insights through a simple and intuitive interface while maintaining a modular and scalable architecture.
