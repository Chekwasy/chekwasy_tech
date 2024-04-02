import Navbar from './Navbar';
import Sidebar from './sidebar'
import Main from './main';

function App() {
  return (
    <div className="App">
      <div className="container">
        <Navbar />
        <div className="main">
          <Sidebar />
          <Main />
        </div>
      </div>
    </div>
  );
}

export default App;
