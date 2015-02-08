#!/bin/bash

for f in $(find . -type f -iname '*.pdf');do

    txt=$(echo $f | sed -e 's/\.pdf$/.txt/i')
    tmp=$(mktemp)
    pdftotext -enc EUC-JP $f
    iconv -c -f EUC-JP -t SHIFT-JIS $txt > $tmp
    /bin/mv $tmp $txt

    echo "$f $txt"
done
