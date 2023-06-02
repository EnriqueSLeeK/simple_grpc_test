
compile-proto: proto_files/grpc_service.proto
	@echo "Compiling proto file"
	protoc --python_out=. proto_files/grpc_service.proto

