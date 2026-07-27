# Decision Log

## Monday.com Business Intelligence Agent

Author: Priya K P

---

# 1. Project Overview

The objective of this project was to build an AI-powered Business Intelligence Agent capable of answering founder-level business questions using live data from monday.com. The application retrieves information from Deals and Work Orders boards, processes the data, and generates business insights through a conversational interface.

---

# 2. Technology Choices

## Backend

FastAPI was selected because it is lightweight, fast, and well suited for building REST APIs. It also integrates easily with Python libraries used for data processing and AI.

## Frontend

React with Vite was chosen to create a responsive and interactive user interface. Vite provides a faster development experience and simpler project structure.

## AI Model

The Hugging Face Inference API with the Qwen model was used to generate executive summaries and answer analytical business questions.

## Data Processing

Pandas was used for cleaning and preprocessing the data due to its powerful data manipulation capabilities.

---

# 3. Architecture Decision

A hybrid architecture was implemented.

Python handles deterministic business calculations such as:

- Total deals
- Total work orders
- Sector analysis
- Deal stage analysis
- Execution status
- Billing status

The AI model is responsible for:

- Executive summaries
- Business insights
- Leadership recommendations
- Data quality explanations

This approach improves accuracy by preventing the language model from performing calculations directly while still providing natural language responses.

---

# 4. Data Cleaning Strategy

The application performs preprocessing before generating responses.

The cleaning process includes:

- Handling missing and null values
- Normalizing text fields
- Cleaning inconsistent formatting
- Creating business metrics from cleaned data

Whenever incomplete information is detected, the agent communicates this clearly instead of producing misleading answers.

---

# 5. Assumptions

Several assumptions were made during development:

- The monday.com API credentials are valid.
- The required boards are accessible.
- Users ask business-related questions in natural language.
- Missing values represent incomplete business data rather than system errors.

---

# 6. Trade-offs

One important observation was that the Deals and Work Orders datasets do not contain a reliable common unique identifier for record-level joins.

Although both datasets are retrieved dynamically from monday.com, creating artificial relationships between records could produce incorrect business insights.

Instead, the application analyzes each board independently while combining insights using shared business dimensions such as Sector and Owner whenever appropriate.

This decision prioritizes accuracy over unsupported assumptions.

---

# 7. Leadership Updates

The optional leadership update feature was interpreted as generating concise executive summaries rather than displaying raw business data.

The AI summarizes:

- Current pipeline status
- Business performance
- Operational progress
- Data quality concerns
- Recommended focus areas for leadership

This provides founders with quick, decision-oriented insights.

---

# 8. Future Improvements

With additional development time, the following improvements would be implemented:

- Interactive dashboards and charts
- Historical trend analysis
- Conversation history
- User authentication
- Role-based access control
- Advanced cross-board analytics
- Exportable business reports
- Real-time notifications

---

# 9. Conclusion

The final solution successfully integrates monday.com with an AI-powered conversational interface to answer business intelligence queries.

The hybrid architecture combines deterministic analytics with AI-generated explanations, providing accurate metrics alongside meaningful business insights while handling incomplete and inconsistent data gracefully.