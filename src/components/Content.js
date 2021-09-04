import React from 'react'

import MostWatched from './MostWatched';
import RecenlyAdded from './RecenlyAdded';
import Recomendation from './Recomendation';
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
