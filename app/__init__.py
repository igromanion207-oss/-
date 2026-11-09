from datetime import date

from flask import Flask, render_template

from config import Config


def create_app(config_class=Config):
    """Фабрика приложения: создаёт и настраивает Flask-приложение."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    from .routes import bp
    app.register_blueprint(bp)

    # Эти переменные доступны в любом шаблоне без передачи из маршрута
    @app.context_processor
    def inject_globals():
        return {
            "site_name": app.config["SITE_NAME"],
            "social": app.config["SOCIAL"],
            "current_year": date.today().year,
        }

    # Фильтр для красивых дат: {{ post.date | ru_date }}
    @app.template_filter("ru_date")
    def ru_date(value):
        months = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля",
                  "августа", "сентября", "октября", "ноября", "декабря"]
        return f"{value.day} {months[value.month - 1]} {value.year}"

    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html"), 404

    return app
