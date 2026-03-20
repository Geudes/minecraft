import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query"

import type { CreateServer, UpdateServer } from "./server-type"
import ServerApi from "../api/server-api"

export const useServers = () =>{
     const queryClient = useQueryClient()
     const useGetAll = () => useQuery({
        queryKey:['servers'],
        queryFn:() => ServerApi.getAll()
     })
     const useGetOne = (id:string | number) => useQuery({
        queryKey:['servers' , id],
        queryFn: () => ServerApi.getOne(id),
        enabled: !!id
     })
     const useCreate = () => useMutation({
        mutationFn:(form:CreateServer) => ServerApi.create(form),
        onSuccess:() => {
            queryClient.invalidateQueries({queryKey:['servers']})
        }
     })
   const useUpdate = () => useMutation({
    mutationFn: ({ id, form }: { id: string | number, form: UpdateServer }) => 
        ServerApi.update(id, form),
    onSuccess: (_, variables) => {
        queryClient.invalidateQueries({ queryKey: ['servers'] })
        queryClient.invalidateQueries({ queryKey: ['servers', variables.id] })
    }
})

     return  {useGetAll , useGetOne , useCreate , useUpdate }
}