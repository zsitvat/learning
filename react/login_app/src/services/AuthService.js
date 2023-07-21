
   
import axios from "axios";

let accessToken = "";

export function login(email, password) {
  return axios
    .post("https://kodbazis.hu/api/login-user", { email, password }, { withCredentials: true })
    .then((res) => {
      accessToken = res.data.accessToken;
    });
}

export function logout() {
  return axios.post("https://kodbazis.hu/api/logout-user", {}, { withCredentials: true })
    .then((res) => {
      accessToken = "";
    });
}

export const fetchHitelesitessel = axios.create();

fetchHitelesitessel.interceptors.request.use(
  (config) => {
    if (!accessToken) {
      return config;
    }

    return {
      ...config,
      headers: {
        ...config.headers,
        Authorization: `Bearer ${accessToken}`,
      }
    };
  },
  (error) => Promise.reject(error)
);

fetchHitelesitessel.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response.status !== 403) {
      return Promise.reject(error);
    }

    const originalRequest = error.config;

    if (originalRequest.isRetry) {
      return Promise.reject(error);
    }

    originalRequest.isRetry = true;

    return axios
      .get("https://kodbazis.hu/api/get-new-access-token", {
        withCredentials: true,
      })
      .then((res) => {
        accessToken = res.data.accessToken;
      })
      .then(() => fetchHitelesitessel(originalRequest));
  }
);

    