ARG version=1.92
FROM rust:${version}
ARG version

RUN dpkg --add-architecture arm64
RUN apt-get update && apt-get install -y \
    cmake \
    libclang-dev \
    libxkbcommon-dev \
    libxkbcommon-dev:arm64 \
    libssl-dev \
    libssl-dev:arm64 \
    libgstreamer1.0-dev \
    libgstreamer-plugins-base1.0-dev

# Install arm64 gstreamer dev packages manually (they conflict with amd64 -dev when co-installed)
RUN cd /tmp && \
    apt-get download \
    libgstreamer1.0-dev:arm64 \
    libgstreamer-plugins-base1.0-dev:arm64 \
    libgstreamer1.0-0:arm64 \
    libgstreamer-plugins-base1.0-0:arm64 && \
    for deb in *.deb; do dpkg -x "$deb" /; done && \
    rm -f *.deb

RUN apt-get install -y \
    g++-aarch64-linux-gnu \
    libc6-dev-arm64-cross

# Taskfile support
RUN curl -1sLf 'https://dl.cloudsmith.io/public/task/task/setup.deb.sh' | bash
RUN apt-get install -y task
RUN ln -sf /usr/bin/task /usr/bin/go-task

# RPM support
RUN apt-get install -y rpm librpmbuild10 elfutils

RUN rustup target add aarch64-unknown-linux-gnu
RUN rustup component add clippy
RUN chmod -R 777 /usr/local/rustup

ENV CARGO_TARGET_AARCH64_UNKNOWN_LINUX_GNU_LINKER=aarch64-linux-gnu-gcc
ENV CC_aarch64_unknown_linux_gnu=aarch64-linux-gnu-gcc
ENV CXX_aarch64_unknown_linux_gnu=aarch64-linux-gnu-g++
