#!/bin/bash

# Disk negotiated link rate query
# IN : N/A
# OUT: N/A


function disk_negotiated_link_rate_query()
{
    Test_Case_Title="disk_negotiated_link_rate_query"
    Test_Case_ID="ST.FUNC.002/ST.FUNC.003"
    
    for dir in `ls ${PHY_FILE_PATH}`
    do
        type=`cat ${PHY_FILE_PATH}/${dir}/device_type`
        [ x"$type" != x"end device" ] && continue
        
        rate_value=`cat ${PHY_FILE_PATH}/${dir}/negotiated_linkrate | awk -F '.' '{print $1}'`
	echo $rate_value
        BRate=1
        for rate in `echo $DISK_NEGOTIATED_LINKRATE_VALUE | sed 's/|/ /g'`
        do
            if [ $rate_value -eq $rate ]
            then
                BRate=0
                break
            fi
        done

        if [ $BRate -eq 1 ]
        then
            writeFail "\"${dir}\" negotiated link rate query ERROR."
	    lava-test-case "disk_negotiated_link_rate_query(luojiaxing_437090)" --result fail
            return 1
        fi
    done

    lava-test-case "disk_negotiated_link_rate_query(luojiaxing_437090)" --result pass

    writePass
}

function main()
{
    JIRA_ID="PV-66/PV-69"
    Test_Item="physical data rate"
    disk_negotiated_link_rate_query
}


PATH="./../../bin:${PATH}"
main
exit 0
