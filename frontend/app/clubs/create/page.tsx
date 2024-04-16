import Link from "next/link";
import { CreateClubForm } from "@/components/forms";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Create New Club",
  description: "Well palibrated club creation"
}

export default function Page() {
    return (
        <div className="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
        <div className="sm:mx-auto sm:w-full sm:max-w-sm">
          <h2 className="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
            Create a new club
          </h2>
        </div>

        <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
          <CreateClubForm />
        </div>
      </div>
    )
}
