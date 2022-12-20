import React, { useEffect, useState } from 'react';
import { Button, Container, Form } from 'react-bootstrap';
import { io, Socket } from 'socket.io-client';
import Main from '../components/Main';
import {
  Bar,
  BarChart,
  CartesianGrid,
  Cell,
  Legend,
  Pie,
  PieChart,
  Tooltip,
  XAxis,
  YAxis,
} from 'recharts';
import { barChartData } from '../data/barChart';
import { pieChartData } from '../data/pieChart';
import { colors } from '../data/colors';

const SOCKET_URL = 'http://localhost:5000/';

export const HomePage = () => {
  const [file, setFile] = useState<File>();
  const [socket, setSocket] = useState<Socket>();
  const [isConnected, setIsConnected] = useState(false);

  useEffect(() => {
    const socket = io(SOCKET_URL, {
      transports: ['websocket'],
    });

    setSocket(socket);

    socket.on('connect', () => {
      setIsConnected(true);
    });

    socket.on('connect_error', (e) => console.log(e));

    socket.on('disconnect', () => {
      setIsConnected(false);
    });

    return () => {
      socket.off('connect');
      socket.off('disconnect');
      socket.off('pong');
    };
  }, []);

  const setInputFile = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.currentTarget.files?.[0];
    if (file) setFile(file);
  };

  const uploadFile = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault();
    if (!(isConnected && socket)) return;

    socket.emit('file-upload', file, (status: string) => {
      console.log(status);
    });
  };

  return (
    <Main>
      <Container fluid>
        <div className="mx-4 py-4">
          <h2>Revenue Prediction Dashboard</h2>
          <div className="my-4">
            <div>
              WebSocket Connection Status:{' '}
              <span className="text-capitalize">
                {isConnected ? 'connected' : 'disconnected'}
              </span>
            </div>
            <Form>
              <Form.Group className="mt-2 mb-3" controlId="formBasicPassword">
                <Form.Label>Upload your CSV File</Form.Label>
                <Form.Control type="file" onChange={setInputFile} />
              </Form.Group>
              <Button variant="primary" type="submit" onClick={uploadFile}>
                Upload
              </Button>
            </Form>
          </div>
          <div>
            <h3 className="mb-4">Results</h3>
            <div className="d-flex flex-column gap-5">
              <div>
                <h4 className="mb-4">Items and their prices</h4>
                <BarChart width={1300} height={250} data={barChartData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="name" />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Bar dataKey="price" fill="#8884d8" />
                </BarChart>
              </div>

              <div>
                <h4>Category distribution</h4>
                <div className="d-flex justify-content-center">
                  <PieChart width={800} height={550}>
                    <Pie
                      data={pieChartData}
                      dataKey="percentage"
                      cx="50%"
                      cy="50%"
                      innerRadius={60}
                      outerRadius={80}
                      fill="#82ca9d"
                      paddingAngle={2}
                      label
                    >
                      {pieChartData.map((_, index) => (
                        <Cell fill={colors[index % colors.length]} />
                      ))}
                    </Pie>
                    <Tooltip />
                    <Legend />
                  </PieChart>
                </div>
              </div>
            </div>
          </div>
        </div>
      </Container>
    </Main>
  );
};
