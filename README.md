
# 🖼️ DRF Image Resizer with Celery & Redis

This is a training project to explore **asynchronous background processing** using **Celery** and **Redis** in a Django REST Framework (DRF) application.

## 🚀 Features

- ✅ Upload images via a REST API.
- 🔄 Asynchronously resize uploaded images using **Celery**.
- 📬 Redis is used as the **message broker** between Django and Celery.
- 🐳 Fully containerized with Docker.
- 🌐 API available at: `http://localhost:8000`

---

## 📦 Tech Stack

- **Django** + **Django REST Framework**
- **Celery** for background task processing
- **Redis** as the Celery message broker
- **Docker & Docker Compose** for containerization

---

## 📁 API Endpoints

- `POST /image/upload/` – Upload a new image
- `PUT /image/resize/<image_id>/` – Resize the image asynchronously

---

## ▶️ How to Run

Make sure you have **Docker** and **Docker Compose** installed.

```bash
docker-compose up --build
```

The web app will be running at:  
👉 `http://localhost:8000`

---

## 🛠️ Project Structure

```
convertio/
├── converter/         # Django app with models, views, serializers
├── celery.py          # Celery app configuration
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## 📌 Notes

- This project is intended for educational purposes.
- All image processing tasks are done in the background via Celery.
- You can check Celery logs in the `celery` container for task execution info.

---

## 📃 License

MIT – do whatever you want ✌️
