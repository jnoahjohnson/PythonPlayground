# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.19

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.19.4/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.19.4/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/noahjohnson/Dev/PythonPlayground/opencv

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/noahjohnson/Dev/PythonPlayground/build_opencv

# Include any dependencies generated for this target.
include samples/cpp/CMakeFiles/example_tutorial_how_to_scan_images.dir/depend.make

# Include the progress variables for this target.
include samples/cpp/CMakeFiles/example_tutorial_how_to_scan_images.dir/progress.make

# Include the compile flags for this target's objects.
include samples/cpp/CMakeFiles/example_tutorial_how_to_scan_images.dir/flags.make

samples/cpp/CMakeFiles/example_tutorial_how_to_scan_images.dir/tutorial_code/core/how_to_scan_images/how_to_scan_images.cpp.o: samples/cpp/CMakeFiles/example_tutorial_how_to_scan_images.dir/flags.make
samples/cpp/CMakeFiles/example_tutorial_how_to_scan_images.dir/tutorial_code/core/how_to_scan_images/how_to_scan_images.cpp.o: /Users/noahjohnson/Dev/PythonPlayground/opencv/samples/cpp/tutorial_code/core/how_to_scan_images/how_to_scan_images.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/noahjohnson/Dev/PythonPlayground/build_opencv/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object samples/cpp/CMakeFiles/example_tutorial_how_to_scan_images.dir/tutorial_code/core/how_to_scan_images/how_to_scan_images.cpp.o"
	cd /Users/noahjohnson/Dev/PythonPlayground/build_opencv/samples/cpp && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/example_tutorial_how_to_scan_images.dir/tutorial_code/core/how_to_scan_images/how_to_scan_images.cpp.o -c /Users/noahjohnson/Dev/PythonPlayground/opencv/samples/cpp/tutorial_code/core/how_to_scan_images/how_to_scan_images.cpp

samples/cpp/CMakeFiles/example_tutorial_how_to_scan_images.dir/tutorial_code/core/how_to_scan_images/how_to_scan_images.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/example_tutorial_how_to_scan_images.dir/tutorial_code/core/how_to_scan_images/how_to_scan_images.cpp.i"
	cd /Users/noahjohnson/Dev/PythonPlayground/build_opencv/samples/cpp && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/noahjohnson/Dev/PythonPlayground/opencv/samples/cpp/tutorial_code/core/how_to_scan_images/how_to_scan_images.cpp > CMakeFiles/example_tutorial_how_to_scan_images.dir/tutorial_code/core/how_to_scan_images/how_to_scan_images.cpp.i

samples/cpp/CMakeFiles/example_tutorial_how_to_scan_images.dir/tutorial_code/core/how_to_scan_images/how_to_scan_images.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/example_tutorial_how_to_scan_images.dir/tutorial_code/core/how_to_scan_images/how_to_scan_images.cpp.s"
	cd /Users/noahjohnson/Dev/PythonPlayground/build_opencv/samples/cpp && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/noahjohnson/Dev/PythonPlayground/opencv/samples/cpp/tutorial_code/core/how_to_scan_images/how_to_scan_images.cpp -o CMakeFiles/example_tutorial_how_to_scan_images.dir/tutorial_code/core/how_to_scan_images/how_to_scan_images.cpp.s

# Object files for target example_tutorial_how_to_scan_images
example_tutorial_how_to_scan_images_OBJECTS = \
"CMakeFiles/example_tutorial_how_to_scan_images.dir/tutorial_code/core/how_to_scan_images/how_to_scan_images.cpp.o"

# External object files for target example_tutorial_how_to_scan_images
example_tutorial_how_to_scan_images_EXTERNAL_OBJECTS =

bin/example_tutorial_how_to_scan_images: samples/cpp/CMakeFiles/example_tutorial_how_to_scan_images.dir/tutorial_code/core/how_to_scan_images/how_to_scan_images.cpp.o
bin/example_tutorial_how_to_scan_images: samples/cpp/CMakeFiles/example_tutorial_how_to_scan_images.dir/build.make
bin/example_tutorial_how_to_scan_images: 3rdparty/lib/libippiw.a
bin/example_tutorial_how_to_scan_images: 3rdparty/ippicv/ippicv_mac/icv/lib/intel64/libippicv.a
bin/example_tutorial_how_to_scan_images: lib/libopencv_gapi.4.5.1.dylib
bin/example_tutorial_how_to_scan_images: lib/libopencv_highgui.4.5.1.dylib
bin/example_tutorial_how_to_scan_images: lib/libopencv_ml.4.5.1.dylib
bin/example_tutorial_how_to_scan_images: lib/libopencv_objdetect.4.5.1.dylib
bin/example_tutorial_how_to_scan_images: lib/libopencv_photo.4.5.1.dylib
bin/example_tutorial_how_to_scan_images: lib/libopencv_stitching.4.5.1.dylib
bin/example_tutorial_how_to_scan_images: lib/libopencv_video.4.5.1.dylib
bin/example_tutorial_how_to_scan_images: lib/libopencv_videoio.4.5.1.dylib
bin/example_tutorial_how_to_scan_images: lib/libopencv_imgcodecs.4.5.1.dylib
bin/example_tutorial_how_to_scan_images: lib/libopencv_calib3d.4.5.1.dylib
bin/example_tutorial_how_to_scan_images: lib/libopencv_features2d.4.5.1.dylib
bin/example_tutorial_how_to_scan_images: lib/libopencv_flann.4.5.1.dylib
bin/example_tutorial_how_to_scan_images: lib/libopencv_dnn.4.5.1.dylib
bin/example_tutorial_how_to_scan_images: lib/libopencv_imgproc.4.5.1.dylib
bin/example_tutorial_how_to_scan_images: lib/libopencv_core.4.5.1.dylib
bin/example_tutorial_how_to_scan_images: samples/cpp/CMakeFiles/example_tutorial_how_to_scan_images.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/noahjohnson/Dev/PythonPlayground/build_opencv/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../../bin/example_tutorial_how_to_scan_images"
	cd /Users/noahjohnson/Dev/PythonPlayground/build_opencv/samples/cpp && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/example_tutorial_how_to_scan_images.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
samples/cpp/CMakeFiles/example_tutorial_how_to_scan_images.dir/build: bin/example_tutorial_how_to_scan_images

.PHONY : samples/cpp/CMakeFiles/example_tutorial_how_to_scan_images.dir/build

samples/cpp/CMakeFiles/example_tutorial_how_to_scan_images.dir/clean:
	cd /Users/noahjohnson/Dev/PythonPlayground/build_opencv/samples/cpp && $(CMAKE_COMMAND) -P CMakeFiles/example_tutorial_how_to_scan_images.dir/cmake_clean.cmake
.PHONY : samples/cpp/CMakeFiles/example_tutorial_how_to_scan_images.dir/clean

samples/cpp/CMakeFiles/example_tutorial_how_to_scan_images.dir/depend:
	cd /Users/noahjohnson/Dev/PythonPlayground/build_opencv && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/noahjohnson/Dev/PythonPlayground/opencv /Users/noahjohnson/Dev/PythonPlayground/opencv/samples/cpp /Users/noahjohnson/Dev/PythonPlayground/build_opencv /Users/noahjohnson/Dev/PythonPlayground/build_opencv/samples/cpp /Users/noahjohnson/Dev/PythonPlayground/build_opencv/samples/cpp/CMakeFiles/example_tutorial_how_to_scan_images.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : samples/cpp/CMakeFiles/example_tutorial_how_to_scan_images.dir/depend

