#  AI-Powered Startup Funding Discovery Agent

An AI agent that automatically discovers recently funded startups, enriches company information, and creates a structured database of funding opportunities for job seekers, founders, and investors.

##  Problem Statement

Finding recently funded startups is a manual and time-consuming process. Funding news is scattered across multiple platforms, and users must manually:

- Search funding news websites
- Read long articles
- Extract funding details
- Visit company websites
- Find careers pages

This delays discovering high-growth startups and potential job opportunities.

---

##  Solution

The Startup Funding Discovery Agent automates the entire workflow.

It:

- Scrapes the latest funding news from **Entrackr** and **Inc42**
- Uses **Google Gemini** to extract structured funding information
- Enriches company data with:
  - Industry
  - Headquarters
  - Official Website
  - Careers Page
- Automatically updates a **Google Sheet**
- Provides a simple web interface to trigger the workflow

---

##  Features

- 📰 Weekly funding news scraping
- 🤖 AI-powered funding extraction using Gemini
- 🌐 Automatic company website discovery
- 🏢 Industry & headquarters enrichment
- 💼 Careers page discovery
- 📊 Google Sheets integration
- 🌍 Deployed on Railway
- 🖥️ Simple FastAPI web interface

---

## 🏗️ Tech Stack

### Backend

- FastAPI
- LangGraph
- Python

### AI

- Google Gemini
- LangChain

### Web Scraping

- Requests
- BeautifulSoup
- DDGS

### Storage

- Google Sheets API

### Deployment

- Railway

---

##  Workflow

```text
User
   │
   ▼
Web Interface
   │
   ▼
Scrape Entrackr & Inc42
   │
   ▼
Gemini extracts funding data
   │
   ▼
Company enrichment
(Industry • HQ • Website • Careers)
   │
   ▼
Google Sheets
```

---

##  Project Structure

```
funding_agent/
│
├── app.py
├── graph.py
├── models/
├── nodes/
├── prompts/
├── services/
├── sources/
├── templates/
├── static/
├── credentials/
├── requirements.txt
└── README.md
```

---

##  Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/funding_agent.git
```

Move into the project

```bash
cd funding_agent
```

Create a virtual environment

```bash
python -m venv avenv
```

Activate

Windows

```bash
avenv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

##  Environment Variables

Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

GOOGLE_SHEET_URL=YOUR_GOOGLE_SHEET_URL

GOOGLE_SERVICE_ACCOUNT_JSON=YOUR_SERVICE_ACCOUNT_JSON
```

---

##  Run Locally

```bash
uvicorn app:app --reload
```

Open

```
http://127.0.0.1:8000
```

---

##  Live Demo

**Railway**

```
https://YOUR-RAILWAY-URL.up.railway.app/
```

---

##  Output

The generated Google Sheet contains:

| Date | Company | Funding | Round | Industry | Headquarters | Website | Careers | Source |
|------|----------|----------|--------|----------|--------------|----------|----------|--------|

---
---
##  Author

**Himanshu Pewal**

---

## 📜 License

This project was developed as part of a Buildathon and is intended for educational and demonstration purposes.
