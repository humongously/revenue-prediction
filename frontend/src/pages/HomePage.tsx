import { Button, Container, Form } from 'react-bootstrap';
import Main from '../components/Main';

export const HomePage = () => (
  <Main>
    <Container fluid>
      <div className="mx-4 py-4">
        <h2>Revenue Prediction Dashboard</h2>
        <div className="my-4">
          <Form>
            <Form.Group className="mt-2 mb-3" controlId="formBasicPassword">
              <Form.Label>Upload your CSV File</Form.Label>
              <Form.Control type="file" />
            </Form.Group>
            <Button variant="primary" type="submit">
              Upload
            </Button>
          </Form>
        </div>
      </div>
    </Container>
  </Main>
);
