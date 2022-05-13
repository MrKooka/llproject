import axios from "axios";

export default class PostService {
    static async getTrainWords(offset) {
        if (offset) {
            const response = await axios.get(`http://127.0.0.1:8000/api/word/?offset=${offset}`)
            return response
        }else{
            const response = await axios.get(`http://127.0.0.1:8000/api/word/`)
            return response
        }

    }
        
};