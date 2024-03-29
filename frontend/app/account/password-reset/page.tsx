import type { Metadata } from 'next';
import { ResetPasswordForm } from '@/components/forms'

export const metadata: Metadata = {
    title: 'Password Reset',
    description: 'Reset your Well Palibrated password'
}

export default function Page() {
    return (
        <div className="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
        <div className="sm:mx-auto sm:w-full sm:max-w-sm">
          <h2 className="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
            Reset Password
          </h2>
        </div>

        <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
          <ResetPasswordForm />
        </div>
      </div>
    )
}
