cmake_minimum_required(VERSION 3.21)

project(grpc_cross LANGUAGES CXX)

set(
    CMAKE_CXX_STANDARD 17               # Use C++17
    CMAKE_CXX_STANDARD_REQUIRED ON      # Require the compiler to support C++17 (don't fall back to e.g. C++14)
    CXX_EXTENSIONS OFF)                 # e.g. use -std=c++11 rather than -std=gnu++11

# Make sure the `.cmake` files for the individual packages, as installed by Conan, are found
list(APPEND CMAKE_PREFIX_PATH "${CMAKE_BINARY_DIR}")

if(CONAN_EXPORTED)
    # in conan local cache
else()
    include(cmake/cmake_helper.cmake)
endif()

find_package(protobuf CONFIG REQUIRED)
find_package(gRPC CONFIG REQUIRED)
get_target_property(grpc_cpp_plugin_location gRPC::grpc_cpp_plugin LOCATION)

add_subdirectory(protos)
