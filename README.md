# LinkShort - URL Shortener

A modern URL shortener built with Flask and SQLite featuring a sleek glass-morphism design.

## ✨ Features

- **Fast URL shortening** with 5-character random codes
- **Modern responsive UI** with animations and glass effects
- **One-click copy** and social sharing
- **SQLite database** for lightweight storage
- **No authentication required**

## 🚀 Quick Start

1. **Install Flask**
```bash
pip install flask
```

2. **Run the app**
```bash
python app.py
```

3. **Open browser**
Navigate to `http://127.0.0.1:5000/`


## 🔧 How It Works

1. Enter long URL → Generate 5-char code → Store in database → Return short URL
2. Visit short URL → Lookup in database → Redirect to original URL

## 🎯 API Endpoints

- `GET /` - Home page
- `POST /` - Shorten URL
- `GET /result` - Show result
- `GET /<short_url>` - Redirect to original

## 🎨 Tech Stack

- **Backend**: Flask, SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Design**: Glass-morphism, CSS animations

## 📱 Responsive Design

Works on desktop, tablet, and mobile with touch-friendly controls.

## 🔧 Customization

Change URL length in `app.py`:
```python
k = 5  # Change this value
```

## 🤝 Contributing

1. Fork repo
2. Create feature branch
3. Submit pull request

---

**Made with ❤️ - Transform long URLs into short, shareable links**