#!/bin/bash

# Log Colors
COLOR_INFO="\033[0;34m"
COLOR_WARNING="\033[1;33m"
COLOR_ERROR="\033[0;31m"
NOCOLOR='\033[0m'

# Env Vars
SIMULATOR_PATH="/home/leonel/facu/lifia/DRT-driving-simulator"

CARLA_SV_PATH="/home/leonel/facu/lifia/DRT-driving-simulator/Carla"
CARLA_SV_IP="localhost"
CARLA_SV_PORT="2000"
CARLA_SV_ARGS=""

CARLA_CLIENT_ARGS=""
ENV_CMD="source env/bin/activate"

is_carla_sv_running() {
    nc -z $CARLA_SV_IP $CARLA_SV_PORT
}

wait_carla_sv() {
	until is_carla_sv_running
	do
		echo -e "${INFO_COLOR}Waiting carla sv${NOCOLOR}"

		sleep 2
	done
}

launch_carla_sv() {
	echo -e "${INFO_COLOR}Starting carla sv . . .${NOCOLOR}"

	bash $CARLA_SV_PATH/CarlaUE4.sh $CARLA_SV_ARGS
}

launch_carla_client() {
	echo -e "${INFO_COLOR}Starting carla client . . .${NOCOLOR}"

	wait_carla_sv
    cd "simulator"
	python3 app.py $CARLA_CLIENT_ARGS
}

launch_face_detector() {
	echo -e "${INFO_COLOR}Starting face detector . . .${NOCOLOR}"

	cd "face-detector"
	python3 face_detection_on_webcam.py
}

if  is_carla_sv_running; then
    echo "Carla is already running, can't have multiple instances..."
    exit 1
fi

cd $SIMULATOR_PATH

$ENV_CMD
launch_carla_sv 1>&2 | launch_carla_client 1>&2 | launch_face_detector 1>&2
