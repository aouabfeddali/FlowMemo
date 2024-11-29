import colors from "tailwindcss/colors";

export const NAV_THEME = {
  light: {
    background: "hsl(0 0% 100%)", // background
    border: "hsl(240 5.9% 90%)", // border
    card: "hsl(0 0% 100%)", // card
    notification: "hsl(0 84.2% 60.2%)", // destructive
    primary: "hsl(240 5.9% 10%)", // primary
    text: "hsl(240 10% 3.9%)", // foreground
  },
  dark: {
    background: "hsl(240 10% 3.9%)", // background
    border: "hsl(240 3.7% 15.9%)", // border
    card: "hsl(240 10% 3.9%)", // card
    notification: "hsl(0 72% 51%)", // destructive
    primary: "hsl(0 0% 98%)", // primary
    text: "hsl(0 0% 98%)", // foreground
  },
};

export const INTRO_CONTENT = [
  {
    title: "FlowMemo",
    bg: colors.emerald[50],
    fontColor: colors.green[600],
  },
  {
    title: "FlowMemo",
    bg: colors.indigo[600],
    fontColor: colors.sky[100],
  },
  {
    title: "FlowMemo",
    bg: colors.emerald[800],
    fontColor: colors.emerald[50],
  },
  {
    title: "FlowMemo",
    bg: colors.violet[600],
    fontColor: colors.violet[50],
  },
  {
    title: "FlowMemo",
    bg: colors.cyan[400],
    fontColor: colors.emerald[300],
  },
];
