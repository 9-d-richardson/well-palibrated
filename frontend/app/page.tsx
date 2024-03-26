import Link from 'next/link';
import type { Metadata } from 'next';

export const metadata: Metadata = {
	title: 'Full Auth | Home',
	description: 'Full Auth home page',
};

export default function Page() {
	return (
		<main className="bg-white">
			<div className="relative isolate px-6 pt-14 lg:px-8">
				<div className="mx-auto max-w-2xl py-32 sm:py-48 lg:py-56">
					<div className="text-center">
						<h1 className="text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl">
							Well Palibrated
						</h1>
						<p className="mt-6 text-lg leading-8 text-gray-600">
							Website thing.
						</p>
						<div className="mt-10 flex items-center justify-center gap-x-6">
							<Link
								href="#"
								className="rounded-md bg-indigo-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
							>
								Login
							</Link>
							<Link
								href="#"
								className="rounded-md bg-indigo-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
							>
								See Events
							</Link>
						</div>
					</div>
				</div>
			</div>
    	</main>
	);
}
