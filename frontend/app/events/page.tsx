import type { Metadata } from "next";
import { fetchData } from '@/utils/api'

export const metadata: Metadata = {
  title: "Clubs",
};

export default async function Page() {
  // const data = await fetchData(`events/irl-event.json`);
  // const events = data.results;
  // const eventList = events.map((event: any) => {
  //   return (
  //     <li key={event.event_name}>
  //       <b>Event name: </b>{event.event_name}
  //     </li>
  //   )
  // })

  // return (
  //   <div>
  //     <h2 className={`text-2xl font-semibold`}>Events</h2>
  //     <ul>{eventList}</ul>
  //   </div>
  // )
  return (
    <div>
      <h1>Events</h1>
    </div>
  )
}
