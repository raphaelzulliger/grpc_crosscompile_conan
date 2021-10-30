#/bin/sh
conan --version
conan install conanfile.txt --profile:host=conan/profiles/m1 --profile:build=conan/profiles/default --generator virtualenv
