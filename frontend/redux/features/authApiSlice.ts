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

interface Club {
    club_name: string;
    admins: [];
    club_description: string;
}

const authApiSlice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        retrieveUser: builder.query<User, void>({
            query: () => '/users/me/'
        }),
        login: builder.mutation({
            query: ({ username, password }) => ({
                url:'/auth/accounts/login/',
                method: 'POST',
                body: { username, password }
            })
        }),
        register: builder.mutation({
            query: ({ username, email, password1, password2 }) => ({
                url:'/auth/accounts/register/',
                method: 'POST',
                body: { username, email, password1, password2 }
            })
        }),
        verify: builder.mutation({
            query: () => ({
                url:'/auth/accounts/token/verify/',
                method: 'POST',
            })
        }),
        logout: builder.mutation({
            query: () => ({
                url:'/auth/accounts/logout/',
                method: 'POST',
            })
        }),
        // activation: builder.mutation({
        //     query: ({ uid, token }) => ({
        //         url:'/users/activation/',
        //         method: 'POST',
        //         body: { uid, token }
        //     })
        // }),
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
        }),

        getEventsList: builder.mutation({
            query: () => ({
                url:'/users/reset_password_confirm/',
                method: 'POST',
                body: {}
            })
        }),
        getClub: builder.query<Club, string>({
            query: (id) => `/auth/clubs/clubs/${id}`
        }),
        getClubList: builder.query<any, void>({
            query: () => `/auth/clubs/clubs/`
        }),
        getEvent:  builder.query<Club, string>({
            query: (id) => `/auth/events/events/${id}`
        }),
        getEventList: builder.query<any, void>({
            query: () => `/auth/events/events/`
        }),
    })
})

export const {
    useRetrieveUserQuery,
    useLoginMutation,
    useRegisterMutation,
    useVerifyMutation,
    useLogoutMutation,
    // useActivationMutation,
    useResetPasswordMutation,
    useResetPasswordConfirmMutation,
    useGetEventsListMutation,
    useGetClubQuery,
    useGetClubListQuery,
    useGetEventQuery,
    useGetEventListQuery,
 } = authApiSlice;
