import React from 'react';
import {
    Routes,
    Route,
    Navigate
} from "react-router-dom";
import AddWords from './components/AddWords';
import ListWords from './components/ListWords';
import Login from './components/Login';
import TrainWord from './components/TrainWord';

const AppRouter = () => {
    return (
        <div>
            <Routes>

                <Route path='add' element={<AddWords />} />
                <Route path='train' element={<TrainWord />} />
                <Route path='list' element={<ListWords/>} />
                <Route path='login' element={<Login/>}/>

                    




            </Routes>
        </div>
    );
};

export default AppRouter;