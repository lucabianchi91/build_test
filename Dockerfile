FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
    git \
    python3-pip \
    python3-dev

RUN python3 -m pip install --upgrade pip setuptools wheel
RUN pip3 install \
	urllib3 \
	requests \
	python-socketio \
	eventlet
	
RUN pip3 install https://github.com/pyinstaller/pyinstaller/archive/develop.zip
WORKDIR /root/build_test
COPY . .
RUN pyinstaller --noconfirm build_test.spec
ENTRYPOINT ["/root/build_test/dist/build_test/build_test"]
