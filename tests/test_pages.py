import pytest

from app import create_app
from app.content import get_posts, get_projects


@pytest.fixture
def client():
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()


@pytest.mark.parametrize("url", ["/", "/projects/", "/blog/", "/about/", "/contact/",
                                 "/sitemap.xml", "/robots.txt"])
def test_pages_open(client, url):
    assert client.get(url).status_code == 200


def test_site_name_on_home(client):
    assert "Xagan6_9" in client.get("/").get_data(as_text=True)


def test_all_projects_render(client):
    for p in get_projects():
        assert client.get(f"/projects/{p['slug']}/").status_code == 200


def test_all_posts_render(client):
    for p in get_posts():
        assert client.get(f"/blog/{p['slug']}/").status_code == 200


def test_404(client):
    assert client.get("/projects/net-takogo/").status_code == 404
