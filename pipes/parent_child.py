"""
parent closes its read end and writes to
the pipe. The child closes its write end
and reads from the pipe. This demonstrates
one-way communication.

Remember to close unused ends in both
processes to prevent resource leaks and
potential deadlocks.


"""

import os

# Create pipe before forking
read_fd, write_fd = os.pipe()

pid = os.fork()

if pid > 0:  # Parent process
    os.close(read_fd)  # Close unused read end

    # Send message to child
    message = "Hello child process!"
    os.write(write_fd, message.encode())
    os.close(write_fd)

    print("Parent sent message to child")
else:  # Child process
    os.close(write_fd)  # Close unused write end

    # Receive message from parent
    data = os.read(read_fd, 1024)
    print(f"Child received: {data.decode()}")
    os.close(read_fd)
