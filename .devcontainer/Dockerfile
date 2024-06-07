FROM fedora:40

ARG USERNAME=developer
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN dnf install -y rpmdevtools rpmlint wget meson git gcc shadow-utils-subid-devel cmake systemd patchelf podman skopeo shellcheck openssl

RUN cd /tmp && \
    wget https://go.dev/dl/go1.22.4.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go1.22.4.linux-amd64.tar.gz


ENV PATH=$PATH:/usr/local/go/bin

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -ms /bin/bash $USERNAME \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

USER $USERNAME

RUN go install github.com/cpuguy83/go-md2man@latest

ENV PATH=$PATH:/home/$USERNAME/go/bin
