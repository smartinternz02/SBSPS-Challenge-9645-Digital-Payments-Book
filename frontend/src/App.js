import './App.css';
import { BrowserRouter as Router, Routes, Route, Outlet, Link } from "react-router-dom";
import PurchaseHistory from './pages/purchaseHistory';
import PaymentHistory from './pages/paymentHistory';
import Layout from './pages/Layout';
import Auth from './pages/Auth';
import Home from './pages/Home';
import NoMatch from './pages/NoMatch';
function App() {
  return (
    <div className='app'>
      <Router>
       <Routes>
          <Route index element={<Home />} />
          <Route path="/purchase-history" exact element={<PurchaseHistory/>} />
          <Route path="/payment-history" exact element={<PaymentHistory/>} />
          <Route path="/auth" exact element={<Auth/>} />
          <Route path="*" element={<NoMatch />} />
      </Routes>
      </Router>
    </div>
  );
}

export default App;
