Dockerizing this Flask personal website

Files added:
- Dockerfile: Builds a minimal image and runs the app with gunicorn on port 5000.
- .dockerignore: Excludes local files from the build context.

Build image (from repo root):

```powershell
# From the directory containing Dockerfile
docker build -t personal-website:latest .
```

Run container (bind port 5000):

```powershell
# Run with a named volume to persist SQLite DB (recommended)
docker volume create pw_db
docker run -d -p 5000:5000 -v pw_db:/app/projects.db --name personal-website personal-website:latest

# Or bind-mount a host folder to persist database file:
# docker run -d -p 5000:5000 -v C:\path\to\host\dir\projects.db:/app/projects.db --name personal-website personal-website:latest
```

Notes:
- The app uses SQLite at `/app/projects.db` by default. Use a Docker volume or host bind mount to persist it across restarts.
- For local development, continue using `python -m flask run` or `python app.py`.
- The container runs `gunicorn app:app` listening on 0.0.0.0:5000.
- If you need to set a secret key, pass `-e FLASK_SECRET_KEY=yourkey` to `docker run`.

Docker Desktop (recommended)

This repo includes a `docker-compose.yml` so you can run the site easily with Docker Desktop.

From the project root (where `docker-compose.yml` lives):

```powershell
docker compose up --build
```

This will build the image and start the `web` service. The SQLite DB file will be created at `./data/projects.db` on your host, so it persists across container restarts.

Stop with:

```powershell
docker compose down
```

To remove the DB data file (on host):

```powershell
Remove-Item -Recurse -Force .\data
```
