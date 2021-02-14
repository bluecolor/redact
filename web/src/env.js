const env = process.env.DUCK_ENV

let envApiUrl = ''

if (env === 'development') {
  envApiUrl = `http://${process.env.DUCK_API_DEV}`
} else if (env === 'production') {
  envApiUrl = `https://${process.env.DUCK_API_PROD}`
}

export const apiUrl = envApiUrl
export const appName = process.env.DUCK_APP_NAME
