echo "Building ROS nodes"

cd Examples/ROS/ORB_SLAM2_save_and_load
mkdir build
cd build
cmake .. -DROS_BUILD_TYPE=Release
make -j4
