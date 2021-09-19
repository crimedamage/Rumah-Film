import React from 'react'

import MostWatched from './home/MostWatched';
import RecenlyAdded from './home/RecenlyAdded';
import Recomendation from './home/Recomendation';
import SideContent from './SideContent';

const Content = () => {

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
