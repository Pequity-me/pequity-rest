FROM ubuntu:bionic
MAINTAINER Mike Miller <mtmiller@octave.org>

RUN apt-get update -y && apt-get install -y --no-install-recommends \
    autoconf \
    automake \
    build-essential \
    curl \
    default-jre-headless \
    epstool \
    fig2dev \
    g++ \
    gcc \
    gdb \
    gfortran \
    ghostscript \
    git \
    gnuplot-qt \
    info \
    less \
    libamd2 \
    libarpack2 \
    libblas-dev \
    libbz2-1.0 \
    libcamd2 \
    libccolamd2 \
    libcholmod3 \
    libcolamd2 \
    libcurl3-gnutls \
    libcxsparse3 \
    libfftw3-dev \
    libfltk-gl1.3 \
    libfltk1.3 \
    libfontconfig1 \
    libfreetype6 \
    libgl1 \
    libgl2ps1.4 \
    libglpk40 \
    libglu1-mesa \
    libgraphicsmagick++-q16-12 \
    libhdf5-100 \
    libklu1 \
    liblapack-dev \
    libncurses5 \
    libopenblas-dev \
    libpcre3 \
    libportaudio2 \
    libqhull7 \
    libqrupdate1 \
    libqscintilla2-qt5-13 \
    libqt5core5a \
    libqt5gui5 \
    libqt5help5 \
    libqt5network5 \
    libqt5opengl5 \
    libqt5printsupport5 \
    libqt5sql5 \
    libqt5widgets5 \
    libreadline-dev \
    libsndfile1 \
    libsundials-ida2 \
    libsundials-nvecserial2 \
    libtool \
    libumfpack5 \
    make \
    pstoedit \
    python-dev \
    python-pip \
    python-setuptools \
    python-wheel \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    texinfo \
    unzip \
    xz-utils \
    zip \
  && apt-get clean \
  && rm -rf \
    /tmp/hsperfdata* \
    /var/*/apt/*/partial \
    /var/lib/apt/lists/* \
    /var/log/apt/term*

# The default version of Octave used to build this image
ARG OCTAVE_VERSION=5.1.0

RUN curl -L -S --retry 5 https://octave-snapshot.s3.amazonaws.com/public/octave-$OCTAVE_VERSION-ubuntu-bionic-amd64.tar.xz \
  | tar -xJ

ENV LANG C.UTF-8
ENV OCTAVE_HOME /octave
ENV OCTAVE_VERSION $OCTAVE_VERSION
ENV LD_LIBRARY_PATH $OCTAVE_HOME/lib/octave/$OCTAVE_VERSION
ENV PATH $OCTAVE_HOME/bin:$PATH



# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
ADD . /app

# Install the dependencies
RUN pip3 install -r requirements.txt

# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]
