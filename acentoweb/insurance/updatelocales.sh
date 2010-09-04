#!/bin/sh
i18ndude rebuild-pot --pot locales/acentoweb.insurance.pot --create acentoweb.insurance .
i18ndude sync --pot locales/acentoweb.insurance.pot locales/*/LC_MESSAGES/acentoweb.insurance.po

# Compile po files
for lang in $(find locales -mindepth 1 -maxdepth 1 -type d); do
    if test -d $lang/LC_MESSAGES; then
        msgfmt -o $lang/LC_MESSAGES/acentoweb.insurance.mo $lang/LC_MESSAGES/acentoweb.insurance.po
    fi
done

