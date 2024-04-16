'use client';

import { useCreateClub } from "@/hooks";
import  Form  from "@/components/forms/form";

export default function CreateClubForm() {
  const {
    club_name,
    permission_type,
    club_description,
    admins,
    members,
    isLoading,
    onChange,
    onSubmit,
  } = useCreateClub();

  const config = [
    {
      labelText: 'Club name:',
      labelId: 'club_name',
      type: 'text',
      value: club_name,
      required: true,
    },
    {
      labelText: 'Club description:',
      labelId: 'club_description',
      type: 'textarea',
      value: club_description,
      required: false,
    },
    {
      labelText: 'Permission type:',
      labelId: 'permission_type',
      type: 'radio',
      value: permission_type,
      required: true,
      options: [
        {
          btnLabel: 'Invite only',
          btnId: 'invite_only'
        },
        {
          btnLabel: 'Request to join',
          btnId: 'request_to_join'
        },
        {
          btnLabel: 'Public',
          btnId: 'public'
        },
      ],
    },
  ];


  return (
      <Form
        config={config}
        isLoading={isLoading}
        btnText="Create new club"
        onChange={onChange}
        onSubmit={onSubmit}
      />
  );
}
