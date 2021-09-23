import React, { useState, useEffect } from 'react'

import SwiperCore, { Navigation, Pagination, A11y } from 'swiper'

import StartRating from '../StartRating';

const RecenlyAdded = () => {
  SwiperCore.use([Navigation, Pagination, A11y]);

  const [recenlyAddedState, setRecenlyAddedState] = useState([])

  useEffect(() => {
    fetch('/api/Film_API/film/top/ucok').then((res) => {
      if (res.ok) return res.json()
    }).then((res) => setRecenlyAddedState(res.lates.list)).catch((err) => console.log(err));
  }, [])

  return (
    <>
      <h1 className="text-white transition dark:text-gray-300 pl-7 py-5 text-xl bg-indigo-600 dark:bg-gray-900 mb-1 rounded">RECENLY ADDED</h1>
      <div className="bg-indigo-300 rounded transition dark:bg-gray-700 mb-5 ">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-y-3 gap-x-3 p-10">
          {
            recenlyAddedState.length > 0 && recenlyAddedState.map((film) => {
              return (
                <div className="w-full shadow-lg rounded-lg hover:shadow-2xl bg-indigo-700 transition dark:bg-gray-900 duration-300">
                  <div className="items-end justify-end h-56 w-full bg-cover" style={{ backgroundImage: `url(https://source.unsplash.com/random/800x600)` }}></div>
                  <div className="px-5 py-3 h-20 text-center">
                    <div className="overflow-y-auto overflow-hidden h-14">
                      <a href={`/`} className="text-white transition dark:text-gray-300">{film.title}</a>
                      <p className="text-white transition dark:text-gray-300 mt-2">
                        <StartRating rating={film.rate} />
                      </p>
                    </div>
                  </div>
                </div>
              )
            })
          }
        </div>
      </div>
    </>
  )
}

export default RecenlyAdded
