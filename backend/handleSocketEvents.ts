import { Socket } from 'socket.io';
import { writeFile } from 'fs';

export const handleSocketEvents = (socket: Socket) => {
  socket.on('file-upload', (file, callback) => {
    console.log(file)
    writeFile('/', file, (err) => {
      console.log(err)
      callback({ message: err ? 'failure' : 'success' });
    });
  });
};
