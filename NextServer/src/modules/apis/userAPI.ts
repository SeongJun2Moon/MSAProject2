import axios, { AxiosResponse } from 'axios'
import { context } from '@/src/components/admin/enum'
import { currentTime } from '@/src/components/admin/utils'
import { User } from '@/src/modules/types'
import { author, client } from "@/src/modules/controllers"

export const user = {
    async join(payload: User){
            try{
                const response : AxiosResponse<any, User[]> =
                await axios.post(`http://127.0.0.1:8000/users/register`, payload, {headers: {
                    "Content-Type" : "application/json",
                    Authorization: "JWT fefege...",
                }})
                if(response.data === "success"){
                    alert(' 결과: API 내부 join 성공  '+ JSON.stringify(response.data))
                }else{
                    alert(` 결과: ${response.data.msg}  `)
                }
                return response
            }catch(err){
                console.log(` ${currentTime} : userSaga 내부에서 join 실패 `)
            }
        },

    async login(payload: User){
        try{
            const response : AxiosResponse<any, User[]> =
            await author.post('http://localhost:8000/users/login', payload)
            // alert(` 서버에서 리턴받은 값: ${JSON.stringify(response.data.email)}`)
            alert(`4 API payload is ${JSON.stringify(response.data)}`)
            localStorage.clear()
            const data = response.data
            localStorage.setItem("email", data.email)
            alert(`API 스토리지에 저장된 토큰 ${localStorage.getItem("session")}`)
            return data.msg
        }catch(err){
            return err;
        }
    },
    
    async logout(payload: User){
        try{
            // await client.post('/users/logout')
            const response : AxiosResponse = await client.post('/users/logout', payload)
            return response.data
        } catch(err){
            console.log(err)
            return err;
        }
    },
    
    async userInfo(){
        try{
            const response : AxiosResponse = await client.get(`/users/join`)
            return response.data
        } catch(err) {
            console.log(err)
            return err
        }
    }
    
}