import type { Metadata } from "next";
import { fetchData } from '@/utils/api'

export const metadata: Metadata = {
  title: "Search Clubs",
};

export default async function Page() {
  const data = await fetchData(`clubs/clubs.json`);

  return (
    <div>
      <h2 className={`text-2xl font-semibold`}>Search Clubs</h2>
    </div>
  )
}
