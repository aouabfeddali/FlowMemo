import { Clipboard, Cog, HomeIcon } from "lucide-react";

import type { SidebarLink } from "~/components/sidebar-items";

interface AdditionalLinks {
  title: string;
  links: SidebarLink[];
}

export const defaultLinks: SidebarLink[] = [
  { href: "/dashboard", title: "Home", icon: HomeIcon },
  { href: "/account", title: "Account", icon: Cog },
  { href: "/settings", title: "Instellingen", icon: Cog },
];

export const additionalLinks: AdditionalLinks[] = [
  {
    title: "Flow",
    links: [
      {
        href: "/notes",
        title: "Notities",
        icon: Clipboard,
      },
    ],
  },
];
