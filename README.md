# 💄 makeup_project

A beautifully designed **portfolio website** for a professional makeup artist. Built using **Python, Django, Bootstrap, and HTML**, this site showcases services, a contact form, a gallery, and other relevant details — all in one elegant web interface.

---

![My Site Banner](https://i.postimg.cc/3xmTtNSf/shamblen-studios-xw-M61-TPMl-Yk-unsplash.jpg)


> 🎥 **Demo Video:** 
[click here](https://github.com/user-attachments/assets/fc744e9b-58c9-4eb7-bb79-8ace3720f935)



---

## 📌 Features

- 🖼️ Image gallery showcasing makeup looks
- 📞 Contact page with form submission
- 💼 Services section for detailing packages
- 📱 Responsive design using Bootstrap
- 🔐 Django Admin panel for easy content management

---

## 🛠️ Tech Stack

| Layer        | Technology             |
|--------------|------------------------|
| **Backend**  | Python, Django 4.x     |
| **Frontend** | Bootstrap 5, HTML5, CSS3 |
| **Database** | SQLite (`db.sqlite3`)  |
| **Others**   | Django Admin, Form Handling

---


---

## ⚙️ Installation & Local Setup

```bash
# Clone the repository
git clone https://github.com/ankit1350/makeup_project.git
cd makeup_project

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate     # On Linux/Mac
venv\Scripts\activate        # On Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver

