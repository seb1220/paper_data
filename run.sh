BIN="/bin/compApi"
LIBS="/libs"
BIN_PATH="$PWD$BIN"
LIBS_PATH="$PWD$LIBS"
if [ -z ${CAMERA_INDEX+x} ]; then
    echo "CAMERA_INDEX is unset, setting to 0";
    export CAMERA_INDEX=0;
else
    echo "CAMERA_INDEX is set to '$CAMERA_INDEX'";
fi
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib:/usr/local/lib/x86_64-linux-gnu:/lib/x86_64-linux-gnu:/usr/lib/x86_64-linux-gnu:$LIBS_PATH $BIN_PATH