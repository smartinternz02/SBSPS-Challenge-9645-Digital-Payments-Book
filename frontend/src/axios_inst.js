import axios from 'axios';

const client = axios.create({
    baseURL: "http://127.0.0.1:8000/api/user",
    headers: {
        post: {        // can be common or any other method
          token: localStorage.getItem("token")
        },
        get: {        // can be common or any other method
            token: localStorage.getItem("token")
          },
        //   'Content-type': 'application/json'

      } 
  });

export default client