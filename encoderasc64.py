import base64
message = input("What is you string: ")
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')
print(base64_message)
print("By fortisnighis")


# if u want make it a function
