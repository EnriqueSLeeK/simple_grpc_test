
compile-proto: generate-proto
	@echo "Compile proto files"
	@[[ -d compiled ]] || mkdir compiled
	@protoc --python_out=compiled proto_files/*.proto
	@mv compiled/proto_files/* compiled
	@rmdir compiled/proto_files

generate-proto:
	@echo "Generating proto files"
	@python proto_files/generate_proto_file.py
	@mv *.proto proto_files

clean:
	@echo "Cleaning up some files"
	@rm proto_files/*.proto

fclean: clean
	@echo "Full clean"
	@rm -rf compiled
