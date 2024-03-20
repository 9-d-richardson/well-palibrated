import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "@/styles/globals.css";
import Link from 'next/link';
const inter = Inter({ subsets: ["latin"] });
import Navbar from '@/components/navbar'
import Provider from '@/redux/provider'
import { Setup } from "@/components/utls";

export const metadata: Metadata = {
  title: {
    template: '%s - Well Palibrated',
    default: 'Well Palibrated',
  },
  description: "Plan events, calibrate attendance",
};

export default function RootLayout({
  children, data
}: Readonly<{
  children: React.ReactNode;
  data: any,
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Provider>
          <Setup />
          < Navbar />
          <div className="mx-auto max-w-7xl px-2 sn:px-6 lg:px-d my-8">
            {children}
          </div>
        </Provider>
      </body>
    </html>
  );
}
