import React, { useState, useEffect } from 'react'

import SwiperCore, { Navigation, Pagination, A11y } from 'swiper'
import { Swiper, SwiperSlide } from 'swiper/react'

import StartRating from '../StartRating';

const Jumbotron = () => {
  SwiperCore.use([Navigation, Pagination, A11y]);

  const [jumbotronState, setJumtoronState] = useState([])

  useEffect(() => {
    fetch('/api/Film_API/film/popular/ucok').then((res) => {
      if (res.ok) return res.json()
    }).then((res) => setJumtoronState(res.popular.results)).catch((err) => console.log(err));
  }, [])

  return (
    <>
      <h1 className="text-white transition dark:text-gray-300 pl-7 py-5 text-xl bg-indigo-600 dark:bg-gray-900 mb-1 rounded">TOP RATED</h1>

      <Swiper
        id="jumbotronSwipe"
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
          jumbotronState.length > 0 && jumbotronState.map((film) => {
            return (
              <SwiperSlide>
                <div className="mx-auto rounded shadow-lg overflow-hidden bg-indigo-700 transition dark:bg-gray-900 mb-10">
                  <div className="flex items-end justify-end h-56 w-full bg-cover" style={{ backgroundImage: `url(https://source.unsplash.com/random/800x600)` }}></div>
                  <div className="px-5 py-3 h-20 text-center">
                    <div className="overflow-y-auto overflow-hidden h-14">
                      <a href={`api/Film_API/detail/${film.id}/${film.title}`} className=" text-white transition dark:text-gray-300">{film.title}</a>
                      <p className="text-white transition dark:text-gray-300 mt-2">
                        <StartRating rating={film.vote_average * 10} />
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

export default Jumbotron
