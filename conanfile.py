from conan import ConanFile
from conan.tools.cmake import cmake_layout, CMake, CMakeToolchain, CMakeDeps

class Project(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    
    # Define generators settings
    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.user_presets_path = False
        tc.generate()

    def requirements(self):
        self.requires("opencv/4.10.0")

    # Conan generated files location
    def layout(self):
        cmake_layout(self, build_folder="conan-build")

    def package(self):
        cmake = CMake(self)
        cmake.install()
