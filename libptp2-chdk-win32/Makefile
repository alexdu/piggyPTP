CC=gcc
CFLAGS=-IC:\MinGW\include -I"C:\Program Files\LibUSB-Win32\include"
LDFLAGS="C:\Program Files\LibUSB-Win32\lib\gcc\libusb.a" -lws2_32 -lkernel32

all: ptpcam dll

ptpcam: config.h libptp-endian.h libptp-stdint.h myusb.c properties.c ptp-pack.c ptp.c ptp.h ptpcam.c ptpcam.h
	$(CC) -o ptpcam myusb.c properties.c ptp.c ptpcam.c $(CFLAGS) $(LDFLAGS)

dll: config.h libptp-endian.h libptp-stdint.h myusb.c properties.c ptp-pack.c ptp.c ptp.h ptpcam.c ptpcam.h
	$(CC) -o ptpcam.dll myusb.c properties.c ptp.c ptpcam.c -shared $(CFLAGS) $(LDFLAGS)
