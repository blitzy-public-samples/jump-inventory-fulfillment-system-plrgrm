import axios, { AxiosInstance } from 'axios';
import { getAuthToken } from 'frontend/src/utils/auth';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;

const createApiInstance = (): AxiosInstance => {
  const instance = axios.create({
    baseURL: API_BASE_URL,
  });

  instance.interceptors.request.use(
    async (config) => {
      const token = await getAuthToken();
      if (token) {
        config.headers['Authorization'] = `Bearer ${token}`;
      }
      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
  );

  instance.interceptors.response.use(
    (response) => response,
    (error) => {
      if (error.response) {
        switch (error.response.status) {
          case 401:
            // Handle unauthorized access
            // HUMAN ASSISTANCE NEEDED: Implement proper unauthorized access handling (e.g., redirect to login)
            console.error('Unauthorized access');
            break;
          case 403:
            // Handle forbidden access
            console.error('Forbidden access');
            break;
          case 500:
            // Handle server errors
            console.error('Server error');
            break;
        }
      }
      return Promise.reject(error);
    }
  );

  return instance;
};

export default createApiInstance();