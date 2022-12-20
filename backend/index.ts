import express from 'express';
import http from 'http';
import { Server } from 'socket.io';
import { handleSocketEvents } from './handleSocketEvents';

const app = express();
const server = http.createServer(app);

const io = new Server(server, {
  cors: {
    origin: '*',
  },
});

io.on('connection', (socket) => {
  console.log('a user connected');
  handleSocketEvents(socket);
});

server.listen(5000, () => {
  console.log('listening on *:5000');
});
