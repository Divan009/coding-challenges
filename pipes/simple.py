"""
The pipe is unidirectional - data flows from
write_fd to read_fd.
Attempting to read from write_fd or write to
read_fd will fail.
"""

import os

read_fd, write_fd = os.pipe()

os.write(write_fd, b"Hello from pipe!")

data = os.read(read_fd, 100)

print(f"Received: {data.decode()}")

# Close file descriptors
os.close(read_fd)
os.close(write_fd)
