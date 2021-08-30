from conans import ConanFile


class TestGRPCConan(ConanFile):
    name = "grpc_cross"
    version = "0.0.1"
    author = "Raphael Zulliger <zulliger@software-natives.ch>"
    url = ""
    generators = ["CMakeDeps", "CMakeToolchain"]
    settings = ["os", "compiler", "build_type", "arch"]
    requires = ["grpc/1.38.0"]
