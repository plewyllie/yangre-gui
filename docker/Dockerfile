FROM ubuntu
MAINTAINER Pieter Lewyllie

EXPOSE 5000

RUN apt-get update
RUN apt-get -y install clang
RUN apt-get -y install cmake
RUN apt-get -y install libpcre3-dev
RUN apt-get -y install git
RUN cd /home; git clone https://github.com/CESNET/libyang.git
RUN cd /home/libyang; mkdir build
RUN cd /home/libyang/build; cmake ..; make; make install
RUN cd /home; git clone https://github.com/plewyllie/yangre-gui.git
# don't need git anymore
RUN apt-get -y remove git

RUN cd /home; mkdir w3cgrep
# copy C file
COPY w3cgrep.c /home/w3cgrep/.
RUN apt-get -y install libxml2-dev
RUN cd /home/w3cgrep; clang w3cgrep.c -I/usr/include/libxml2 -lxml2 -o w3cgrep

RUN apt-get -y install python3-pip
RUN apt-get -y install nginx
RUN pip3 install uwsgi flask
RUN apt-get -y install uwsgi-plugin-python3


WORKDIR "/home/yangre-gui"
CMD ["uwsgi", "--socket", "0.0.0.0:5000", \
               "--protocol", "uwsgi", \
               "-w", "wsgi:application" ]
