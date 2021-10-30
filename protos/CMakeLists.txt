# Solution as documented here: https://stackoverflow.com/questions/32823563/using-cmake-to-create-protobuf-grpc-cc-files. See second answer! (not the first one)

set(PROTO_FILES
    interface.proto
)

# # Notice the `_BUILD` suffix, as documented https://docs.conan.io/en/1.39/reference/conanfile/tools/cmake/cmakedeps.html#build-context-suffix
# find_package(protobuf REQUIRED)
# find_package(gRPC REQUIRED)
# if(NOT TARGET gRPC::grpc_cpp_plugin)
#     if(CMAKE_CROSSCOMPILING)
#         find_program(GRPC_CPP_PLUGIN_PROGRAM
#             NAMES grpc_cpp_plugin
#             PATHS ENV
#             PATH NO_DEFAULT_PATH)
#     else()
#         find_program(GRPC_CPP_PLUGIN_PROGRAM
#             NAMES grpc_cpp_plugin
#             PATHS "${CMAKE_CURRENT_LIST_DIR}/../../bin/"
#             NO_DEFAULT_PATH)
#     endif()

#     get_filename_component(GRPC_CPP_PLUGIN_PROGRAM "${GRPC_CPP_PLUGIN_PROGRAM}" ABSOLUTE)

#     add_executable(gRPC::grpc_cpp_plugin IMPORTED)
#     set_property(TARGET gRPC::grpc_cpp_plugin PROPERTY IMPORTED_LOCATION ${GRPC_CPP_PLUGIN_PROGRAM})
# endif()
# get_target_property(grpc_cpp_plugin_location gRPC::grpc_cpp_plugin LOCATION)

# find_package(protobuf CONFIG REQUIRED)
# find_package(gRPC CONFIG REQUIRED)

# protobuf source files go into the lib just like any other CPP source file
add_library(libinterface STATIC
    ${PROTO_FILES})


# compile the message types
protobuf_generate(
    TARGET
        libinterface
    LANGUAGE
        cpp)

# compile the GRPC services
protobuf_generate(
    TARGET
        libinterface
    LANGUAGE
        grpc
    GENERATE_EXTENSIONS
        .grpc.pb.h
        .grpc.pb.cc
    PLUGIN
        "protoc-gen-grpc=${grpc_cpp_plugin_location}"
)

# target_include_directories(libinterface
#     PUBLIC
#         ${CMAKE_CURRENT_BINARY_DIR}
# )

# # Add globally available libraries
# target_link_libraries(libinterface
#         gRPC::grpc++
# )
