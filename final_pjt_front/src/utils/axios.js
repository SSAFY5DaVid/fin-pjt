import axios from "axios"

const DOMAIN = "https://api.themoviedb.org/3/"
const API_KEY = process.env.VUE_APP_THEMOVIEDB_API_KEY
const request = axios.create({
  baseURL: "https://api.themoviedb.org/3/",
  params: {
    api_key: API_KEY,
    language: "ko-KR",
  },
});
export const movieApi = {
  nowPlaying: () => request.get("movie/now_playing"),
  popular: () => request.get("movie/popular"),
  upComing: () => request.get("movie/upcoming"),
  movieDetail: (id) =>
    request.get(`movie/${id}`, {
      params: { append_to_response: "videos" },
    }),
  search: (keyword) =>
    request.get(`search/movie/`, {
      params: {
        query: keyword,
      },
    }),
}
