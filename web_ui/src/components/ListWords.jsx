import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Table, Form, Button } from 'react-bootstrap';



const ListWords = () => {
    const [lw, setLw] = useState([])
    const [ruUpdate, setRuUpdate] = useState({})
    const [engUpdate, setEngUpdate] = useState({})

    useEffect(() => {
        const res = axios.get('http://127.0.0.1:8000/api/word/')
        res.then((data) => {
            setLw(data.data)

        })

    }, [])
    const deleteWord = (id) => {
        const res = axios.delete(`http://127.0.0.1:8000/api/deleteword/${id}`)
        res.then(data => setLw(data.data))

    }

    const changeWord = (id, value, eng = false) => {
        if (eng) {
            setEngUpdate({ ...engUpdate, id: id, value: value })
        } else {
            setRuUpdate({ ...ruUpdate, id: id, value: value })
        }
    }

    const sentRuUpdateWord = (event) => {
        event.preventDefault();
        console.log(ruUpdate);
        axios.post('http://127.0.0.1:8000/api/updateWord/', {
            id: ruUpdate.id,
            newWord: ruUpdate.value
        }).then((data) => { setLw(data.data); console.log(data.data); })
    }
    const sentEngUpdateWord = (event) => {
        event.preventDefault();
        console.log(ruUpdate);
        axios.post('http://127.0.0.1:8000/api/updateWord/', {
            id: engUpdate.id,
            newWord: engUpdate.value,
            eng: 1
        }).then((data) => { setLw(data.data) })
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

                    {setLw.length > 0 ? lw.map((w) =>
                        <tr key={w.id}>
                            <td>{w.id}</td>
                            <td>{w.ru}
                                <Form onSubmit={sentRuUpdateWord}>
                                    <Form.Control
                                        className="mt-3"
                                        onChange={(e) => { changeWord(w.id, e.target.value) }}
                                    />
                                </Form>

                            </td>
                            <td>{w.eng}
                                <button onClick={() => {
                                    const audio = new Audio(`http://127.0.0.1:8000/api/voice/${w.id}`);
                                    audio.play()
                                }} type="button" class="btn btn-secondary btn-sm" style={{"margin-left":"10px"}}>
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-play" viewBox="0 0 16 16">
                                        <path d="M10.804 8 5 4.633v6.734L10.804 8zm.792-.696a.802.802 0 0 1 0 1.392l-6.363 3.692C4.713 12.69 4 12.345 4 11.692V4.308c0-.653.713-.998 1.233-.696l6.363 3.692z" />
                                    </svg>
                                </button>


                                <Form onSubmit={sentEngUpdateWord}>
                                    <Form.Control
                                        className="mt-3"
                                        onChange={(e) => { changeWord(w.id, e.target.value, true) }}
                                    />
                                </Form>
                            </td>
                            <td>{w.context}</td>

                            <td><button className="btn btn-outline-danger" onClick={() => { deleteWord(w.id) }}>Delete</button></td>

                        </tr>
                    ) : <tr></tr>}


                </tbody>
            </Table>
        </div>
    );
};

export default ListWords;