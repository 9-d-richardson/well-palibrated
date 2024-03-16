import { apiSlice } from "../services/apiSlice";

interface User {
    first_name: string;
    last_name: string;
    email: string;
}
interface CreateUserResponse {
    success: boolean;
    user: User;
}

const authApiSlice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        retrieveUser: builder.query<User, void>({
            query: () => '/users/me/'
        }),
        login: builder.mutation({
            query: ({ email, password }) => ({
                url:'/jwt/create/',
                method: 'POST',
                body: { email, password }
            })
        }),
        register: builder.mutation({
            query: ({ username, email, password1, password2 }) => ({
                url:'/auth/register/',
                method: 'POST',
                body: { username, email, password1, password2 }
            })
        }),
        verify: builder.mutation({
            query: () => ({
                url:'/jwt/verify',
                method: 'POST',
            })
        }),
        logout: builder.mutation({
            query: () => ({
                url:'/logout/',
                method: 'POST',
            })
        }),
        activation: builder.mutation({
            query: ({ uid, token }) => ({
                url:'/users/activation/',
                method: 'POST',
                body: { uid, token }
            })
        }),
        resetPassword: builder.mutation({
            query: (email) => ({
                url:'/users/reset_password/',
                method: 'POST',
                body: { email }
            })
        }),
        resetPasswordConfirm: builder.mutation({
            query: ({ uid, token, new_password, re_new_password }) => ({
                url:'/users/reset_password_confirm/',
                method: 'POST',
                body: {  uid, token, new_password, re_new_password  }
            })
        })
    })
})

export const {
    useRetrieveUserQuery,
    useLoginMutation,
    useRegisterMutation,
    useVerifyMutation,
    useLogoutMutation,
    useActivationMutation,
    useResetPasswordMutation,
    useResetPasswordConfirmMutation,
 } = authApiSlice;