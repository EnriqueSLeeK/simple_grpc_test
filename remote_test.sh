#!/bin/bash

echo "Remote test"

old_rpyc="conn = rpyc.connect('localhost'"
new_rpyc="conn = rpyc.connect('$IP'"

sub_rpyc="s/$old_rpyc/$new_rpyc/"
rev_rpyc="s/$new_rpyc/$old_rpyc/"

cd rpyc \
    && sed -i "$sub_rpyc" rpyc_client.py \
    && sleep 1\
    && for i in {0..5}; do python rpyc_client.py <<< "500"; done

sed -i "$sub_rpyc" rpyc_stop.py

python rpyc_stop.py

sed -i "$rev_rpyc" rpyc_client.py
sed -i "$rev_rpyc" rpyc_stop.py

old_grpc="channel = grpc.insecure_channel('\[::\]:50051')"
new_grpc="channel = grpc.insecure_channel('$IP:50051')"

sub_grpc="s/$old_grpc/$new_grpc/"
rev_grpc="s/$new_grpc/$old_grpc/"

cd ../grpc\
    && sed -i "$sub_grpc" grpc_client.py \
    && sleep 1\
    && for i in {0..5}; do python grpc_client.py <<< "500"; done

sed -i "$sub_grpc" grpc_stop.py

python grpc_stop.py

sed -i "$rev_grpc" grpc_client.py
sed -i "$rev_grpc" grpc_stop.py
