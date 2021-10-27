${VERSION_FILE}:
	echo "__version__ = \"$(shell git describe --tag --always | grep -oE '[0-9]+\.[0-9]+\.[0-9]+')\"" > ${VERSION_FILE}
