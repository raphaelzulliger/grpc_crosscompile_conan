# in user space
if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
message(STATUS "Downloading conan.cmake from https://github.com/conan-io/cmake-conan")
file(DOWNLOAD "https://raw.githubusercontent.com/conan-io/cmake-conan/v0.16.1/conan.cmake"
                "${CMAKE_BINARY_DIR}/conan.cmake"
                EXPECTED_HASH SHA256=396e16d0f5eabdc6a14afddbcfff62a54a7ee75c6da23f32f7a31bc85db23484
                TLS_VERIFY ON)
endif()

include(${CMAKE_BINARY_DIR}/conan.cmake)

# Make sure to use conanfile.py to define dependencies, to stay consistent
# Get settings, such as Debug vs. Release, selected compiler, etc.
conan_cmake_autodetect(settings)

SET(conan_profile "default")
if (DEFINED CMAKE_TOOLCHAIN_FILE)
    # *IF* we are crosss compiling then it's always for `grpc_repro` thus far.
    SET(conan_profile "grpc_repro")
endif()

#
# A note about cross compilation:
# Note on `PROFILE_BUILD` and `PROFILE_HOST`: Only specifying `PROFILE` is not sufficient for `grpc`.
# Somewhere in the warnings, the build outputs of grpc mentioned that we need to specify `-pr:b` and
# soon after that warning output, the build failed because it tried to execute `protoc` on x64 which was
# compiled for ARMv7.
conan_cmake_install(
    PATH_OR_REFERENCE
        ${CMAKE_SOURCE_DIR}
    BUILD
        missing
    SETTINGS
        ${settings}
    PROFILE_BUILD
        default
    PROFILE_HOST
        ${conan_profile}
)
