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
# Configure
cmake -DCMAKE_TOOLCHAIN_FILE=cmake/crosstoolchain.cmake -DCMAKE_BUILD_TYPE=Debug -H. -Bbuild/Debug -G Ninja
# Build
cmake --build build/Debug
```

## Project structure

- CMake drives the whole build process
- CMake configuration:
  - Performs `conan intall` to install dependencies (`gRPC` in this case)
  - Since no pre-built binaries of `gRPC` are available, these will be built (may take some time!)
- CMake build:
  - Uses `protobuf` and `gRPC` CMake modules to compile `.proto` files
