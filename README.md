# 🚀 KPCL AI Chatbot (S.A.N.E.-AI)

A powerful AI-driven chatbot designed for **Kirloskar Pneumatic Company Limited (KPCL)** to analyze warranty claims, query knowledge bases, and perform cost analysis for spare parts. Built with a modern tech stack focusing on speed, accuracy, and interactive data visualization.

---

## 🌟 Key Features

- **📊 Warranty Analysis**: Automatically process and visualize warranty claims from master datasets.
- **🔍 Knowledge Base Query**: Interact with internal technical documentation and knowledge bases.
- **💰 Cost Analysis**: Analyze spare part costs and financial data using AI-driven insights.
- **📈 Dynamic Visualization**: Interactive charts and data representations using Plotly and React.
- **🤖 Multi-Model Support**: Integrated with **Google Gemini 1.5 Flash** for cloud-based reasoning and **Ollama** for local backup.
- **🧠 Intelligent Agents**: Dedicated `Code Agent` for complex data parsing and decision-making.

---

## 🛠️ Tech Stack

### Backend
- **FastAPI**: High-performance Python web framework.
- **Uvicorn**: Lightning-fast ASGI server.
- **Pydantic**: Robust data validation and settings management.
- **LangChain**: Framework for building LLM-powered applications.
- **Pandas & Openpyxl**: Advanced data manipulation and Excel processing.

### Frontend
- **React (Vite)**: Modern frontend development environment.
- **Tailwind CSS**: Utility-first CSS framework for premium UI/UX.
- **Lucide React**: Beautiful icons for a professional interface.
- **Plotly.js**: Interactive data visualization.
- **Axios**: Promised-based HTTP client for API communication.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Node.js 18+
- Google Gemini API Key (or local Ollama setup)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/sanskrutipasalkar10/kpcl-chatbot.git
   cd kpcl-chatbot
   ```

2. **Backend Setup**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
   Create a `.env` file in the root directory (one level above `backend/`) and add your API keys:
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   MODEL_NAME=gemini-1.5-flash
   ```

3. **Frontend Setup**
   ```bash
   cd ../frontend
   npm install
   ```

### Running the Application

1. **Start the Backend**
   ```bash
   cd backend
   python main.py
   ```
   The backend will be available at `http://localhost:8000`.

2. **Start the Frontend**
   ```bash
   cd frontend
   npm run dev
   ```
   Open `http://localhost:5173` in your browser.

---

## 📁 Project Structure

```text
kpcl-chatbot/
├── backend/
│   ├── app/
│   │   ├── agents/          # AI Agent logic (Code Agent, prompts)
│   │   ├── api/             # API routes and endpoints
│   │   ├── core/            # Configuration and security settings
│   │   ├── models/          # Data models and schemas
│   │   └── services/        # Business logic (Parser, Chart Gen)
│   ├── data/
│   │   └── raw/             # Excel datasets (Warranty, Cost, KB)
│   ├── logs/                # API and Agent execution logs
│   ├── main.py              # Application entry point
│   └── requirements.txt     # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/      # UI components (Chat, Layout, Charts)
│   │   ├── assets/          # Static assets
│   │   ├── services/        # API communication logic
│   │   └── App.jsx          # Main React application
│   ├── package.json         # Node.js dependencies
│   └── vite.config.js       # Vite configuration
├── .env                     # Environment variables (AI keys)
├── .gitignore               # Git ignore rules
└── README.md                # Project documentation
```

---

## 🤝 Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

**Developed for KPCL with ❤️ by [Sanskruti Pasalkar](https://github.com/sanskrutipasalkar10)**


<img width="1868" height="959" alt="image" src="https://github.com/user-attachments/assets/310e8d42-1ede-4fed-90ff-9f1c6ff256f7" />
<img width="1897" height="965" alt="image" src="https://github.com/user-attachments/assets/8848a61d-7cb6-40a4-a09f-b335e37181c4" />
<img width="1905" height="975" alt="image" src="https://github.com/user-attachments/assets/8aa5ce39-3648-45fb-95c1-1224c21d79c7" />
<img width="1892" height="991" alt="image" src="https://github.com/user-attachments/assets/c858bdbc-37dd-4dfe-97db-7dc2d1e00092" />
