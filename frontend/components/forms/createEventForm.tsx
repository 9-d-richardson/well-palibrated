'use client';

import { useCreateEvent } from "@/hooks";
import  Form  from "@/components/forms/form";

export default function CreateEventForm() {
  const {
    event_name,
    event_description,
    isLoading,
    onChange,
    onSubmit,
  } = useCreateEvent();

  const config = [
    {
      labelText: 'Event name:',
      labelId: 'event_name',
      type: 'text',
      value: event_name,
      required: true,
    },
    {
      labelText: 'Event description:',
      labelId: 'event_description',
      type: 'textarea',
      value: event_description,
      required: true,
    },
  ];


  return (
      <Form
        config={config}
        isLoading={isLoading}
        btnText="Create new event"
        onChange={onChange}
        onSubmit={onSubmit}
      />
  );
}
