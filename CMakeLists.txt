cmake_minimum_required(VERSION 3.16)
project(example)

set(CMAKE_CROSSCOMPILING 1)

find_package(gRPC REQUIRED)
message("GRPC_CPP_PLUGIN_PROGRAM: ${GRPC_CPP_PLUGIN_PROGRAM}")

get_target_property(grpc_cpp_plugin_location gRPC::grpc_cpp_plugin IMPORTED_LOCATION)
message("grpc_cpp_plugin_location: ${grpc_cpp_plugin_location}")

message("CMAKE_CROSSCOMPILING: ${CMAKE_CROSSCOMPILING}")
