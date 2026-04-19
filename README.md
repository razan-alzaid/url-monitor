# 🌐 URL Monitoring System (Dockerized)

A full-stack URL monitoring system built using Docker, Flask, MongoDB, and Nginx.

## 🚀 Features

* Add and monitor URLs
* Background worker checks status & response time
* Real-time dashboard
* Fully dockerized multi-container architecture
* Reverse proxy to solve CORS issues

## 🧱 Tech Stack

* Backend: Flask (Python)
* Frontend: HTML + Nginx
* Database: MongoDB
* Worker: Python
* DevOps: Docker & Docker Compose

## 🐳 Run the Project

docker-compose up --build

## 🌐 Access

Dashboard: http://localhost:3000

## 🧠 Architecture

Frontend (nginx) → API (Flask) → MongoDB
↓
Worker

## ✨ Highlights

* Solved real-world CORS issue using reverse proxy
* Built a distributed multi-container system
* Implemented background processing

## 👩‍💻 Author

Razan Alzaid
