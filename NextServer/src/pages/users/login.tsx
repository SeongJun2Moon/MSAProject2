import { ChangeEvent,FormEvent, useState } from "react"
import { NextPage } from "next"
import { Login} from "@/src/components/user"
import { UserLoginInput } from "@/src/modules/types"
import { useDispatch } from "react-redux"
import { loginRequest } from "@/src/modules/slices"
import {useAppDispatch, useAppSelector} from '@/src/hooks'



const LoginPage: NextPage = function(){
    const [loginInfo, setLoginInfo] = useState<UserLoginInput>({email : '', password: ''})
    const dispatch = useAppDispatch()

    const onChange = (e: React.FormEvent<HTMLTextAreaElement | HTMLInputElement>) => {
        e.preventDefault()
        const { name, value} = e.currentTarget
        setLoginInfo({...loginInfo, [name]:value})
    }
    const onSubmit = (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault()
        
        dispatch(loginRequest(loginInfo))
    }
    return (
        <>
           <Login onChange={onChange} onSubmit={onSubmit}/>
        </>
            
        
 );
}
LoginPage.getInitialProps =async (ctx) => {
    const pathname = ctx.pathname
    return { pathname }
}
export default LoginPage