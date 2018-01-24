#!/bin/bash

CUR=$(cd "`dirname $0`" ; pwd)

echo ${CUR}

# Load common function
#. roce_autotest/config/roce_test_lib
. ${CUR}/config/roce_test_lib

# Main operation function
# IN : N/A
# OUT: N/A
function main()
{
    Module_Name="ROCE"
    
    for key in "${!case_map[@]}"
    do
        case "${case_map[$key]}" in
            on)
                commd="${key}.sh"
                source $TEST_CASE_PATH/$commd
            ;;
            off)
            ;;
            *)
                echo "roce_test_config file test case flag parameter configuration error."
                echo "please configure on or off."
                echo "on  - open test case."
                echo "off - close test case."
            ;;
       esac
    done
}

#get the internet ip of servcie
LC_ALL=C ifconfig | grep 'inet addr:' | grep -v '127.0.0.1' | cut -d: -f2 | awk '{print $1}'

CurrIp=$1
print ${CurrIp}
#get the BACK_IP
declare -A ip_map
ip_map=(
["192.168.3.238"]="192.168.3.211"
["192.168.3.211"]="192.168.3.238"
)

for tmpip in "${!ip_map[@]}"
do
 if ${tmpip} == $CurrIp
 then
	BACK_IP=${ip_map[$tmpip]}
 fi
done



# Output log file header
#writeLogHeader

#TrustRelation ${BACK_IP}
#copy_tool_so
#main

echo "testmain finish"
# clean exit so lava-test can trust the results
exit 0

