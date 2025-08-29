# Drone-project-
AI Robotics using opencv
# 🚁 Drone Project – Keyboard Control, Live Video, Image Capture & Face Tracking

This project demonstrates a drone (or webcam)-based vision system with real-time video capture, keyboard control for interaction, face tracking using OpenCV, and the ability to capture and save images using keyboard input.

---

## 🔄 Project Flow

1. 🎮 **Keyboard Control** – Press keys to interact (e.g., save frames, quit)
2. 📸 **Live Video Capture** – Real-time stream from webcam (or drone camera)
3. 🖼️ **Image Capture** – Press a key to take a snapshot
4. 💾 **Image Save** – Images are saved to the `Resources/` folder
5. 😃 **Face Tracking** – Detect and highlight faces using Haarcascade

---

## 🛠️ Technologies Used

- **Python 3.x**
- **OpenCV**
- **NumPy**
- **pygame**
- **Haarcascade Classifier**
- **Git + GitHub**

---

## 📂 Project Structure
Drone_Project/
│
├── Resources/ # Contains haarcascade files and saved images
├── pycache/ # Python cache files
├── README.md # Project documentation
├── basic_movement.py # Module for basic drone movement controls
├── face_tracking.py # Face detection and tracking script
├── image_capture.py # Image capture and saving functions
├── keypress_module.py # Keyboard input handling utilities
├── mapping.py # Mapping inputs to drone commands or functions
├── project_keyboard_img_capture.py # Main script combining keyboard control and image capture
├── test_control.py # Testing drone controls and functions

