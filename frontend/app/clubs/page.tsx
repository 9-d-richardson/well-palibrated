import type { Metadata } from "next";
import { fetchData } from '@/utils/api'

export const metadata: Metadata = {
  title: "Clubs",
};

export default async function Page() {
  const data = await fetchData(`clubs/clubs.json`);
  const clubs = data.results;
  const clubList = clubs.map((club: any) => {
    return (
      <li key={club.club_name}>
        <b>Club name: </b>{club.club_name}
      </li>
    )
  })

  return (
    <div>
      <h2 className={`text-2xl font-semibold`}>Clubs</h2>
      <ul>{clubList}</ul>
    </div>
  )
}
