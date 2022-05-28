import React, { useEffect } from 'react';
import {
    Routes,
    Route,
    Navigate
} from "react-router-dom";
import AddWords from './components/AddWords';
import ListWords from './components/ListWords';
import Login from './components/Login';
import Logout from './components/Logout';

import TrainWord from './components/TrainWord';

import { gapi } from "gapi-script"
import TestComponent from './components/TestComponent';


const clientId = "383926561924-0kr85vallh5j759q23i127s0mqor1ihg.apps.googleusercontent.com"
const AppRouter = () => {
    useEffect(()=>{
        const start = ()=>{
            gapi.client.init({
                clientId:clientId,
                scope:""
            })
        }
        gapi.load('client:auth2', start)
    })
    
    return (
        <div>
            <Routes>

                <Route path='add' element={<AddWords />} />
                <Route path='train' element={<TrainWord />} />
                <Route path='list' element={<ListWords/>} />
                <Route path='login' element={<Login/>}/>
                <Route path='logout' element={<Logout/>}/>
                <Route path='test' element={<TestComponent/>}/>
                



                    




            </Routes>
        </div>
    );
};

export default AppRouter;