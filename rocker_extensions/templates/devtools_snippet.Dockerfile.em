# workspace development helpers
RUN apt-get update \
  && apt-get install -y \
  bat \
  build-essential \
  clang-format clang-tidy clang-tools clang \
  cmake \
  curl \
  dbus-x11 \
  direnv \
  gdb \
  git \
  git-core \
  git-lfs \
  iputils-ping \
  less \
  lsd \
  nano \
  net-tools \
  openssh-client \
  ripgrep \
  trash-cli \
  wget \
  x11-apps \
  xterm \
  zsh \
  && apt-get clean
