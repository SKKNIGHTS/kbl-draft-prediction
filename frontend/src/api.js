import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",  // ✅ 반드시 FastAPI 주소
});

export default api;

