import axios from "axios";

const API = axios.create({
  baseURL: "https://monday-bi-agent-cqgn.onrender.com",
});

export default API;