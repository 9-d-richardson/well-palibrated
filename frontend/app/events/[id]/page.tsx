'use client';

import type { Metadata, ResolvingMetadata } from "next";
import { fetchData } from '@/utils/api'
import { useGetEventQuery } from "@/redux/features/authApiSlice";
import { Spinner, ClubList } from '@/components/common';

// export async function generateMetadata(
//     { params }: Props,
//     parent: ResolvingMetadata
//     ): Promise<Metadata> {

//     const club_id = params.id
//     console.log(club_id)
//     const club = await fetchData(`clubs/clubs/` + club_id + `.json`);

//     return { title: club.club_name, }
//     }

// interface Config {
// 	label: string;
// 	value: string | undefined;
// }


export default function Page({params}: {params: {id: string} }) {
  const id = params.id;
  const { data: event, isLoading, isFetching } = useGetEventQuery(id);
  const event_name = event?.event_name
  const event_description = event?.event_description
  // const admins = event?.admins

  if (isLoading || isFetching) {
		return (
			<div className='flex justify-center my-8'>
				<Spinner large />
			</div>
		);
	}

	return (
		<>
			<header className='bg-white shadow'>
				<div className='mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8'>
					<h1 className='text-3xl font-bold tracking-tight text-gray-900'>
            {event_name || <Spinner small />}
					</h1>
				</div>
			</header>
			<main className='mx-auto max-w-7xl py-6 my-8 sm:px-6 lg:px-8'>
				<h1>{event_description || <Spinner small />}</h1>
				<p>Administrators:</p>
				{/* {admins.forEach(admin) => <p>admin</p>} */}
			</main>
		</>
	);
}
