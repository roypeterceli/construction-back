FROM python:3.13-slim
COPY --from=ghcr.io/astral-sh/uv:0.6.6 /uv /uvx /bin/

WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-cache
COPY app/ app/

EXPOSE 9000

CMD ["/app/.venv/bin/fastapi", "run", "app/main.py", "--port", "9000", "--host", "0.0.0.0"]
