#!/bin/bash


SAS_TOP_DIR=$(cd "`dirname $0`" ; pwd)

# Load module configuration library
. ${SAS_TOP_DIR}/config/sas_test_config
source ${SAS_TOP_DIR}/config/sas_test_lib

# Load the public configuration library
. ${SAS_TOP_DIR}/../config/common_config
. ${SAS_TOP_DIR}/../config/common_lib


# Main operation function
# IN : N/A
# OUT: N/A
function main()
{
    Module_Name="SAS"
    
    echo $SAS_TOP_DIR

    for key in "${!case_map[@]}"
    do
        echo $key " : " ${case_map[$key]}
        case "${case_map[$key]}" in
            on)
                commd="${key}.sh"
                source ${SAS_TOP_DIR}/case_script/$commd
            ;;
            off)
            ;;
            *)
                echo "sas_test_config file test case flag parameter configuration error."
                echo "please configure on and off."
                echo "on  - open test case."
                echo "off - close test case."
            ;;
       esac
    done
}


#lava-test-case的定义位于hip06D03-06/bin文件夹，我们的ci_testcase文件夹也与bin位于同一层文件夹
#PATH="./../bin:${PATH}"
echo $(pwd)
python ${SAS_TOP_DIR}/AddPath.py
echo $PATH

#Output log file header
writeLogHeader

# Get all disk partition information
get_all_disk_part

main

# clean exit so lava-test can trust the results
exit 0

