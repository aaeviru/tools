#!/bin/sh
for d in A B; do
        for n in 1993 1994 1995 1996 1997 1998 1999 2000 2001 2002; do
                qrsh -N cl$n$d -nostdin python clearup.py /mnt/nas2b/ko/Data/$n$d/ >& logcl$n$d.txt &
        done
done

