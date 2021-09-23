import React, { useState, useEffect } from 'react'

import SwiperCore, { Navigation, Pagination, A11y } from 'swiper'
import { Swiper, SwiperSlide } from 'swiper/react'

import StartRating from '../StartRating';

const MostWatched = () => {
  SwiperCore.use([Navigation, Pagination, A11y]);

  const [mostWatchedState, setMostWatchedState] = useState([])

  useEffect(() => {
    fetch('/api/Film_API/film/popular/ucok').then((res) => {
      if (res.ok) return res.json()
    }).then((res) => setMostWatchedState(res.lates.list)).catch((err) => console.log(err));
  }, [])

  return (
    <>
      <h1 className="text-white transition dark:text-gray-300 pl-7 py-5 text-xl bg-indigo-600 dark:bg-gray-900 mb-1 rounded">MOST WATCHED</h1>

      <Swiper
        id="mostSwipe"
        // install Swiper modules
        modules={[Navigation, Pagination, A11y]}
        spaceBetween={3}
        slidesPerView={6}
        navigation={{
          // nextEl: ".swiper-button-next",
          // prevEl: ".swiper-button-prev"
        }}
        pagination={{
          // el: ".swiper-pagination",
          clickable: true
        }}
      >
        {
          mostWatchedState.length > 0 && mostWatchedState.map((film) => {
            return (
              <SwiperSlide>
                <div className="mx-auto rounded shadow-lg overflow-hidden bg-indigo-700 transition dark:bg-gray-900 mb-10">
                  <div className="flex items-end justify-end h-56 w-full bg-cover" style={{ backgroundImage: `url(https://source.unsplash.com/random/800x600)` }}></div>
                  <div className="px-5 py-3 h-20 text-center">
                    <div className="overflow-y-auto overflow-hidden h-14">
                      <a href={"/"} className=" text-white transition dark:text-gray-300">{film.title}</a>
                      <p className="text-white transition dark:text-gray-300 mt-2">
                        <StartRating rating={film.rate} />
                      </p>
                    </div>
                  </div>
                </div>
              </SwiperSlide>
            )
          })
        }
      </Swiper>
    </>
  )
}

export default MostWatched
