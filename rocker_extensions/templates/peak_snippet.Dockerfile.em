# Add peak driver
ARG PEAK_DRIVER=install
RUN if [ "$PEAK_DRIVER" = "install" ]; \
    then \
    apt-get update && apt-get install -y udev libpopt-dev linux-headers-$(uname -r) \
    && wget https://www.peak-system.com/fileadmin/media/linux/files/peak-linux-driver-8.18.0.tar.gz \
    && wget https://www.peak-system.com/quick/BasicLinux -O PCAN-Basic_Linux.tar.gz \
    && tar -xvf peak-linux-driver-8.18.0.tar.gz \
    && cd peak-linux-driver-8.18.0 \
    && make clean && make install || echo 'make failed but move forward'\
    && cd .. \
    && tar -xvf PCAN-Basic_Linux.tar.gz \
    && cd PCAN-Basic_Linux-4.8.0.5/libpcanbasic \
    && make clean && make install || echo 'make failed but move forward';\
    fi
