# 🥗 NutriScan  

[![Cloud Run](https://img.shields.io/badge/Deployed-Google%20Cloud%20Run-blue)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-Production%20API-green)]()
[![Architecture](https://img.shields.io/badge/Architecture-Sequential%20Multi--Agent-purple)]()

**Multi-Agent Nutrition Analysis System**  
Built for the **Google Cloud Run Hackathon**

---

## 🚀 Overview

NutriScan is a cloud-native, multi-agent system that analyzes food images and returns structured nutrition estimates in ~6 seconds.

The project demonstrates:

- Multi-agent orchestration using Google ADK  
- Production-ready API deployment on Google Cloud Run  
- Modular AI system design  
- End-to-end integration from mobile frontend to scalable backend  

---

## 🎥 Demo

[![NutriScan Demo](https://img.youtube.com/vi/4EbKh5Ua81w/maxresdefault.jpg)](https://youtu.be/4EbKh5Ua81w?si=7TsdbIrIhyHIAPiU)


---

## 🧠 Architecture & Design
```
NutriScan follows a **sequential agent pipeline**:

Frontend (React Native)
↓
Cloud Run (FastAPI Backend)
↓
Vision Agent → Nutrition Analysis Agent
↓
Structured JSON Response
```

### Vision Agent
- Extracts structured food labels from image input  

### Nutrition Analysis Agent
- Maps detected food items to calorie & macronutrient estimates  
- Returns consistent, schema-controlled output  

This separation improves:
- Maintainability  
- Interpretability  
- Extensibility  

---

## ☁️ Cloud Deployment

- Containerized with Docker  
- Deployed on Google Cloud Run  
- Stateless API design  
- Scalable, managed infrastructure  

Average inference latency: **~6 seconds**

---

## ⚙️ Tech Stack

**Backend**
- Python  
- FastAPI  
- Google Agent Development Kit (ADK)  
- Docker  
- Google Cloud Run  

**Frontend**
- React Native  
- Camera integration  

---

## 📂 Project Structure
```
nutriscan_agent/
│
├── sub_agents/
│ ├── vision_agent/
│ └── nutrition_analysis_agent/
│
├── agent.py # Sequential orchestrator
├── requirements.txt
└── README.md
```

---

## 🧪 Example API Response

```json
{
  "food_items": ["Grilled Chicken", "Rice", "Broccoli"],
  "nutrition_estimate": {
    "calories": 520,
    "protein_g": 42,
    "carbs_g": 55,
    "fat_g": 18
  }
}
```

---
## 🐳 Run Locally
```
pip install -r requirements.txt
uvicorn agent:app --reload
```
---

## ☁️ Deploy to Cloud Run
```
gcloud builds submit --tag gcr.io/PROJECT-ID/nutriscan
gcloud run deploy nutriscan \
  --image gcr.io/PROJECT-ID/nutriscan \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```
