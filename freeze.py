"""Сборка статической версии сайта в папку build/ (для GitHub Pages и любого хостинга HTML)."""
from flask_frozen import Freezer

from app import create_app
from app.content import get_posts, get_projects

app = create_app()
freezer = Freezer(app)


# Маршруты лежат в блюпринте "main", поэтому указываем полное имя endpoint
@freezer.register_generator
def project():
    for p in get_projects():
        yield "main.project", {"slug": p["slug"]}


@freezer.register_generator
def post():
    for p in get_posts():
        yield "main.post", {"slug": p["slug"]}


if __name__ == "__main__":
    freezer.freeze()
    print("Готово: статический сайт лежит в папке build/")
