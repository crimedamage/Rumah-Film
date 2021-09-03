import React from 'react'
import useDarkMode from '../hooks/useDarkMode'

const ThemeSwitch = () => {

  const [colorTheme, setTheme] = useDarkMode()

  return (
    <label id="switchTheme" for="switchCheckbox" className="cursor-pointer">
      <div className="relative">
        <input id="switchCheckbox" type="checkbox" className="sr-only" checked={colorTheme === 'light'} onClick={() => setTheme(colorTheme)} />
        <div className="w-10 h-4 bg-gray-400 rounded-full shadow-inner"></div>
        <div className="dot absolute w-6 h-6 rounded-full shadow -left-1 -top-1 transition">
          {colorTheme === 'light' ? 
            <svg xmlns="http://www.w3.org/2000/svg" className="text-white" viewBox="0 0 24 24"
              fill="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
            </svg> 
            : 
            <svg xmlns="http://www.w3.org/2000/svg" className="text-white" viewBox="0 0 24 24"
              fill="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
            </svg> 
          }
        </div>
      </div>
    </label>
  )
}

export default ThemeSwitch
