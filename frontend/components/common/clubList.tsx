import { Spinner } from '@/components/common';
import Link from  'next/link';

interface Config {
	label: string;
	value: string | undefined;
}

interface Props {
	clubs_list: Config;
}

export default function List({ clubs_list }: any) {
	return (
        <>
					{clubs_list.map((club:any) => (
						<p><b>Club name:</b> <Link href={'/'}>{club.club_name}</Link></p>
					) )}
        </>
		// <ul role='list' className='divide-y divide-gray-100'>
		// 	{config.map(({ label, value }) => (
		// 		<li key={label} className='flex justify-between gap-x-6 py-5'>
		// 			<div>
		// 				<p className='text-sm font-semibold leading-6 text-gray-900'>
		// 					{label}
		// 				</p>
		// 			</div>
		// 			<div>
		// 				<h2 className='text-sm font-semibold leading-6 text-gray-900'>
		// 					{value || <Spinner small />}
		// 				</h2>
		// 			</div>
		// 		</li>
		// 	))}
		// </ul>
	);
}
