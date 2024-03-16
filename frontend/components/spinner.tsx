import cn from 'classnames';
import { ImSpinner3 } from 'react-icons/im';

interface Props {
    small?: boolean;
    medium?: boolean;
    large?: boolean
}

export default function Spinner({small, medium, large}: Props) {
    const className = cn('animate-spin text-white-300 fill-white-300 mr-2', {
        'w-4 h-4': small,
        'w-6 h-6': medium,
        'w-8 h-8': large,
    });

    return (
        <div role='status'>
            <ImSpinner3 className={className} />
            <span className="sr-only">Loading...</span>
        </div>
    )
}
