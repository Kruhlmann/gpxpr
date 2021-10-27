# gpxpr

## Development

```sh
make lint # Runs flake8, black and isort in checking mode.
make test # Runs unit tests.
make install # Installs the 'gpxpr' entrypoint
```

### Windows

The recommended way to develop on Windows is the make use of the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install) and then referring to the UNIX-like section.

### UNIX-like

Auto-running tests on code change is achievable with [entr](https://archlinux.org/packages/community/x86_64/entr/)

```sh
find src tests -name "*.py" | entr make test
```

Similarly for linting on file change:


```sh
find src tests -name "*.py" | entr make lint
```
