# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/dorian/code/blokboi

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/dorian/code/blokboi

# Include any dependencies generated for this target.
include src/CMakeFiles/blokboi.dir/depend.make

# Include the progress variables for this target.
include src/CMakeFiles/blokboi.dir/progress.make

# Include the compile flags for this target's objects.
include src/CMakeFiles/blokboi.dir/flags.make

src/CMakeFiles/blokboi.dir/game.cpp.o: src/CMakeFiles/blokboi.dir/flags.make
src/CMakeFiles/blokboi.dir/game.cpp.o: src/game.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/dorian/code/blokboi/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/CMakeFiles/blokboi.dir/game.cpp.o"
	cd /home/dorian/code/blokboi/src && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/blokboi.dir/game.cpp.o -c /home/dorian/code/blokboi/src/game.cpp

src/CMakeFiles/blokboi.dir/game.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/blokboi.dir/game.cpp.i"
	cd /home/dorian/code/blokboi/src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/dorian/code/blokboi/src/game.cpp > CMakeFiles/blokboi.dir/game.cpp.i

src/CMakeFiles/blokboi.dir/game.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/blokboi.dir/game.cpp.s"
	cd /home/dorian/code/blokboi/src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/dorian/code/blokboi/src/game.cpp -o CMakeFiles/blokboi.dir/game.cpp.s

# Object files for target blokboi
blokboi_OBJECTS = \
"CMakeFiles/blokboi.dir/game.cpp.o"

# External object files for target blokboi
blokboi_EXTERNAL_OBJECTS =

src/blokboi: src/CMakeFiles/blokboi.dir/game.cpp.o
src/blokboi: src/CMakeFiles/blokboi.dir/build.make
src/blokboi: src/CMakeFiles/blokboi.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/dorian/code/blokboi/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable blokboi"
	cd /home/dorian/code/blokboi/src && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/blokboi.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/CMakeFiles/blokboi.dir/build: src/blokboi

.PHONY : src/CMakeFiles/blokboi.dir/build

src/CMakeFiles/blokboi.dir/clean:
	cd /home/dorian/code/blokboi/src && $(CMAKE_COMMAND) -P CMakeFiles/blokboi.dir/cmake_clean.cmake
.PHONY : src/CMakeFiles/blokboi.dir/clean

src/CMakeFiles/blokboi.dir/depend:
	cd /home/dorian/code/blokboi && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/dorian/code/blokboi /home/dorian/code/blokboi/src /home/dorian/code/blokboi /home/dorian/code/blokboi/src /home/dorian/code/blokboi/src/CMakeFiles/blokboi.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/CMakeFiles/blokboi.dir/depend

