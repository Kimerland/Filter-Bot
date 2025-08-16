# ⛓️‍💥 Filter-Bot 

![Filter-Bot](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjE1bGVlNXBqcHZ4bnEycG9yd245azNnNnB5OWp0ZnczZWZhZWllbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VDMHgvx8N9U7UUlczQ/giphy.gif)  

Filter-Bot is a modern telegram-bot solution for filter messages built with Python + [Aiogram 3.0](https://docs.aiogram.dev/en).

---

## 📌 Tech Stack  
- 🐍 Python + Aiogram – Simple framework for fast start 
- 📅 [Prisma](https://prisma-client-py.readthedocs.io/en/stable/) (python version) – Work with DB 
- 🫂 [G4f](https://github.com/xtekky/gpt4free) – API requests for free AI  
- 👨‍💻 PostgreSQL - Favourite DB  

---

## 📖 Installation  

### 1️⃣ Clone the repository 
```bash
git clone https://github.com/Kimerland/Filter-Bot.git
```
```bash
cd Filter-Bot
```

---

### 2️⃣ Create a virtual ENV

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

The first it's node modules:

```bash
npm install
```

Others:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

My problem in case - If aiogram or g4f are not installed, download manually:

```bash
pip install aiogram
pip install g4f
```

---

### 4️⃣ Create DB

Install PostgreSQL (Example DB):

macOS (Homebrew):

```bash
brew install postgresql
brew services start postgresql
```

Windows:

```bash
Download installer from postgresql.org/download and install.
```

Create a database:

```bash
psql -U postgres
CREATE DATABASE filterbot;
```

Update your .env file:

```bash
DATABASE_URL="postgresql://postgres:your_password@localhost:5432/filterbot"
```

---

### 5️⃣ Install Prisma

Install Prisma CLI(global):

```bash
npm install -g prisma
```

Install Python client:

```bash
pip install prisma
```

Generate client:
```bash
prisma generate
```

Apply migrations:
```bash
prisma migrate dev --name init
```

---

### 🛠 Additional Commands

📦 Build the project
```bash
source venv/bin/activate
```
```bash
venv\Scripts\activate
```
```bash
python main.py
```

---
### 📢 Contact

👤 Author: Kimerland
📧 Email: kimerland.project@gmail.com
🐙 GitHub: Kimerland

---

### ⭐️ If you like this project, please give it a star!
