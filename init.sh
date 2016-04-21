#!/bin/sh
for d in A B; do
        for n in 1993 1994 1995 1996 1997 1998 1999 2000 2001 2002; do
		qrsh -N ch$n$d -nostdin python init.py /mnt/nas2b/ko/Data/$n$d/ >& login$n$d.txt &
        done
done

