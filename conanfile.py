from conans import ConanFile, tools
from conan.tools.cmake import CMakeDeps


class TestGRPCConan(ConanFile):
    name = "grpc_cross"
    version = "0.0.1"
    author = "Raphael Zulliger <zulliger@software-natives.ch>"
    url = ""
    generators = "cmake", "cmake_find_package"
    settings = ["os", "compiler", "build_type", "arch"]
    requires = ["grpc/1.38.0", "protobuf/3.17.1"]
    # build_requires = ["grpc/1.38.0", "protobuf/3.17.1"]

    def build_requirements(self):
        if hasattr(self, "settings_build") and tools.cross_building(self):
            self.build_requires(str(self.requires['grpc']))
            self.build_requires(str(self.requires['protobuf']))

    # def build(self):
    #     cmake = CMake(self)
    #     cmake.configure()
    #     cmake.build()

    # def generate(self):
    #     cmake = CMakeDeps(self)
    #     # # generate the config files for the build require
    #     # cmake.build_context_activated = ["grpc", "protobuf"]
    #     # # disambiguate the files, targets, etc
    #     # cmake.build_context_suffix = {"grpc": "_BUILD", "protobuf": "_BUILD"}
    #     # # Choose the build modules from "build" context
    #     # cmake.build_context_build_modules = ["grpc", "protobuf"]
    #     cmake.generate()
