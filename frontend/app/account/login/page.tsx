import type { Metadata } from "next";
import { fetchData } from '@/utils/api'

const pageName = "Login"

export const metadata: Metadata = {
  title: pageName,
};

export default async function Page() {
  return (
    <div>
      <h2 className={`text-2xl font-semibold`}>{pageName}</h2>
    </div>
  )
}
