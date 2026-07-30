# This Dockerfile is used to deploy a simple single-container Reflex app instance.
FROM python:3.14.6


WORKDIR /app
COPY . .

ENV VIRTUAL_ENV=/app/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
# Install app requirements and reflex in the container
RUN pip install -r requirements.txt

# Always apply migrations before starting the backend.
CMD reflex run --env prod --backend-only
