import pytest

# Skip these tests if Flask isn't installed in the test environment
pytest.importorskip('flask')
import app


def test_index_route_renders_template():
    with app.app.test_client() as client:
        resp = client.get('/')
        assert resp.status_code == 200


def test_projects_route():
    with app.app.test_client() as client:
        resp = client.get('/projects')
        assert resp.status_code == 200
