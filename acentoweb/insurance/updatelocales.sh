#!/bin/sh
i18ndude rebuild-pot --pot locales/acentoweb.insurance.pot --create acentoweb.insurance .
i18ndude sync --pot locales/acentoweb.insurance.pot locales/*/LC_MESSAGES/acentoweb.insurance.po
i18ndude sync --pot locales/plone.pot locales/*/LC_MESSAGES/plone.po

