# PiSync Backend

A lightweight Django backend to collect and manage sync events from PiBook and PiBox devices.

---

## 📦 Features

✅ Store sync events with device_id, timestamp, files synced, errors, internet speed  
✅ Retrieve sync history for any device  
✅ Find devices with repeated sync failures (>3)  
✅ Bonus: Console notification when a device fails 3 times **in a row**

---

## 🚀 Setup Instructions

1️⃣ Clone the repository:

-git clone <repo-url>
-cd pisync_backend

2️⃣ Create a virtual environment:

-python3 -m venv venv
-source venv/bin/activate

3️⃣ Install dependencies:

-pip install -r requirements.txt

4️⃣ Apply migrations:

-python manage.py makemigrations
-python manage.py migrate

5️⃣ Run the development server:

-python manage.py runserver

🔗 API Endpoints
➤ Create sync event
-POST /api/sync-event/

Request body:

{
    "device_id": "device123",
    "timestamp": "2025-05-07T10:00:00Z",
    "total_files_synced": 10,
    "total_errors": 0,
    "internet_speed": 5.6
}

➤ Get sync history for device
-GET /api/device/<device_id>/sync-history/

Response:

[
    { "device_id": "device123", "timestamp": "...", ... },
    ...
]

➤ Get devices with repeated failures
-GET /api/devices/repeated-failures/

Response:

[
    { "device_id": "device123", "timestamp": "...", ... },
    ...
]

⚡ Bonus: 3 consecutive failure notification

When a device sends 3 sync events in a row with total_errors > 0,
the backend prints this to the console:

⚠️ Device device123 has failed 3 times in a row!
📈 Scaling Strategy
-Use PostgreSQL + add indexes on device_id, timestamp

-Allow batch event ingestion (bulk_create)

-Add Redis or RabbitMQ + Celery for async processing

-Cache repeated failure queries with Redis

-Scale backend horizontally with load balancers

-Use monitoring tools (Grafana, Prometheus) and autoscaling

🛠 Tech Stack

-Django 4.x

-Django REST framework

-SQLite (development), PostgreSQL (recommended for production)

-Optional: Celery, Redis for background tasks

