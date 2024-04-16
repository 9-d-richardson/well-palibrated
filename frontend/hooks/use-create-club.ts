import { useCreateClubMutation } from "@/redux/features/authApiSlice";
import { toast } from "react-toastify";
import { useRouter } from "next/navigation";
import { useState, ChangeEvent, FormEvent } from "react"
import { setAuth } from "@/redux/features/authSlice";
import { useAppDispatch } from "@/redux/hooks";

export default function useCreateClub() {
    const router = useRouter();
    const dispatch = useAppDispatch();
    const [createClub, {isLoading}] = useCreateClubMutation();
    const [ formData, setFormData ] = useState({
        club_name: '',
        permission_type: '',
        club_description: '',
        members: [],
        admins: [],
    });
    const { club_name, permission_type, club_description, members, admins } = formData;

    const onChange = (event: ChangeEvent<HTMLInputElement>) => {
        const { name, value } = event.target;
        setFormData({ ...formData, [name]: value })
    }

    const onSubmit = (event: FormEvent<HTMLFormElement>) => {
      event.preventDefault();

      createClub({club_name, permission_type, club_description, members, admins})
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
      club_name,
      permission_type,
      club_description,
      members,
      admins,
      isLoading,
      onChange,
      onSubmit,
    };
}
