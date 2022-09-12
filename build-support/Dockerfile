ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}-slim as python-builder
ARG REPO

# PYTHONUNBUFFERED: Force stdin, stdout and stderr to be totally unbuffered.
# PYTHONHASHSEED: Enable hash randomization.
# PYTHONDONTWRITEBYTECODE: Do not write byte files to disk.
ENV LANG=C.UTF-8 \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_NO_CACHE_DIR=off \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONIOENCODING=utf-8 \
    PYTHONUNBUFFERED=1

# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#run
RUN apt-get update \
    && apt-get install -yqq --no-install-recommends \
        curl \
        git \
        docker.io \
# Clean up the apt cache by removing /var/lib/apt/lists to reduce the image size, since 
# the apt cache is not stored in a layer. Since the RUN statement starts with 
# apt-get update, the package cache is always refreshed prior to apt-get install.
    && rm -rf /var/lib/apt/lists/*

# Run Docker as a non-root user
ENV USER=pantsuser
RUN useradd --create-home ${USER}
USER ${USER}

# Setup application install directory.
ENV REPO_PATH=/home/${USER}/${REPO}
RUN mkdir ${REPO_PATH}
WORKDIR ${REPO_PATH}

# bootstrap pants
COPY pants pants.toml ${REPO_PATH}
RUN ./pants --version

CMD ["sleep", "infinity"]