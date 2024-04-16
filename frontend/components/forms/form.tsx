import { FormEvent, ChangeEvent } from "react";
import { Input } from '@/components/forms';
import  { Spinner }  from '@/components/common';
import {
    RadioGroup,
    Radio,
    Textarea,
    Listbox,
    ListboxSection,
    ListboxItem
} from "@nextui-org/react";


interface Config {
    labelText?: string;
    labelId: string;
    type: string;
    value: string;
    link?: {
        linkText: string;
        linkUrl: string;
    };
    required?: boolean;
    btnLabel?: string;
    options?: Array<{
        btnLabel: string;
        btnId: string;
    }>;
}

interface Props {
    config: Config[];
    onChange: (event: ChangeEvent<HTMLInputElement>) => void;
	onSubmit: (event: FormEvent<HTMLFormElement>) => void;
    isLoading: boolean;
    btnText: string;
}

function InputCreator(input: any, onChange: any) {
    if (input.type === 'radio') {
        return (
            <RadioGroup
                label={input.labelText}
                key={input.labelId}
                onChange={onChange}
                // value={input.value}
                // link={input.link}
                isRequired={input.required}
                name={input.labelId}
            >
                {input.options?.map((option: {btnId: string, btnLabel: string}) => (
                    <Radio key={option.btnId} value={option.btnId}>{option.btnLabel}</Radio>
                ))}
            </RadioGroup>

        )
    } else if (input.type === 'textarea'){
        return (
            <Textarea
                key={input.labelId}
                label={input.labelText}
                type={input.type}
                onChange={onChange}
                name={input.labelId}
                // value={input.value}
                // link={input.link}
                isRequired={input.required}
            />
        )
    } else if (input.type === 'listbox') {
        return (
            <></>
        )
    } else {
        return (
            <Input
                key={input.labelId}
                labelId={input.labelId}
                type={input.type}
                onChange={onChange}
                value={input.value}
                link={input.link}
                required={input.required}
            >
                {input.labelText}
            </Input>
        )
    }
}

export default function Form({config, isLoading, btnText, onSubmit, onChange}: Props) {
    return (
        <form className="space-y-6" onSubmit={onSubmit}>
            {config.map(input => (
                <div key={input.labelId}>
                    {InputCreator(input, onChange)}
                </div>
            ))}

            <div>
              <button
                type="submit"
                className="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                disabled={isLoading}
              >
                {isLoading ? <Spinner small /> : `${btnText}`}
              </button>
            </div>
        </form>


    )
}
