
# Prerequisites

## Package managers

Most of the prerequisites should be installed with your package manager if a package is
available:

* MacOS: [homebrew](https://brew.sh/).
* Linux: distro-specific.

Windows is not supported !

## [Docker](https://docs.docker.com/get-docker/)

To verify your installation of Docker, run the following command and confirm there is an output.

```bash
$ docker --version
Docker version 19.03.1
```

## [Taskfile](https://taskfile.dev/)

[Task](https://taskfile.dev/) is a task runner similar to Make but human-friendly.

Verify its installation by running the following command from the top of the repo:
```bash
task --list
```

# Terminology

## Applications and libraries

Applications and libraries are two fundamental building blocks of a monorepo.

A library:
- contains code that can be consumed by applications or other libraries
- contains a configuration for runnings its tests
- can consume code from other libraries

An application:
- can be built into a deployable artifact
- contains a configuration for its build process
- contains a configuration for runnings its tests
- can consume code from libraries
    
A monorepo can contain multiple applications and multiple libraries.