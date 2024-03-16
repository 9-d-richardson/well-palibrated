import Link from 'next/link';

export default function Navbar() {
	return (<nav>
        <h1 className={`mb-3 text-4xl`}><Link href="/">Well Palibrated</Link></h1>
        <p><b>Account: </b>
          <Link href="/profiles/edit">Edit Profile</Link> |&nbsp;
           <Link href="/profiles/score">Calibration Score</Link> |&nbsp;
           <Link href="/account/logout">Log Out</Link>
        <br /><b>Events: </b>
          <Link href="/events/calendar">Calendar</Link> |&nbsp;
          <Link href="/events/search">Search Events</Link> |&nbsp;
          <Link href="/events/new">Create New Event</Link>
        <br /><b>Clubs: </b>
          <Link href="/clubs/search">Search Clubs</Link> |&nbsp;
          <Link href="/clubs/new">Create Club</Link></p>
        <br />
    </nav>
    )
};
