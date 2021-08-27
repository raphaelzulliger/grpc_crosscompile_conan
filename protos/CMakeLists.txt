# Solution as documented here: https://stackoverflow.com/questions/32823563/using-cmake-to-create-protobuf-grpc-cc-files. See second answer! (not the first one)

set(PROTO_FILES
    interface.proto
)

# protobuf source files go into the lib just like any other CPP source file
add_library(libinterface STATIC
    ${PROTO_FILES})

target_include_directories(libinterface
    PUBLIC
        ${CMAKE_CURRENT_BINARY_DIR}
)

# Add globally available libraries
target_link_libraries(libinterface
        gRPC::grpc++
)

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
