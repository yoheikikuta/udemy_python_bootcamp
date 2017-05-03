FROM python:3.6.1
MAINTAINER Yohei Kikuta <diracdiego@gmail.com>

#Language set up
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

#Anaconda installation
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh \
    && wget --quiet https://repo.continuum.io/archive/Anaconda3-4.3.0-Linux-x86_64.sh \
    && /bin/bash ./Anaconda3-4.3.0-Linux-x86_64.sh -b -p /opt/conda \
    && rm ./Anaconda3-4.3.0-Linux-x86_64.sh
ENV PATH=/opt/conda/bin:$PATH

#Set working directory
WORKDIR /work

#Set entrypoint
ENTRYPOINT ["/bin/bash"]
