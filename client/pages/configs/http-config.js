// const currentBaseUrl = (() => {
//   const urlLoc = window.location
//   const baseUrl = urlLoc.protocol + '//' + urlLoc.hostname
//   return baseUrl
// })()

const currentBaseUrl = 'http://37.152.181.93'

const apiPort = process.env.API_PORT || 8080

const httpConfig = {
  url: '',
  method: 'get',
  baseURL: `${currentBaseUrl}:${apiPort}`,
  timeout: 30000,
  withCredentials: false,
  responseType: 'json',
  maxContentLength: Math.pow(2, 10) * 50,
  validateStatus: status => status >= 200 && status < 600,
  maxRedirects: 5,
  httpErrorMsg: 'خطای سیستمی رخ داده است، با پشتیبانی تماس بگیرید'
}

export { httpConfig }
