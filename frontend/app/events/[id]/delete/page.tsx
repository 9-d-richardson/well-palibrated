import type { Metadata } from "next";
import { fetchData } from '@/utils/api'

export const metadata: Metadata = {
  title: "Clubs",
};

// export async function getStaticProps() {
//     return { props: { title: 'HomePage' } }
// }

export default async function Page() {
  return (
    <div>
      <h2 className={`text-2xl font-semibold`}>Delete Event</h2>
    </div>
  )
}
