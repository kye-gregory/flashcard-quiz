FROM python:3.12-alpine3.22@sha256:02a73ead8397e904cea6d17e18516f1df3590e05dc8823bd5b1c7f849227d272

# Install UV
COPY --from=ghcr.io/astral-sh/uv:0.8.14@sha256:f3660c56d5b08d6c516360981bedc439f499b9bf37f46a216018da3777a74011 /uv /uvx usr/local/bin/

# Setup non-root user for security
RUN addgroup -g 61000 docker
RUN adduser -D -G docker -u 61000 docker
USER docker

# Copy the project into the image
COPY --chown=docker:docker pyproject.toml uv.lock /app/

# Sync the project into a new environment, asserting the lockfile is up to date
WORKDIR /app
RUN uv sync --locked

COPY --chown=docker:docker . /app

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
