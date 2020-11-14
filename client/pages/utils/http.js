import axios from 'axios'
import { httpConfig } from '../configs/http-config'

const httpClient = (config) => {
  const instance = axios.create({ ...httpConfig, ...config })
  instance.defaults.timeout = httpConfig.timeout
  return instance(config)
}

export { httpClient }
