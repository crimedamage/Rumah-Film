import React from 'react'

import SwiperCore, { Navigation, Pagination, A11y } from 'swiper'
import { Swiper, SwiperSlide } from 'swiper/react'

import StartRating from './StartRating';

const RecenlyAdded = () => {
  SwiperCore.use([Navigation, Pagination, A11y]);

  const films = [
    { title: 'Title 1', url: 'url-1', image: 'https://source.unsplash.com/random/800x600', rating: 50 },
    { title: 'Title 2', url: 'url-2', image: 'https://source.unsplash.com/random/800x600', rating: 50 },
    { title: 'Title 3', url: 'url-3', image: 'https://source.unsplash.com/random/800x600', rating: 50 },
    { title: 'Title 4', url: 'url-4', image: 'https://source.unsplash.com/random/800x600', rating: 50 },
    { title: 'Title 5', url: 'url-5', image: 'https://source.unsplash.com/random/800x600', rating: 50 },
    { title: 'Title 6', url: 'url-6', image: 'https://source.unsplash.com/random/800x600', rating: 50 },
    { title: 'Title 7', url: 'url-7', image: 'https://source.unsplash.com/random/800x600', rating: 50 },
    { title: 'Title 8', url: 'url-8', image: 'https://source.unsplash.com/random/800x600', rating: 50 },
    { title: 'Title 9', url: 'url-9', image: 'https://source.unsplash.com/random/800x600', rating: 50 },
    { title: 'Title 10', url: 'url-10', image: 'https://source.unsplash.com/random/800x600', rating: 50 },
  ]

  return (
    <>
      <h1 className="text-white transition dark:text-gray-300 pl-7 py-5 text-xl bg-indigo-600 dark:bg-gray-900 mb-1 rounded">RECENLY ADDED</h1>
      <div className="bg-indigo-300 rounded transition dark:bg-gray-700 mb-5 ">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-y-3 p-10">
          {
            films.map((film) => {
              return (
                <div className="mx-auto shadow-lg  rounded-lg hover:shadow-2xl bg-indigo-700 transition dark:bg-gray-900 duration-300">
                  <div className=" items-end justify-end h-56 w-full bg-cover" style={{ backgroundImage: `url(${film.image})` }}></div>
                  <div className="px-5 py-3 h-20 text-center">
                    <div className="overflow-ellipsis overflow-hidden h-24">
                      <a href={`/film/${film.url}`} className="text-white transition dark:text-gray-300">{film.title}</a>
                      <p className="text-white transition dark:text-gray-300 mt-2">
                        <StartRating rating={film.rating} />
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
