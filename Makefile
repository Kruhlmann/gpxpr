VERSION_FILE:=src/gpxpr/__version__.py

include make/clean.mk
include make/help.mk
include make/install.mk
include make/lint.mk
include make/test.mk
include make/version.mk

.DEFAULT:help
