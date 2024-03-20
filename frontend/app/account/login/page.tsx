import Link from "next/link";
import LoginForm from "@/components/forms/loginForm";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Login",
  description: "Well palibrated login page"
}

export default function Page() {
    return (
        <div className="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
        <div className="sm:mx-auto sm:w-full sm:max-w-sm">
          <img
            className="mx-auto h-10 w-auto"
            src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600"
            alt="Well Palibrated"
          />
          <h2 className="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
            Log In
          </h2>
        </div>

        <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
          <LoginForm />
          <p className="mt-10 text-center text-sm text-gray-500">
            Don't have an account?{' '}
            <Link href="/account/register" className="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">
              Register
            </Link>
          </p>

        </div>
      </div>
    )
}
