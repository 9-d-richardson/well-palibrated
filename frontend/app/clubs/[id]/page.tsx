import type { Metadata, ResolvingMetadata } from "next";
import { fetchData } from '@/utils/api'

type Props = {
    params: { id: string }
}

export async function generateMetadata(
    { params }: Props,
    parent: ResolvingMetadata
    ): Promise<Metadata> {

    const club_id = params.id
    console.log(club_id)
    const club = await fetchData(`clubs/clubs/` + club_id + `.json`);

    return { title: club.club_name, }
    }


// Page.getInitialProps = async () => {
//   return { title: 'test' }
// }


export default async function Page({params}: {params: {id: string} }) {
  const club_id = params.id;
  const club = await fetchData(`clubs/clubs/` + club_id + `.json`);

  return (
    <div>
      <h2 className={`text-2xl font-semibold`}>{ club.club_name }</h2>
    </div>
  )
}
