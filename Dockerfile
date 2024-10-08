ARG progress=plain
# Use specific version of nvidia cuda image
# initial 11.7.1-cudnn8-runtime-ubuntu20.04
# update 11.8.0-cudnn8-runtime-ubuntu20.04
# experimental 12.2.2-cudnn8-runtime-ubuntu20.04
# 11.8.0-cudnn8-runtime-ubuntu22.04
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04

# Remove any third-party apt sources to avoid issues with expiring keys.
RUN rm -f /etc/apt/sources.list.d/*.list

# Set shell and noninteractive environment variables
SHELL ["/bin/bash", "-c"]
ENV DEBIAN_FRONTEND=noninteractive
ENV SHELL=/bin/bash

# Set working directory
WORKDIR /

# Update and upgrade the system packages (Worker Template)
# =7:6.0-6ubuntu1
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install --yes --no-install-recommends sudo ca-certificates git wget curl bash libgl1 libx11-6 software-properties-common build-essential -y &&\
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*

#COPY bin /usr/bin

# Install latest ffmpeg from compiled source
#ADD https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz /lctmp/
# /lctmp/ffmpeg-6.1-amd64-static/ffmpeg
ADD https://johnvansickle.com/ffmpeg/builds/ffmpeg-git-amd64-static.tar.xz /lctmp/
RUN tar -xJvf /lctmp/ffmpeg-git-amd64-static.tar.xz -C /lctmp/ && \
    ls -l /lctmp/ && \
    ffmpeg_dir=$(ls -1 ffmpeg-git-*-amd64-static /lctmp/ | head -1) && \
    echo $ffmpeg_dir && \
    chmod 755 /lctmp/"$ffmpeg_dir"ffmpeg && \
    cp /lctmp/"$ffmpeg_dir"ffmpeg /usr/bin/ && \
    chmod 755 /lctmp/"$ffmpeg_dir"ffprobe && \
    cp /lctmp/"$ffmpeg_dir"ffprobe /usr/bin/ && \
    chmod 755 /lctmp/"$ffmpeg_dir"qt-faststart && \
    cp /lctmp/"$ffmpeg_dir"qt-faststart /usr/bin/ && \
    rm -rf /lctmp && \
    ffmpeg -version | grep 'ffmpeg version' > ./ffmpeg_version.txt

#RUN ffmpeg -version | grep 'ffmpeg version' > ./ffmpeg_version.txt

# Install CUDA 12
# wget https://developer.download.nvidia.com/compute/cuda/12.3.1/local_installers/cuda_12.3.1_545.23.08_linux.run
# sudo sh cuda_12.3.1_545.23.08_linux.run

# Add the deadsnakes PPA and install Python 3.10
RUN add-apt-repository ppa:deadsnakes/ppa -y && \
    apt-get install python3.10-dev python3.10-venv python3-pip -y --no-install-recommends && \
    ln -s /usr/bin/python3.10 /usr/bin/python && \
    rm /usr/bin/python3 && \
    ln -s /usr/bin/python3.10 /usr/bin/python3 && \
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*

# Download and install pip
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python get-pip.py && \
    rm get-pip.py

# Install Python dependencies (Worker Template)
COPY builder/requirements.txt /requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip && \
    pip install -r /requirements.txt --no-cache-dir && \
    rm /requirements.txt

# Copy and run script to fetch models
COPY builder/fetch_models.py /fetch_models.py
RUN python /fetch_models.py && \
    rm /fetch_models.py

# Copy source code into image
COPY src .

# Set default command
CMD python -u /rp_handler.py
