import React from 'react'

const StartRating = ({rating}) => {
  return (
    <div className="star-ratings-sprite mx-auto">
      <span style={{width: `${rating}%`}} className="rating"></span>
    </div>
  )
}

export default StartRating
