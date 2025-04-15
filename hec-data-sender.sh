#!/bin/bash
# This script sends data to Splunk local instance via HEC (HTTP Event Collector) using curl.
echo "Enter Splunk HEC token: "
read hec_token
echo "Enter Splunk HEC index: "
read hec_index
echo "Enter how many POST requests you want to send: "
read num_requests

for i in $(seq 1 $num_requests)
    do curl -k https://localhost:8088/services/collector/event \
       -H "Authorization: Splunk $hec_token" \
       -H "Content-Type: application/json" \
       -d '{"event": "172.31.1.2 - - [2025-03-17 20:47:57] \"DELETE /api/v1/orders HTTP/1.1\" 401 4677 \"-\" \"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT10.0; Trident/5.0)\"","index": "'$hec_index'", "sourcetype": "access_combined"}' \
       && sleep 1
done


