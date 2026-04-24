md
# 🏋️ GymSense AI – AI-Powered Personal Fitness Coaching System

## 🚀 Overview
GymSense AI is a full-stack, AI-powered mobile fitness application designed to act as a smart personal trainer. It provides personalized workout plans, diet recommendations, progress tracking, and AI-based posture correction.

The system is designed using a scalable architecture combining mobile development, backend engineering, and AI integration.

---

## 🎯 Objective
To build an intelligent fitness assistant that:
- Guides users through structured workouts
- Provides personalized diet plans
- Tracks user progress over time
- Uses AI to improve exercise form

---

## 🧠 Key Features

### 🔐 Authentication System
- User registration and login
- Secure password handling
- JWT-based authentication

---

### 👤 User Profile & Fitness Setup
- Collects:
  - Age
  - Height
  - Weight
  - Fitness goals (fat loss / muscle gain)
  - Experience level

- Calculates:
  - BMI
  - Daily calorie needs
  - Macro distribution (Protein, Carbs, Fat)

---

### 🏋️ Workout Planning System
- Multiple workout splits:
  - Full Body
  - Upper/Lower
  - Push Pull Legs
  - Bro Split

- Dynamic workout generation based on:
  - User goal
  - Experience level
  - Available workout time

---

### 📅 Daily Dashboard
Displays:
- Today’s workout plan
- Total workout duration
- Calorie target
- Macro targets

---

### 💪 Exercise Module
- Muscle-based exercise selection
- Each exercise includes:
  - Name
  - Target muscle
  - Sets & reps
  - Video reference

---

### ▶️ Workout Execution Flow
- Start workout session
- Timer tracking
- Rest intervals
- Progress logging

---

### 🤖 AI Posture Correction System
- Upload workout video
- AI analyzes body posture using:
  - OpenCV
  - MediaPipe

- Provides feedback like:
  - “Keep your back straight”
  - “Increase squat depth”

---

### 🏃 Cardio Tracking
- Activities:
  - Running
  - Cycling
- Tracks duration and estimates calories burned

---

### 🥗 Diet & Nutrition System
- Daily calorie calculation
- Macro distribution
- 7-day meal plan generation

---

### 🧠 Smart Diet Suggestions
- Fat loss → High protein recommendations
- Muscle gain → Increased calorie intake
- Low energy → Carb adjustments

---

### 📊 Progress Tracking
- Weight logs
- Workout logs
- Graph-based visualization (planned)

---

### ⚠️ Plateau Detection
- Detects lack of progress
- Suggests:
  - Workout changes
  - Intensity adjustments

---

### 📍 Nearby Gym Finder
- Suggests nearby gyms using location data

---

### 💬 AI Fitness Chatbot
- Answers queries like:
  - “How to do squats?”
  - “Best chest exercises”

---

### 🔔 Notification System
- Workout reminders
- Missed session alerts
- Diet notifications

---

## 🏗️ System Architecture

```

Mobile App (React Native)
↓
Node.js Backend (REST API)
↓
MongoDB Database
↓
Python AI Microservice
(OpenCV + MediaPipe)

```

---

## 🛠️ Tech Stack

### Frontend
- React Native (TypeScript)

### Backend
- Node.js
- Express.js

### Database
- MongoDB

### AI Service
- Python
- OpenCV
- MediaPipe

### Authentication
- JWT (JSON Web Token)

---

## 📂 Project Structure

```

gymsense-ai/
│
├── frontend/
│   ├── App.tsx
│   └── screens/
│
├── backend/
│   ├── server.js
│   ├── routes/
│   ├── controllers/
│   └── models/
│
├── ai-service/
│   ├── app.py
│   └── posture.py
│
├── assets/
├── docs/
└── README.md

```

---

## 🔄 Workflow

1. User interacts with mobile app  
2. Frontend sends request to backend  
3. Backend processes logic  
4. AI service analyzes posture (if required)  
5. Response sent back to frontend  

---

## 🧪 Engineering Practices

- Modular architecture (routes/controllers/services)
- Clean code structure
- RESTful API design
- Async/await handling
- Input validation
- Error handling
- Secure authentication (JWT)

---

## 🚀 Future Enhancements

- Real-time posture correction (live camera)
- Wearable device integration
- Advanced AI recommendations
- Social fitness features
- Leaderboards and challenges

---

## 📸 Screenshots
*(Add screenshots here later)*

```

assets/dashboard.png
assets/workout.png


## 🌍 Deployment (Planned)
- Frontend: Mobile build (APK / Expo)
- Backend: Cloud deployment
- AI Service: Python microservice server

---

## 👨‍💻 Author
Gnanesh Charlin A

## Email
gnanesh1charlin2gmail.com

---

## 📜 License
This project is for educational and portfolio purposes.



