FROM ubuntu:24.04

WORKDIR /workspace

RUN apt update && \
    apt install -y curl build-essential openssh-client zip unzip tmux && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

# install rye
ENV RYE_HOME="$HOME/.rye"
ENV PATH="$RYE_HOME/shims:$PATH"
RUN curl -sSf https://rye.astral.sh/get | RYE_NO_AUTO_INSTALL=1 RYE_INSTALL_OPTION="--yes" bash

# activate uv
RUN rye config --set-bool behavior.use-uv=true
