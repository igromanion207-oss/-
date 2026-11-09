"""Загрузка контента: проекты из YAML и статьи блога из Markdown."""
from functools import lru_cache
from pathlib import Path

import frontmatter
import markdown
import yaml

CONTENT_DIR = Path(__file__).resolve().parent.parent / "content"
MD_EXTENSIONS = ["fenced_code", "codehilite", "tables", "toc"]


def render_md(text: str) -> str:
    """Превращает Markdown-текст в HTML."""
    return markdown.markdown(text, extensions=MD_EXTENSIONS)


@lru_cache
def get_projects():
    with open(CONTENT_DIR / "projects.yaml", encoding="utf-8") as f:
        projects = yaml.safe_load(f) or []
    for p in projects:
        p["description_html"] = render_md(p.get("description", ""))
    return sorted(projects, key=lambda p: p["date"], reverse=True)


def get_project(slug):
    return next((p for p in get_projects() if p["slug"] == slug), None)


@lru_cache
def get_posts():
    posts = []
    for path in (CONTENT_DIR / "posts").glob("*.md"):
        post = frontmatter.load(path)
        if post.get("draft"):
            continue
        posts.append({
            "slug": path.stem,
            "title": post["title"],
            "date": post["date"],
            "summary": post.get("summary", ""),
            "tags": post.get("tags", []),
            "html": render_md(post.content),
        })
    return sorted(posts, key=lambda p: p["date"], reverse=True)


def get_post(slug):
    return next((p for p in get_posts() if p["slug"] == slug), None)


def get_all_tags():
    """Все технологии из проектов — для фильтра на странице проектов."""
    tags = {t for p in get_projects() for t in p.get("stack", [])}
    return sorted(tags, key=str.lower)
