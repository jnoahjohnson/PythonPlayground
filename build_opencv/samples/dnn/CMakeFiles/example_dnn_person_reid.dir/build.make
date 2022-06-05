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
include samples/dnn/CMakeFiles/example_dnn_person_reid.dir/depend.make

# Include the progress variables for this target.
include samples/dnn/CMakeFiles/example_dnn_person_reid.dir/progress.make

# Include the compile flags for this target's objects.
include samples/dnn/CMakeFiles/example_dnn_person_reid.dir/flags.make

samples/dnn/CMakeFiles/example_dnn_person_reid.dir/person_reid.cpp.o: samples/dnn/CMakeFiles/example_dnn_person_reid.dir/flags.make
samples/dnn/CMakeFiles/example_dnn_person_reid.dir/person_reid.cpp.o: /Users/noahjohnson/Dev/PythonPlayground/opencv/samples/dnn/person_reid.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/noahjohnson/Dev/PythonPlayground/build_opencv/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object samples/dnn/CMakeFiles/example_dnn_person_reid.dir/person_reid.cpp.o"
	cd /Users/noahjohnson/Dev/PythonPlayground/build_opencv/samples/dnn && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/example_dnn_person_reid.dir/person_reid.cpp.o -c /Users/noahjohnson/Dev/PythonPlayground/opencv/samples/dnn/person_reid.cpp

samples/dnn/CMakeFiles/example_dnn_person_reid.dir/person_reid.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/example_dnn_person_reid.dir/person_reid.cpp.i"
	cd /Users/noahjohnson/Dev/PythonPlayground/build_opencv/samples/dnn && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/noahjohnson/Dev/PythonPlayground/opencv/samples/dnn/person_reid.cpp > CMakeFiles/example_dnn_person_reid.dir/person_reid.cpp.i

samples/dnn/CMakeFiles/example_dnn_person_reid.dir/person_reid.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/example_dnn_person_reid.dir/person_reid.cpp.s"
	cd /Users/noahjohnson/Dev/PythonPlayground/build_opencv/samples/dnn && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/noahjohnson/Dev/PythonPlayground/opencv/samples/dnn/person_reid.cpp -o CMakeFiles/example_dnn_person_reid.dir/person_reid.cpp.s

# Object files for target example_dnn_person_reid
example_dnn_person_reid_OBJECTS = \
"CMakeFiles/example_dnn_person_reid.dir/person_reid.cpp.o"

# External object files for target example_dnn_person_reid
example_dnn_person_reid_EXTERNAL_OBJECTS =

bin/example_dnn_person_reid: samples/dnn/CMakeFiles/example_dnn_person_reid.dir/person_reid.cpp.o
bin/example_dnn_person_reid: samples/dnn/CMakeFiles/example_dnn_person_reid.dir/build.make
bin/example_dnn_person_reid: 3rdparty/lib/libippiw.a
bin/example_dnn_person_reid: 3rdparty/ippicv/ippicv_mac/icv/lib/intel64/libippicv.a
bin/example_dnn_person_reid: lib/libopencv_dnn.4.5.1.dylib
bin/example_dnn_person_reid: lib/libopencv_highgui.4.5.1.dylib
bin/example_dnn_person_reid: lib/libopencv_videoio.4.5.1.dylib
bin/example_dnn_person_reid: lib/libopencv_imgcodecs.4.5.1.dylib
bin/example_dnn_person_reid: lib/libopencv_imgproc.4.5.1.dylib
bin/example_dnn_person_reid: lib/libopencv_core.4.5.1.dylib
bin/example_dnn_person_reid: samples/dnn/CMakeFiles/example_dnn_person_reid.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/noahjohnson/Dev/PythonPlayground/build_opencv/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../../bin/example_dnn_person_reid"
	cd /Users/noahjohnson/Dev/PythonPlayground/build_opencv/samples/dnn && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/example_dnn_person_reid.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
samples/dnn/CMakeFiles/example_dnn_person_reid.dir/build: bin/example_dnn_person_reid

.PHONY : samples/dnn/CMakeFiles/example_dnn_person_reid.dir/build

samples/dnn/CMakeFiles/example_dnn_person_reid.dir/clean:
	cd /Users/noahjohnson/Dev/PythonPlayground/build_opencv/samples/dnn && $(CMAKE_COMMAND) -P CMakeFiles/example_dnn_person_reid.dir/cmake_clean.cmake
.PHONY : samples/dnn/CMakeFiles/example_dnn_person_reid.dir/clean

samples/dnn/CMakeFiles/example_dnn_person_reid.dir/depend:
	cd /Users/noahjohnson/Dev/PythonPlayground/build_opencv && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/noahjohnson/Dev/PythonPlayground/opencv /Users/noahjohnson/Dev/PythonPlayground/opencv/samples/dnn /Users/noahjohnson/Dev/PythonPlayground/build_opencv /Users/noahjohnson/Dev/PythonPlayground/build_opencv/samples/dnn /Users/noahjohnson/Dev/PythonPlayground/build_opencv/samples/dnn/CMakeFiles/example_dnn_person_reid.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : samples/dnn/CMakeFiles/example_dnn_person_reid.dir/depend

