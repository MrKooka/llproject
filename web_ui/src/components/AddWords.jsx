import React, { useEffect, useState } from 'react';
import { Form, Button, Row, Col } from 'react-bootstrap'
import axios from 'axios'
import { gapi } from "gapi-script"


const AddWords = () => {
    const [eng, setEng] = useState('')
    const [ru, setRu] = useState('')
    const [context, setContex] = useState('')
    const [sugList, setSugList] = useState([])

    const sendForm = (event) => {
        event.preventDefault();
        console.log({
            ru: ru,
            eng: eng,
            context: context ? context : 'context',
            
        });
        axios.post('http://127.0.0.1:8000/api/word/ ', {
            ru: ru,
            eng: eng,
            context: context ? context : 'context',
            user: ["412bcd27-bca3-4d64-a4fd-4b2364ada541"]
        }).then((res) => { console.log(res.data); })
        setEng('')
        setRu('')
        setContex('')



    }
    
    useEffect(()=>{
        if (eng){
            const res = axios.get(`http://127.0.0.1:8000/api/existword/${eng}`)
            // res.then((v)=>console.log(v.data));
            res.then((v)=>{setSugList(v.data)})
            console.log('sugList',sugList);
        }
    },[eng])
    return (
        <div>
            <Row className="justify-content-md-center mt-4" >
                <Col lg={5}>
                    <Form onSubmit={sendForm}>
                        <Form.Group className="mb-3" controlId="formBasicPassword">
                            <Form.Label>English</Form.Label>
                            <Form.Control value={eng} onChange={(e) => { setEng(e.target.value) }} />
                            {sugList.length >0 ? sugList.map((s, i)=>
                                <div key={i}  > {s.eng} | {s.ru} </div>
                            ) : <div></div>}
                        </Form.Group>
                        <Form.Group className="mb-3" controlId="formBasicEmail">
                            <Form.Label>Russian</Form.Label>
                            <Form.Control value={ru} onChange={(e) => { setRu(e.target.value) }} />
                        </Form.Group>

                        <Form.Group className="mb-3" controlId="formBasicPassword">
                            <Form.Label>Meaning</Form.Label>
                            <Form.Control as="textarea" rows={3} value={context} onChange={(e) => { setContex(e.target.value) }} />
                        </Form.Group>

                        <Button variant="primary" type="submit">
                            Сохранить
                        </Button>
                    </Form>
                </Col>
            </Row>
        </div>
    );
};

export default AddWords;