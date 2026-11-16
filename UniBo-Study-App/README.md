# UniBo AI Master – Interactive Study Hub & Strategy Coach App

A custom-built, modern local desktop web application for your first semester of the Master's Degree in Artificial Intelligence at the Università di Bologna (UniBo).

---

## Features

1. **Course & Exam Explorer:**
   - Real official course names, professors, credit amounts (CFU), and room numbers.
   - Exact exam dates and AlmaEsami registration windows.
   - Real-time countdown timer to your nearest exam (December 21, 2026).

2. **In-App Interactive PDF Reader:**
   - Browse all 86 lecture slides, lab code packages, and exercise solutions.
   - Click any PDF to immediately view it directly inside the app without opening separate windows.
   - Checkbox tracking: "Mark Completed" updates your course progress and global degree completion percentage.
   - Personal study notes: add and save notes for any lecture slide.

3. **Integrated Gemini AI Strategy Coach:**
   - Pre-configured with your Gemini API Key.
   - **Context-Aware:** It knows your exact live study progress (how many files you've finished in each course), your upcoming exam dates, and which PDF you are currently reading!
   - Ask for customized day-by-day study plans, algorithm explanations, or practice quizzes.

4. **Sleek, Eye-Friendly Dark Theme:**
   - Designed with high-contrast, comfortable slate/zinc surfaces for fatigue-free studying.

---

## How to Start the App

Double-click **`start-study-app.bat`** in your main `UniBo` folder (or `start-app.bat` inside this folder).  
The app will launch its server and automatically open **`http://localhost:3000`** in your default web browser!



---

## 📱 Mobile & Remote Access (Study From Anywhere on Your Phone)

The entire application is optimized with a **Mobile-First Tactical Architecture**:
- **Mobile Single-Pane Navigation**: Full-width slides with pinch-zoom, and an obsidian bottom navigation bar to switch seamlessly between `[ 🗂️ Materials ]`, `[ 📄 Slides ]`, and `[ 💬 AI Copilot ]`.
- **Dynamic Viewport (`dvh`)**: Virtual keyboard safe spacing preventing input occlusion on iOS Safari and Android Chrome.
- **LaTeX Math Rendering**: Mobile-optimized KaTeX formulas with horizontal scrolling.

### 1. Instant Wi-Fi Access (At Home / Study Desk)
If your phone is connected to the same Wi-Fi network as your PC:
1. Ensure the server is running (`npm start` or `node UniBo-Study-App/server.js`).
2. On your phone, open your browser and navigate to:
   ```
   http://192.168.1.54:3000
   ```
   *(Or click **[ 📱 Phone Access ]** in the top header and scan the live QR code with your iPhone or Android camera!)*

### 2. Worldwide Remote Access via Secure Tunnel (Anywhere on 4G / 5G)
Access your local setup with all 430MB of slides and your AI Copilot from outside your home:
- **One-Click on Windows**: Double-click `start_remote_tunnel.bat` in the project root.
- **Or via Terminal**:
  ```bash
  npm run tunnel
  # or
  npx localtunnel --port 3000
  ```
- It gives you a public HTTPS URL (e.g., `https://xxxx.loca.lt`) to open on your phone anywhere in the world!

### 3. Permanent 24/7 Cloud Hosting (Render / Railway)
To keep the app online 24/7 even when your computer is turned off:
1. Push this directory to a GitHub repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit of UniBo AI Master Hub"
   git branch -M main
   git remote add origin https://github.com/<your-username>/unibo-ai-master.git
   git push -u origin main
   ```
2. Go to [Render.com](https://render.com) (free) or [Railway.app](https://railway.app).
3. Connect your GitHub repository.
4. Render will automatically detect `render.yaml` or use `npm start` with zero configuration needed.
5. Your custom URL (e.g. `https://unibo-study.onrender.com`) is live 24/7!
