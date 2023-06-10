#!/bin/bash

echo "Remote test"

old_rpyc="conn = rpyc.connect('$localhost'"
new_rpyc="conn = rpyc.connect('$IP'"

cd rpyc \
    && sed -i "s/$old_rpyc/$new_rpyc/" rpyc_client.py \
    && sleep 1\
    && for i in {0..5}; do python rpyc_client.py <<< "500"; done

sed -i "s/$old_rpyc/$new_rpyc/" rpyc_stop.py

python rpyc_stop.py

sed -i "s/$new_rpyc/$old_rpyc/" rpyc_client.py
sed -i "s/$new_grpc/$old_grpc/" rpyc_stop.py

old_grpc="channel = grpc.insecure_channel('[::]:50051')"
new_grpc="channel = grpc.insecure_channel('$IP:50051')"

cd ../grpc\
    && sed -i "s/$old_grpc/$new_grpc/" grpc_client.py \
    && sleep 1\
    && for i in {0..5}; do python grpc_client.py <<< "500"; done

sed -i "s/$old_grpc/$new_grpc/g" grpc_stop.py

python grpc_stop.py

sed -i "s/$new_grpc/$old_grpc/" grpc_client.py
sed -i "s/$new_grpc/$old_grpc/" grpc_stop.py
