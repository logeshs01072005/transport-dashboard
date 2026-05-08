# 🚌 Transport Dashboard

A full-stack transport data management system built with **FastAPI** and **HTML/CSS/JS**.

## 🔗 Live Demo
https://transport-dashboard-5.onrender.com

## 📌 Features
- 📂 Upload CSV or Excel files
- 📊 View transport data in a table
- ✏️ Edit rows directly
- 🗑️ Delete rows
- 🔄 REST API with FastAPI

## 🛠️ Tech Stack
| Frontend | Backend | Deployment |
|----------|---------|------------|
| HTML, CSS, JS | FastAPI, Python | Render |
| | Pandas, OpenPyXL | GitHub |

## 📁 Project Structure
backend/
├── main.py
├── requirements.txt
└── static/
└── transport-dashboard.html

## ⚙️ Run Locally
```bash
# Install dependencies
pip install -r requirements.txt

# Start server
uvicorn main:app --reload
```

## 🌐 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Home dashboard |
| POST | /upload | Upload CSV/Excel |
| GET | /data | Get all data |
| PUT | /update/{index} | Update a row |
| DELETE | /delete/{index} | Delete a row |

## 👨‍💻 Author
**Logesh S** — [GitHub](https://github.com/logeshs01072005

