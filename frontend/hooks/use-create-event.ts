import { useCreateEventMutation } from "@/redux/features/authApiSlice";
import { toast } from "react-toastify";
import { useRouter } from "next/navigation";
import { useState, ChangeEvent, FormEvent } from "react"
import { setAuth } from "@/redux/features/authSlice";
import { useAppDispatch } from "@/redux/hooks";

export default function useCreateEvent() {
    const router = useRouter();
    const dispatch = useAppDispatch();
    const [createEvent, {isLoading}] = useCreateEventMutation();
    const [ formData, setFormData ] = useState({
        event_name: '',
        event_description: '',
        members: [],
        admins: [],
    });
    const { event_name, event_description,  } = formData;

    const onChange = (event: ChangeEvent<HTMLInputElement>) => {
        const { name, value } = event.target;
        setFormData({ ...formData, [name]: value })
    }

    const onSubmit = (event: FormEvent<HTMLFormElement>) => {
      event.preventDefault();

      createEvent({event_name, event_description})
        .unwrap()
        .then(() => {
          dispatch(setAuth());
          toast.success('Club created!');
          router.push('/');
        })
        .catch(() => {
          toast.error('Failed to create club');
        })
    }

    return {
      event_name,
      event_description,
      isLoading,
      onChange,
      onSubmit,
    };
}
