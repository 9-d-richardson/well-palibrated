'use client'

import { useAppSelector } from "@/redux/hooks";
import { redirect } from "next/navigation";
import { Spinner } from "@/components/common";
import { toast } from "react-toastify";

interface Props {
    children: React.ReactNode;
}

// For pages which require being logged in, import this into the layout
export default function RequireAuth({children}: Props) {
    const {isLoading, isAuthenticated} = useAppSelector(state => state.auth);

    if (isLoading) {
        return (
            <div className="flex justify-center my-8">
                <Spinner large />
            </div>
        )
    }

    if (!isAuthenticated) {
        toast.error('Must be logged in')
        redirect('login');
    }

    return (
        <>{children}</>
    )
}
