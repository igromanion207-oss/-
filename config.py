import os


class Config:
    """Настройки сайта. Меняйте значения здесь — шаблоны подхватят их сами."""

    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-change-me")

    SITE_NAME = "Xagan6_9"
    SITE_TAGLINE = "Python-разработчик"
    SITE_DESCRIPTION = "Портфолио Xagan6_9: проекты на Python, боты, автоматизация и веб."
    SITE_URL = os.environ.get("SITE_URL", "http://127.0.0.1:5000")

    # Замените ссылки на свои
    SOCIAL = {
        "GitHub": "https://github.com/Xagan6_9",
        "Telegram": "https://t.me/Xagan6_9",
        "Email": "mailto:you@example.com",
    }

    SKILLS = {
        "Языки": ["Python", "SQL", "HTML/CSS", "JavaScript"],
        "Фреймворки": ["Flask", "Django", "FastAPI", "aiogram"],
        "Инструменты": ["Git", "Docker", "Linux", "PostgreSQL"],
    }

    # Настройки Frozen-Flask (сборка статической версии сайта)
    FREEZER_DESTINATION = "../build"
    FREEZER_RELATIVE_URLS = False
    # Полный адрес сайта: если он в подпапке (user.github.io/repo/), ссылки получат этот префикс
    FREEZER_BASE_URL = SITE_URL
