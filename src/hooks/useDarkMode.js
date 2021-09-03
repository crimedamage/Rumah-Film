import { useState, useEffect } from 'react';

export default function useDarkMode() {
  const [theme, setTheme] = useState(localStorage.theme)
  const colorTheme = theme === 'light' ? 'dark' : 'light'

  useEffect(() => {
    localStorage.theme = theme;
    const root = window.document.documentElement
    root.classList.remove(colorTheme)
    root.classList.add(theme)
  }, [theme, colorTheme])

  return [colorTheme, setTheme]
}
