import React, { useState } from 'react'
import PropTypes from 'prop-types'
import { Link } from 'react-router-dom';

const Header = ({ title, navbar }) => {

  const [isOpen, setIsOpen] = useState(false);

  return (
    <div>
      <nav className="relative px-4 md:px-28 py-4 flex justify-between items-center bg-indigo-900 transition dark:bg-gray-900">
        <a className="text-3xl font-bold leading-none text-white transition dark:text-gray-300 hidden lg:block" href="/">{title}</a>
        <ul className="hidden absolute top-1/2 left-1/2 transform -translate-y-1/2 -translate-x-1/2 lg:flex lg:mx-auto lg:items-center lg:w-auto lg:space-x-6">{
          navbar.map((x) => {
            return (
              <>
                <Link to={x.url}>
                  <li className={`text-sm ${window.location.pathname == x.url ? 'text-blue-600 font-bold' : 'text-gray-400 hover:text-gray-300'}`}>{x.name}</li>
                </Link>
                <li className="text-gray-300">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" className="w-4 h-4 current-fill"
                    viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 5v0m0 7v0m0 7v0m0-13a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z" />
                  </svg>
                </li>
              </>
            )
          })
        }</ul>
        <form action="#" method="GET">
          <div>
            <div id="search" className="shadow flex">
              <input className="w-full rounded-lg p-2 mr-3" type="text" name="query" placeholder="Search..." />
              <button type="submit"
                className="bg-indigo-500 dark:bg-gray-800 bg-opacity-50 w-auto flex justify-end items-center p-2 text-gray-300 hover:text-white rounded-full">
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24" width="24px"
                  fill="currentColor">
                  <path d="M0 0h24v24H0V0z" fill="none" />
                  <path
                    d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z" />
                </svg>
              </button>
            </div>
          </div>
        </form>
        <div className="lg:hidden">
          <button className="navbar-burger flex items-center text-blue-600 p-3" onClick={() => setIsOpen(!isOpen)}>
            <svg className="block h-4 w-4 fill-current" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <title>Mobile menu</title>
              <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"></path>
            </svg>
          </button>
        </div>
      </nav>
      <div className={`navbar-menu relative z-50 ${isOpen ? 'block' : 'hidden'}`}>
        <div className="navbar-backdrop fixed inset-0 bg-gray-800 opacity-25" onClick={() => setIsOpen(!isOpen)}></div>
        <nav
          className="fixed top-0 left-0 bottom-0 flex flex-col w-5/6 max-w-sm py-6 px-6 bg-white transition dark:bg-gray-800 border-r overflow-y-auto">
          <div className="flex items-center mb-8">
            <a className="mr-auto text-3xl font-bold leading-none transition dark:text-gray-300" href="/">{title}</a>
            <button className="navbar-close" onClick={() => setIsOpen(!isOpen)}>
              <svg className="h-6 w-6 text-gray-400 cursor-pointer hover:text-gray-300" xmlns="http://www.w3.org/2000/svg"
                fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
              </svg>
            </button>
          </div>
          <div>
            <ul>
              {
                navbar.map((x) => {
                  return (
                    <>
                      <li className="mb-1">
                        <a className="block p-4 text-sm font-semibold text-gray-400 hover:bg-blue-50 hover:text-blue-600 rounded"
                          href={x.url}>{x.name}</a>
                      </li>
                    </>
                  )
                })
              }
            </ul>
          </div>
          <div className="mt-auto">
            <p className="my-4 text-xs text-center text-gray-400">
              <span>Copyright © {new Date().getFullYear()}</span>
            </p>
          </div>
        </nav>
      </div>
    </div>
  )
}

Header.defaultProps = {
  navbar: [
    { name: "SEMUA", url: '/list' },
    { name: "TOP RATING", url: '/top-rating' },
    { name: "MOST WATCHED", url: '/most-watched' },
    { name: "TAHUN", url: '/year' },
  ]
}

Header.propTypes = {
  title: PropTypes.string,
  navbar: PropTypes.object,
}

export default Header
