import { FormEvent, ChangeEvent } from "react";
import { Input } from '@/components/forms';
import  Spinner  from '@/components/spinner'

interface Config {
    labelText: string;
    labelId: string;
    type: string;
    value: string;
    required?: boolean;
}

interface Props {
    config: Config[];
    onChange: (event: ChangeEvent<HTMLInputElement>) => void;
	onSubmit: (event: FormEvent<HTMLFormElement>) => void;
    isLoading: boolean;
    btnText: string;
}

export default function Form({config, isLoading, btnText, onSubmit, onChange}: Props) {
    return (
        <form className="space-y-6" onSubmit={onSubmit}>
            {config.map(input => (
                <Input
                    labelId={input.labelId}
                    type={input.type}
                    onChange={onChange}
                    value={input.value}
                    required={input.required}
                >
                    {input.labelText}
                </Input>
            ))}

            <div>
              <button
                type="submit"
                className="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
              >
                {isLoading ? <Spinner small /> : `${btnText}`}
              </button>
            </div>
        </form>


    )
}