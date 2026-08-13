# 🤖 AI Info Generator

### AI-Powered Chat Application with Groq & OpenAI

**A modern AI chat application built with Streamlit, featuring authentication, persistent chat history, file and image attachments, and support for Groq and OpenAI models.**

**🤖 Generative AI • 💬 AI Chat • 📁 File Uploads • 🗄️ SQLite • ⚡ Streamlit • 🔌 API Integration**

---

## 🚀 Live Demo

🌐 **Try the application:**
https://ai-info-generator.streamlit.app/

> 💡 The application is deployed using Streamlit and can be accessed directly from the browser.

---

# 🧭 Overview

**AI Info Generator** is a full-featured AI chat application designed to provide an interactive conversational experience through a modern, Gemini-inspired interface.

The application integrates **Groq** and **OpenAI** models, allowing users to select their preferred AI model while interacting with the chatbot.

The application also supports **file and image attachments directly inside the chat composer**, making it possible to provide additional context to the AI while having a conversation.

The project focuses on creating a clean, practical and user-friendly AI assistant rather than simply providing a basic API wrapper.

---

# 🎯 Project Objectives

The main objectives of this project are to:

* 🤖 Build a functional AI-powered chat application
* 🔌 Integrate Groq and OpenAI APIs
* 💬 Create a modern conversational interface
* 🔐 Implement user login and signup
* 🗄️ Store chat history using SQLite
* 📁 Support file attachments inside the chat composer
* 🖼️ Support image uploads
* 📄 Allow users to upload documents for AI interaction
* 🔄 Allow users to switch between supported AI models
* ⚡ Build a responsive Streamlit-based interface
* 🧠 Provide a smooth and practical AI chat experience

---

# ✨ Features

## 💬 AI Chat

The application provides a conversational AI interface where users can interact with supported AI models.

Users can send messages and receive AI-generated responses through the chat interface.

---

## 🤖 Multiple AI Models

The application currently supports:

### 🟠 Groq

**Model:**

`openai/gpt-oss-120b`

### 🟢 OpenAI

**Model:**

`gpt-5.6`

Users can select the model they want to use from the application interface.

---

## 🔐 Login & Signup

The application includes user authentication functionality.

Users can:

* 📝 Create an account
* 🔑 Log in
* 👤 Access their own conversations
* 🔒 Keep their chat history associated with their account

---

## 🗄️ Persistent Chat History

Chat conversations are stored using **SQLite**.

This allows conversations to persist instead of disappearing when the application session ends.

The database is automatically created when the application starts.

```text
info_generator.db
```

---

## 📁 File Attachments

Users can upload files directly from the chat composer.

Supported file types include:

```text
PDF
TXT
DOCX
PNG
JPG
JPEG
WEBP
```

This makes it possible to provide documents and images as additional context during conversations.

---

## 🖼️ Image Uploads

The application supports common image formats including:

* PNG
* JPG
* JPEG
* WEBP

Images can be attached directly through the chat interface.

---

## 🎨 Modern Chat Interface

The application uses a **Gemini-inspired conversational interface** designed to provide a clean and intuitive user experience.

The chat composer includes file attachment functionality directly within the messaging interface.

---

# 🏗️ Application Architecture

```text
                         ┌──────────────────────┐
                         │       User           │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │  Streamlit Frontend  │
                         │   Chat Interface     │
                         └──────────┬───────────┘
                                    │
                   ┌────────────────┼────────────────┐
                   │                │                │
                   ▼                ▼                ▼
          ┌────────────────┐ ┌───────────────┐ ┌───────────────┐
          │ Authentication │ │ File Uploads  │ │ Chat History  │
          │ Login / Signup │ │ PDF/TXT/DOCX  │ │    SQLite     │
          └────────────────┘ │ Images        │ └───────────────┘
                             └───────┬───────┘
                                     │
                                     ▼
                           ┌────────────────────┐
                           │   Model Selection  │
                           └─────────┬──────────┘
                                     │
                         ┌───────────┴───────────┐
                         │                       │
                         ▼                       ▼
                 ┌───────────────┐       ┌───────────────┐
                 │     Groq      │       │    OpenAI     │
                 │ gpt-oss-120b  │       │    gpt-5.6     │
                 └───────┬───────┘       └───────┬───────┘
                         │                       │
                         └───────────┬───────────┘
                                     ▼
                           ┌────────────────────┐
                           │   AI Response      │
                           └────────────────────┘
```

---

# 🔄 Application Workflow

```text
User
 │
 ▼
Login / Signup
 │
 ▼
Open Chat
 │
 ▼
Select AI Model
 │
 ├───────────────┐
 │               │
 ▼               ▼
Groq           OpenAI
 │               │
 └───────┬───────┘
         ▼
   Enter Message
         │
         ▼
 Attach Files / Images
         │
         ▼
    Send Message
         │
         ▼
     AI Processing
         │
         ▼
    AI Response
         │
         ▼
   Save Chat History
         │
         ▼
    Continue Chat
```

---

# 🛠️ Technology Stack

| Technology               | Purpose                            |
| ------------------------ | ---------------------------------- |
| 🐍 **Python**            | Core application development       |
| ⚡ **Streamlit**          | Web application and user interface |
| 🟠 **Groq API**          | AI model integration               |
| 🟢 **OpenAI API**        | AI model integration               |
| 🧠 **LLMs**              | Conversational AI                  |
| 🗄️ **SQLite**           | User and chat history storage      |
| 📄 **PDF / DOCX / TXT**  | Document processing                |
| 🖼️ **PNG / JPG / WEBP** | Image uploads                      |
| 🔐 **Authentication**    | Login and signup                   |
| 🌐 **Streamlit Cloud**   | Application deployment             |
| 🔧 **Git / GitHub**      | Version control                    |

---

# 📂 Supported File Types

The application supports the following file formats:

| Type         | Formats              |
| ------------ | -------------------- |
| 📄 Documents | PDF, DOCX, TXT       |
| 🖼️ Images   | PNG, JPG, JPEG, WEBP |

---

# 📁 Project Structure

```text
AI-Info-Generator/
│
├── 📄 app.py
│
├── 📄 requirements.txt
│
├── 📄 .env.example
│
├── 📄 .gitignore
│
├── 🗄️ info_generator.db
│
├── 📄 README.md
│
└── 📁 other application files
```

> `info_generator.db` is created automatically beside `app.py` when the application runs.

---

# 🔑 Environment Variables

The application requires API keys for the supported AI providers.

Create a `.env` file based on `.env.example`.

```env
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
```

⚠️ **Never commit your actual API keys to GitHub.**

Make sure `.env` is included in `.gitignore`.

---

# 💻 Run Locally

## 1️⃣ Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

Move into the project directory:

```bash
cd AI-Info-Generator
```

---

## 2️⃣ Create a virtual environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

---

## 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure environment variables

Copy:

```text
.env.example
```

to:

```text
.env
```

Then add your API keys.

---

## 5️⃣ Start the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

# ☁️ Deployment

The application is deployed using **Streamlit**.

### Live Application

🌐 https://ai-info-generator.streamlit.app/

For deployment, configure the required API keys using the deployment platform's secrets/environment-variable system rather than uploading your `.env` file.

---

# 🔒 Security

The project follows basic API-key security practices.

* 🔐 API keys are stored using environment variables
* 🚫 `.env` should not be committed to GitHub
* 🔑 API credentials should be configured separately during deployment
* 🗄️ User/chat information is stored using SQLite

> **Important:** Never publish API keys directly inside source code or commit them to a public repository.

---

# 🎨 User Interface

The application provides a modern chat experience inspired by contemporary AI assistants.

### Interface includes:

* 💬 Conversational chat
* 📎 File attachment inside composer
* 🖼️ Image attachment
* 🤖 AI model selection
* 🔐 Authentication
* 🗄️ Persistent conversations
* ⚡ Streamlit-powered interface

---

# 🌟 Key Highlights

```text
🤖 Multi-Model AI
        │
        ├── Groq
        │   └── openai/gpt-oss-120b
        │
        └── OpenAI
            └── gpt-5.6

💬 Modern Chat Interface
        │
        ├── Conversations
        ├── Attachments
        └── Model Selection

📁 File Support
        │
        ├── PDF
        ├── TXT
        ├── DOCX
        ├── PNG
        ├── JPG
        ├── JPEG
        └── WEBP

🗄️ Persistent Storage
        │
        └── SQLite
```

---

# 🚀 Future Improvements

Potential future improvements include:

* 🧠 More AI model integrations
* 💾 Improved conversation management
* 📂 Better document processing
* 🔎 Conversation search
* 🗂️ Chat organization
* 🎙️ Voice input and output
* 🌐 Additional deployment options
* 👤 Improved account management
* 📊 Usage analytics
* ⚙️ Advanced AI configuration

---

# 📸 Demo

> Add screenshots or GIFs of the application here.

Example:

```markdown
![AI Info Generator](screenshots/home.png)
```

You can create a `screenshots` folder and add images of:

```text
screenshots/
│
├── login.png
├── chat.png
├── file-upload.png
└── model-selection.png
```

---

# 📌 Project Information

**Project:** AI Info Generator
**Category:** Generative AI / AI Chatbot
**Framework:** Streamlit
**Language:** Python
**Database:** SQLite
**AI Providers:** Groq & OpenAI
**Deployment:** Streamlit Cloud

---

# 👨‍💻 Author

## Samarth Sehdev

🎓 Computer Science Engineering Graduate

💻 Full-Stack Developer
🤖 AI / ML Enthusiast
🚀 Software & AI Application Builder

### 🌐 Connect With Me

[![GitHub](https://img.shields.io/badge/GitHub-samarth87-181717?style=for-the-badge\&logo=github)](https://github.com/samarth87)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Samarth_Sehdev-0077B5?style=for-the-badge\&logo=linkedin\&logoColor=white)](https://www.linkedin.com/in/samarth-sehdev-36039726a/)

[![Email](https://img.shields.io/badge/Email-samarthsehdev502%40gmail.com-D14836?style=for-the-badge\&logo=gmail\&logoColor=white)](mailto:samarthsehdev502@gmail.com)

---

<div align="center">

### ⭐ If you find this project interesting, consider giving it a star!

**Built with ❤️ using Python, Streamlit, Groq & OpenAI**

</div>
