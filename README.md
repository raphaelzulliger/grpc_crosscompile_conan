# Cross compile gRPC

Cross compiling a gRPC based project from Linux `x64` to Linux `armv7` using Conan and CMake

## ATTENTION

## DOES NOT WORK

## DO NOT USE

This project was built to report a bug. Hence, it does not actually work! "Not working" in this case means that compiling the `.proto` files will fail because the `ARM` binaries of `protoc` and the `grpc plugin` are used instead of the `x64` ones.

## Prerequisites

### Build system

The following steps have been performed on an Ubuntu 20.04:

```sh
apt-get install g++-10-arm-linux-gnueabihf
```

### Conan

Install a Conan profile for making Conan aware of the cross toolchain and the targeted ARM embedded system:

```sh
conan config install ./conan
```

This projects expects a `default` profile, matching your current system. If you start with an empty `~/.conan`, you may create one like this

```sh
conan profile new default --detect
```

## Configure and Build

```sh
# Conan install (install dependencies)
conan install . -pr:b default -pr:h grpc_repro --build missing -if build/Debug
# Configure
cmake -DCMAKE_TOOLCHAIN_FILE=cmake/crosstoolchain.cmake -DCMAKE_BUILD_TYPE=Debug -H. -Bbuild/Debug -G Ninja
# Build
cmake --build build/Debug
```

## High level view

- Conan
  - Conan handles dependencies (gRPC & Co)
  - Downloads pre-built `x64` binaries for Linux of gRPC & Co.
  - Downloads recipes and builds (cross compilation) gRPC & CO for the embedded target
  - Places CMake modules into this projects' build folder
- CMake configuration:
  - Uses the CMake modules being installed by Conan just before
  - These CMake modulees help CMake to find the `protoc` binary
- CMake build:
  - Uses `protobuf` and `gRPC` binaries to compile `.proto` files
