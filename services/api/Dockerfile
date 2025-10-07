# ---------- BUILD STAGE ----------
# Build wheels for the target arch (set via --platform at build time)
FROM --platform=$TARGETPLATFORM python:3.12-slim AS builder

WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
  && rm -rf /var/lib/apt/lists/*

# Copy deps first to leverage Docker layer cache
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip wheel --no-cache-dir --wheel-dir=/wheels -r requirements.txt

# Copy app source (brings in app.py)
COPY . .

# ---------- RUNTIME STAGE ----------
# Target the same platform (no hard-coded constant)
FROM --platform=$TARGETPLATFORM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

RUN useradd -m appuser
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates \
  && rm -rf /var/lib/apt/lists/*

# Install deps built for this arch
COPY --from=builder /wheels /wheels
RUN pip install --no-cache /wheels/*

# Copy only what we need to run
COPY app.py /app/app.py

USER appuser
EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/healthz')" || exit 1

# Run Flask app with gunicorn (app object is in app.py)
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "app:app"]
