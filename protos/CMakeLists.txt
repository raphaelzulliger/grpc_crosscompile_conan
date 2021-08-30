# Solution as documented here: https://stackoverflow.com/questions/32823563/using-cmake-to-create-protobuf-grpc-cc-files. See second answer! (not the first one)

set(PROTO_FILES
    interface.proto
)

# Notice the `_BUILD` suffix, as documented https://docs.conan.io/en/1.39/reference/conanfile/tools/cmake/cmakedeps.html#build-context-suffix
find_package(protobuf_BUILD CONFIG REQUIRED)
find_package(gRPC_BUILD CONFIG REQUIRED)
get_target_property(grpc_cpp_plugin_location gRPC::grpc_cpp_plugin LOCATION)

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
