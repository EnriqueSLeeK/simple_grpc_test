
data_types = ["string", "int32", "float", "double"]


def write_message(proto_file, name, mode):

    action = "recv"
    if mode:
        action = "send"

    proto_file.write(f"message {name}{action.title()} {{\n")
    proto_file.write(f"\t{name} {name}_data_{action} = 1;\n")
    proto_file.write("}\n")


def write_service(proto_file, data_type):
    proto_file.write(f"service {data_type}Test {{\n")
    proto_file.write(f"\trpc {data_type}Return ({data_type}Send) returns\n")
    proto_file.write(f"\t\t({data_type}Recv);\n")
    proto_file.write("}\n")


def main():
    for data_type in data_types:
        with open(f"{data_type}.proto", "w") as proto_file:
            proto_file.write("syntax = \"proto3\";\n")
            proto_file.write("\n")
            write_service(proto_file, data_type)
            proto_file.write("\n")
            write_message(proto_file, data_type, 1)
            proto_file.write("\n")
            write_message(proto_file, data_type, 0)

    return 0


if __name__ == "__main__":
    main()
