# Coin-or CBC native interface for Python
# Copyright (C) 2019 Patrik Dufresne Service Logiciel <info@patrikdufresne.com>
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

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
