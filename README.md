# Python-Django-QR-Code-Generator

This is a simple yet professional web application that allows users to generate personalized QR codes easily. Built with Django, it includes user authentication features such as registration, login, and logout, ensuring secure access. The app is designed with a clean, modern interface and is suitable for both personal and professional use.

---

# Features

- **User Registration & Login:** Create an account or sign in to access the QR code generator.
- **Secure Access:** Only logged-in users can generate QR codes.
- **Custom QR Code Generation:** Enter any text or URL to generate a unique QR code.
- **Downloadable QR Code:** Save your generated QR code as an image file directly from the website.
- **Responsive Design:** Looks great on both desktop and mobile devices.

---

## Technologies Used

- **Django:** Python-based web framework for rapid development.
- **qrcode:** Python library to generate QR code images.
- **HTML/CSS:** For designing a user-friendly interface.
- **JavaScript:** Enhancing user interactions (optional, minimal use here).

---

## How to Use

### 1. Setup Your Environment

Before running the app, ensure you have Python installed on your computer. Then, follow these steps:

```bash
# Clone the repository
git clone https://github.com/yourusername/qr-code-generator.git

# Navigate into the project folder
cd qr-code-generator

# Create a virtual environment
python -m venv env

# Activate the virtual environment
# On Windows:
env\Scripts\activate
# On MacOS/Linux:
source env/bin/activate

# Install required dependencies
pip install -r requirements.txt
```

### 2. Run the Application

```bash
# Apply database migrations
python manage.py migrate

# Create a superuser (admin account)
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

Open your browser and go to `http://127.0.0.1:8000/`. You can now register an account or log in to generate QR codes.

### 3. Generate a QR Code

- Log in with your credentials.
- Enter any text or URL into the input box.
- Click the "Generate" button.
- Your QR code will appear below.
- Click "Download" to save the QR code image.

---

## Deployment & Customization

- To deploy this app online, consider hosting on platforms like Heroku, PythonAnywhere, or AWS.
- Customize the interface by editing the HTML and CSS files.
- Add more features such as saving history, sharing QR codes, or customizing QR code styles.

---

## Note

- This project is intended for learning and demonstration purposes.
- Ensure you replace placeholder URLs and customize the project as needed for professional deployment.

---

## Contact

If you have any questions or need further customization, feel free to contact me via jithinchandran527@gamil.com .

---

**Happy QR coding!**
