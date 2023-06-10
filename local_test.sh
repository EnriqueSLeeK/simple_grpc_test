
echo "Local test"

echo 'Caso tenha algum processo em python nao execute esse script :p'
read

killall 'python'

cd rpyc \
    && (python rpyc_server.py&) \
    && sleep 1\
    && for i in {0..5}; do python rpyc_client.py <<< "500"; done

killall 'python'

cd ../grpc\
    && (python grpc_server.py&)\
    && sleep 1\
    && for i in {0..5}; do python grpc_client.py <<< "500"; done

killall 'python'
