#!/bin/bash

# Minified version of the exact same script with hardcoded vars and making using of only /dev/tcp and no checks.
function get_flag() {
    FLAG_FMT="SSCIT"
    if [[ -z $CHALLENGE_ID || -z $TEAM_ID || -z $USER_ID ]]; then
        echo "CHALLENGE_ID or TEAM_ID or USER_ID is empty. Make sure that the variables are set properly."
        exit 1
    fi
    exec 3<>/dev/tcp/172.17.0.1/9512
    echo -en "GET /flag?chal_id=$CHALLENGE_ID&team_id=$TEAM_ID&user_id=$USER_ID HTTP/1.1\nHost: $FLAG_ENDPOINT_HOST\n\n\n" >&3
    while IFS= read -r -u 3 line; do tmp=$(echo "$line" | grep -ioE "$FLAG_FMT{.*}"); if [[ $? == 0 ]]; then flag=$(echo $tmp); fi; done
    exec 3<&-
    if [[ "$flag" == "" ]]; then echo "SSCIT{n1c3_but_dont_trust_0n_nu11}"; else echo $flag; fi
}
rm -f /flag /app/flag.txt
get_flag > /app/flag.txt
rm -- "$0"
/docker-entrypoint.sh