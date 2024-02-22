// api.js
import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/';

export const fetchData = async (endpoint) => {
  try {
    const response = await axios.get(API_BASE_URL + endpoint);
    return response.data;
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};

export const postData = async (endpoint, data) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/${endpoint}`, data);
    return response.data;
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};

// export async function getClubs() {
//   const res = await fetch("http://127.0.0.1:8000/clubs/clubs/1.json");
//   const data = await res.json();
//   return data;
// }
