import React, { useState } from 'react'
import { useForm } from 'react-hook-form'
import { httpClient } from './utils/http'

export default () => {
  const { register, handleSubmit } = useForm()
  const [json, setJson] = useState()

  const onSubmit = async data => {
    const formData = new FormData()

    Object.keys(data).forEach(key => {
      formData.append(key, data[key])
    })

    const res = await httpClient({
      url: '/info',
      method: 'post',
      data: new URLSearchParams(formData),
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    })

    if (res.data) setJson(JSON.stringify(res.data, null, 2))
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      {json ?
        <pre style={{ padding: 70, whiteSpace: "pre-wrap", wordBreak: "break-all" }}> {json} </pre>
        :
        <>
          <input name='pagelink' placeholder='https://www.youtube.com/xxxx' ref={register} />
          <input type='submit' />
        </>
      }
    </form>
  )
}
