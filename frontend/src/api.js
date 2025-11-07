import axios from "axios";

const api = axios.create({
  baseURL: "https://kbl-draft-prediction.onrender.com",  
});

export default api;

