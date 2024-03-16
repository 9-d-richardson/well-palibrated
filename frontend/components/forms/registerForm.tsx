'use client';

import { useRegister } from "@/hooks";
import  Form  from "@/components/forms/form";

export default function RegisterForm() {
  const {
    username,
    email,
    password1,
    password2,
    isLoading,
    onChange,
    onSubmit,
  } = useRegister();

  const config = [
    {
      labelText: 'Username',
      labelId: 'username',
      type: 'text',
      value: username,
      required: true,
    },
    {
      labelText: 'Email',
      labelId: 'email',
      type: 'email',
      value: email,
      required: true,
    },
    {
      labelText: 'Password',
      labelId: 'password1',
      type: 'password',
      value: password1,
      required: true,
    },
    {
      labelText: 'Confirm password',
      labelId: 'password2',
      type: 'password',
      value: password2,
      required: true,
    }
  ];

  return (
      <Form
        config={config}
        isLoading={isLoading}
        btnText="Sign up"
        onChange={onChange}
        onSubmit={onSubmit}
      />
  );
}
