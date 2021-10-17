#/bin/sh
conan --version
conan install conanfile.txt --profile:host=m1 --profile:build=default
