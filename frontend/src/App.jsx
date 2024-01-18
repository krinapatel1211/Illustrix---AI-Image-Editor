import './App.css';
import 'antd/dist/reset.css';
// import { Layout, Space, ConfigProvider } from 'antd';
// import LandingHeader from './landing_header/LandingHeader';
// import LandingMain from './landing_main/LandingMain'
import Landing from './Landing';
// import EditMain from './edit_screen/EditMain';
import WrapperEditMain from './edit_screen/WrapperEditMain';
import {BrowserRouter,Route,Routes} from "react-router-dom";
// import ProtectedRoute from './auth/ProtectedRoute';
// import AuthProvider from './auth/AuthProvider';

function App() {
    return (
        <BrowserRouter>
            {/* <AuthProvider> */}
                <Routes>
                    <Route path="/" element={<Landing/>}/>
                    {/* <Route path="/edit" element={<WrapperEditMain/>} /> */}
                    {/* <ProtectedRoute path="/edit" element={<WrapperEditMain/>} /> */}
                    {/* <Route exact path='/edit' element={<ProtectedRoute/>}> */}
                    <Route path="/edit" element={<WrapperEditMain/>} />
                    {/* </Route> */}
                </Routes>
            {/* </AuthProvider> */}
        </BrowserRouter>
    );
}

export default App;
