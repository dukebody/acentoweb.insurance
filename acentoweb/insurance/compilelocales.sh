#!/bin/sh
# Compile po files
for lang in $(find locales -mindepth 1 -maxdepth 1 -type d); do
    if test -d $lang/LC_MESSAGES; then
        msgfmt -o $lang/LC_MESSAGES/acentoweb.insurance.mo $lang/LC_MESSAGES/acentoweb.insurance.po
    fi
done

