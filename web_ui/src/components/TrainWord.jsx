import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Button, Card, Col, Row } from 'react-bootstrap';
import PostService from '../api/postService';
const TrainWord = () => {

    const [listWords, setListWords] = useState([])
    const [count, setCount] = useState(0)

    const nextWords = (count) => {
        console.log(count);
        if (count != 0) {
            console.log('if');
            console.log(count);
            const res = PostService.getTrainWords(count)
            res.then(res => {
                setListWords(res.data)
                console.log(listWords[0])
            })
        } else {
            console.log('else');
            console.log(count);

            const res = PostService.getTrainWords()
            res.then(res => {
                setListWords(res.data)
                console.log(listWords[0])
            })
        }


    }
    useEffect(() => {
        nextWords()
    }, [])
    return (
        <div>
            <Row className="justify-content-md-center mt-4" >
                <Col lg={3}>
                    <Card style={{ width: '18rem' }}>
                        <Card.Body>
                            <Card.Title>{listWords[count] ? listWords[count].ru : nextWords(count)}</Card.Title>
                            <Card.Text>{listWords[count] ? listWords[count].eng : nextWords(count)}</Card.Text>
                            <Card.Link href="#">Card Link</Card.Link>
                            <Card.Link href="#">Another Link</Card.Link>
                        </Card.Body>
                    </Card>
                    <Button variant="primary" type="submit" onClick={() => setCount(count + 1)}>
                        Следующее слово 
                    </Button>
                </Col>
            </Row>
        </div>
    );
};

export default TrainWord;