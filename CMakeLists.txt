cmake_minimum_required(VERSION 3.21)
project(grpc_cross LANGUAGES CXX)

# include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
# conan_basic_setup()

# # Make sure the `.cmake` files for the individual packages, as installed by Conan, are found
# list(APPEND CMAKE_PREFIX_PATH "${CMAKE_BINARY_DIR}")

set(
    CMAKE_CXX_STANDARD 17               # Use C++17
    CMAKE_CXX_STANDARD_REQUIRED ON      # Require the compiler to support C++17 (don't fall back to e.g. C++14)
    CXX_EXTENSIONS OFF)                 # e.g. use -std=c++11 rather than -std=gnu++11


# set(protobuf_MODULE_COMPATIBLE TRUE)
# find_package(protobuf REQUIRED)
# message(STATUS "Using protobuf ${protobuf_VERSION}")
# if (CMAKE_CROSSCOMPILING)
#     find_program(Protoc_Executable protoc PATHS ENV PATH NO_DEFAULT_PATH)
# else()
#     set(Protoc_Executable ${Protobuf_PROTOC_EXECUTABLE})
# endif()

# Find gRPC installation
find_package(gRPC REQUIRED)
message(STATUS "Using gRPC ${gRPC_VERSION}")
set(_GRPC_CPP_PLUGIN_EXECUTABLE $<TARGET_FILE:gRPC::grpc_cpp_plugin>)


message("##### Shit ${Protoc_Executable}")
add_subdirectory(protos)
