import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Vote from "./pages/Vote";
import Result from "./pages/Result";

export default function App() {
  return (
    <BrowserRouter basename="/kbl-draft-prediction">
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/vote" element={<Vote />} />
        <Route path="/result" element={<Result />} />
      </Routes>
    </BrowserRouter>
  );
}
