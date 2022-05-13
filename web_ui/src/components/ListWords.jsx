import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Table} from 'react-bootstrap';



const ListWords = () => {
    const [lw, setLw] = useState([])

    useEffect(() => {
        const res = axios.get('http://127.0.0.1:8000/api/word/')
        res.then((data)=>{
            setLw(data.data)
            
        })
        // console.log(lw);

    }, [])
    const deleteWord = (id)=>{
        const res = axios.delete(`http://127.0.0.1:8000/api/deleteword/${id}`)
        res.then(data =>setLw(data.data))
        
    }
    return (
        <div>
            <h3 >Total: {lw.length}</h3>
            <Table striped bordered hover >
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Rusian</th>
                        <th>English</th>
                        <th>Meaning</th
                        >
                        <th>Action</th>

                    </tr>
                </thead>
                <tbody>

                    {setLw.length > 0 ? lw.map((w)=>
                        <tr key={w.id}>
                            <td>{w.id}</td>
                            <td>{w.ru}</td>
                            <td>{w.eng}</td>
                            <td>{w.context}</td>
                            <td><button className="btn btn-outline-danger" onClick={()=>{deleteWord(w.id)}}>Delete</button></td>

                        </tr>
                    ): <tr></tr>}
                </tbody>
            </Table>
        </div>
    );
};

export default ListWords;