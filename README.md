# 🖐️ Smart-Hand
A real-time computer vision project that lets you **control your computer’s mouse cursor with hand gestures** using **OpenCV, MediaPipe, and PyAutoGUI**.  
Your webcam detects hand landmarks, and gestures are mapped to mouse actions like clicking, scrolling, and taking screenshots.

---

📸 **Demo**  
Smart-Hand in Action (Add GIF or screenshot here)

---

🚀 **Features**
- 🎯 Move cursor with your index finger  
- 🖱️ Click & Double Click using thumb + index gestures  
- 📜 Scroll with four-finger gesture (up/down)  
- 📸 Take screenshots with a fist gesture  
- 🖼 Live webcam feed with real-time hand landmark tracking  
- ⚡ Lightweight, works on most systems with a webcam  

---

📂 **Project Structure**
smart-hand/
│
├── main.py # Main script to run hand gesture control
├── util.py # Utility functions (angles, distances)
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy code

---

🛠 **Installation & Setup**

1️⃣ Clone this repository  
```bash
git clone https://github.com/yourusername/smart-hand.git
cd smart-hand
2️⃣ Install dependencies
Make sure you have Python 3.7+ installed.
Then install required packages:

bash
Copy code
pip install -r requirements.txt
3️⃣ Run the project
Make sure your webcam is connected and accessible:

bash
Copy code
python main.py
🎮 Gestures & Controls

✋ Move Cursor → Move your index finger

👉 Single Click → Thumb + Index close

👆 Double Click → Quick double tap

✨ Scroll Mode → Raise 4 fingers

Move hand up → Scroll Up

Move hand down → Scroll Down

📸 Screenshot → Make a fist

❌ Exit → Press q

🎨 Customization
Want to add new gestures?

Modify main.py and util.py for custom actions.

Example: Add volume control, brightness adjustment, or app shortcuts.

🚀 Future Improvements

Support for multi-hand gestures

Customizable gesture mappings

Add gesture-based system shortcuts (volume, brightness, app launch)

pgsql
Copy code

👉 This version is **neatly formatted with emojis**, easy to read, and GitHub-ready.  

Do you also want me to **design an ASCII logo/banner** (like “SMART-HAND” in big
