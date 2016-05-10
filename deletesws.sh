#!/bin/sh
for n in A B C D E F G H; do
        python deletesws.py ~/data/classinfo/$n/ 1 >& log/dsw$n.txt &
done

