# ORB_SLAM2_save_and_load

Developed based on ORB-SLAM2, adding map saving and loading functions, mainly using the boost library to achieve.

## Map Save/Load

#### Enable:

You can enable this feature by defining a new variable `USE_MAP_SAVE_LOAD` when running cmake.

For example, you can change `cmake .. -DCMAKE_BUILD_TYPE=Release` to `cmake .. -DCMAKE_BUILD_TYPE=Release -DUSE_MAP_SAVE_LOAD=1` after `echo "Configuring and building ORB_SLAM2 ..."` in `build.sh`.

But `CMakeCache.txt` should be deleted if you want to undefine this variable.

#### Usage:

This feature is integrated with `class System`. The path of mapfile can be set by adding `Map.mapfile: map.bin` to ORB_SLAM2's settings file. See the last few line of `Example/Monocular/TUM1.xml`.

To save a map, you need construct `ORB_SLAM2::System` with the last parameter be `true`. Then the `System` will save map to mapfile specified in setting file when `ShutDown`.

With a readable mapfile, map will be loaded automatically and `System` will run in localization mode, but you can change it to SLAM mode later.

If you set a mapfile but it doesn't exist, `System` will create new map.

mono_tum has been updated as a simple example of this functionality. An extra command line parameter(0 or 1) should be given to indicate whether you want to save map or not.

#### Implementation related:

I use boost_serialization library to serialize `Map`, `MapPoint`, `KeyFrame`,`KeyFrameDatabase`, `cv::Mat`, `DBoW2::BowVector`, `DBoW2::FeatureVector`. In brief, only the `ORBVector` isn't serialized.

This feature is tested with boost 1.64 and it works fine mostly. There is still some occasional segmentfault to dig in.
