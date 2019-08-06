FROM ikus060/docker-debian-py2-py3:stretch

# Install the dependencies for CBC and install SWIG v4.0
RUN apt update && \
  apt install -y gfortran && \
  wget https://sourceforge.net/projects/swig/files/swig/swig-4.0.0/swig-4.0.0.tar.gz && \
  tar -zxvf swig-4.0.0.tar.gz  && \
  cd swig-4.0.0  && \
  ./configure  && \
  make  && \
  make install
