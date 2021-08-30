from conans import ConanFile
from conan.tools.cmake import CMakeDeps


class TestGRPCConan(ConanFile):
    name = "grpc_cross"
    version = "0.0.1"
    author = "Raphael Zulliger <zulliger@software-natives.ch>"
    url = ""
    generators = ["CMakeDeps", "CMakeToolchain"]
    settings = ["os", "compiler", "build_type", "arch"]
    requires = ["grpc/1.38.0", "protobuf/3.17.1"]
    build_requires = ["grpc/1.38.0", "protobuf/3.17.1"]


    def generate(self):
        cmake = CMakeDeps(self)
        # generate the config files for the build require
        cmake.build_context_activated = ["grpc", "protobuf"]
        # disambiguate the files, targets, etc
        cmake.build_context_suffix = {"grpc": "_BUILD", "protobuf": "_BUILD"}
        # Choose the build modules from "build" context
        cmake.build_context_build_modules = ["grpc", "protobuf"]
        cmake.generate()
