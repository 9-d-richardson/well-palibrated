'use client';

import { Form } from "@/components/forms";
import { useResetPasswordConfirm } from "@/hooks";

interface Props {
        uid: string;
        token: string;
}

export default function ResetPasswordConfirmForm({uid, token}: Props) {
    const {new_password, re_new_password, isLoading, onChange, onSubmit} = useResetPasswordConfirm(uid, token);

    const config = [
        {
            labelText: 'New Password',
            labelId: 'new_password',
            type: 'password',
            onChange,
            value: new_password,
            required: true,
        },
        {
            labelText: 'Confirm New Password',
            labelId: 're_new_password',
            type: 'password',
            onChange,
            value: re_new_password,
            required: true,
        }
    ]
    return (
        <Form
            config={config}
            isLoading={isLoading}
            btnText="Request password reset"
            onChange={onChange}
            onSubmit={onSubmit}
        >

        </Form>
    )
}
