import { createApiInstance } from 'frontend/src/services/api';
import { setItem, getItem, removeItem } from 'frontend/src/utils/storage';

const TOKEN_KEY = 'auth_token';

// HUMAN ASSISTANCE NEEDED
// The login function has a confidence level below 0.8 and may need review
async function login(email: string, password: string): Promise<boolean> {
  try {
    const api = createApiInstance();
    const response = await api.post('/auth/login', { email, password });
    
    if (response.data && response.data.token) {
      setItem(TOKEN_KEY, response.data.token);
      return true;
    }
    return false;
  } catch (error) {
    console.error('Login failed:', error);
    return false;
  }
}

function logout(): void {
  removeItem(TOKEN_KEY);
}

function isAuthenticated(): boolean {
  return !!getItem(TOKEN_KEY);
}

export { login, logout, isAuthenticated };