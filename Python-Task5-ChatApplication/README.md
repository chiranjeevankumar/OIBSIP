# Chat Application

## Description
A Python socket-based chat application for real-time messaging between multiple clients.

## Features
- Multiple client connections
- Real-time message broadcasting
- Timestamped chat messages
- Join and disconnect notifications
- Username support
- Type `/quit` to leave the chat
- Uses Python sockets and threading

## Requirements
Python 3. No third-party packages are required.

## How to Run
1. Open a terminal in this folder.
2. Start the server: `python server.py`
3. Open another terminal and run: `python client.py`
4. Open a third terminal and run `python client.py` for another user.
5. Enter a username for each client and begin chatting.
6. Type `/quit` to leave.

Use `127.0.0.1` when clients and server run on the same computer.
For other computers, use the server computer's reachable IP address and allow
TCP port 12345 through the firewall.

## Safety
Run the server only on a trusted network.
