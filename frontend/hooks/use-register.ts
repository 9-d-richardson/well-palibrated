import { useRegisterMutation } from "@/redux/features/authApiSlice";
import { toast } from "react-toastify";
import { useRouter } from "next/navigation";
import { useState, ChangeEvent, FormEvent } from "react"

export default function useRegister() {
    const router = useRouter();
    const [register, {isLoading}] = useRegisterMutation();
    const [ formData, setFormData ] = useState({
        username: '',
        email: '',
        password1: '',
        password2: ''
    });

    const { username, email, password1, password2 } = formData;

    const onChange = (event: ChangeEvent<HTMLInputElement>) => {
        const { name, value } = event.target;
        setFormData({ ...formData, [name]: value })
    }

    const onSubmit = (event: FormEvent<HTMLFormElement>) => {
      event.preventDefault();

      register({username, email, password1, password2})
        .unwrap()
        .then(() => {
          toast.success('Account created!');
          router.push('login');
        })
        .catch(() => {
          toast.error('Failed to create account');
        })
    }

    return {
        username,
        email,
        password1,
        password2,
        isLoading,
        onChange,
        onSubmit,
    };
}
