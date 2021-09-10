import React, {useState, useEffect} from 'react'

import MostWatched from './home/MostWatched';
import RecenlyAdded from './home/RecenlyAdded';
import Recomendation from './home/Recomendation';
import SideContent from './SideContent';

const Content = () => {
  useEffect(() => {
    
  }, [])

  const fetchItems = fetch('http://127.0.0.1:8000/api/home_page')

  return (
    <div className="flex justify-between">
      <div className="min-h-screen w-10/12">
        <MostWatched />
        <RecenlyAdded />
        <Recomendation />
      </div>
      <div className="min-h-screen w-2/12 pl-5">
        <SideContent />
      </div>
    </div >
  )
}

export default Content
