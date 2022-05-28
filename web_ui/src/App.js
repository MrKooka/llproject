import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter,Link } from "react-router-dom";
import { Container} from 'react-bootstrap';
import AppRouter from "./AppRouter";
import MyNav from './components/MyNav';

function App() {
  return (
    <div className="App">
     
     <BrowserRouter>
      <MyNav/>
      <Container fluid>
        <AppRouter/>
      </Container>
     
     </BrowserRouter>
    </div>
  );
}

export default App;
