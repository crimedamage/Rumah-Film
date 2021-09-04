import React from 'react'
import ThemeSwitch from '../components/ThemeSwitch'

const Footer = () => {
  return (
		<footer
			className="text-white dark:text-gray-300 transition duration-500 ease-in-out transform bg-indigo-800 dark:bg-gray-900">
			<div
				className="container flex flex-col flex-wrap p-8 mx-auto md:items-center lg:items-start md:flex-row md:flex-no-wrap ">
				<div className="flex flex-wrap flex-grow mt-8 text-left md:mt-0 ">
					<div className="w-full pr-4 md:w-2/4">
						<h2 className="mx-auto mb-6 text-xl font-semibold leading-snug tracking-tighter title-font">Lorem
							ipsum dolor sit amet consectetur adipisicing elit. Quod ab a voluptatem, debitis dicta dolores. Quaerat
							laboriosam reprehenderit ducimus, ab quia in doloremque natus consectetur numquam non adipisci. Suscipit,
							totam.</h2>
					</div>
					<div className="w-full px-8 md:w-1/4 ">
						<h1 className="mb-8 text-xs font-semibold tracking-widest uppercase title-font"> Company </h1>
						<nav className="mb-10 space-y-4 list-none">
							<li>
								<a
									className="cursor-pointer mr-1 text-sm text-blueGray-500 transition duration-500 ease-in-out transform rounded-sm focus:shadow-outline focus:outline-none focus:ring-2 ring-offset-current ring-offset-2">Home</a>
							</li>
							<li>
								<a
									className="cursor-pointer mr-1 text-sm text-blueGray-500 transition duration-500 ease-in-out transform rounded-sm focus:shadow-outline focus:outline-none focus:ring-2 ring-offset-current ring-offset-2">About</a>
							</li>
						</nav>
					</div>
					<div className="w-full px-8 md:w-1/4">
						<span className="inline-flex justify-start sm:mb-12">
							<a className="dark:text-blue-500 hover:text-gray-900 dark:hover:text-black">
								<svg fill="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" className="w-5 h-5"
									viewBox="0 0 24 24">
									<path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"></path>
								</svg>
							</a>
							<a className="ml-3 dark:text-blue-500 hover:text-gray-900 dark:hover:text-black">
								<svg fill="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" className="w-5 h-5"
									viewBox="0 0 24 24">
									<path
										d="M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2c9 5 20 0 20-11.5a4.5 4.5 0 00-.08-.83A7.72 7.72 0 0023 3z">
									</path>
								</svg>
							</a>
							<a className="ml-3 dark:text-blue-500 hover:text-gray-900 dark:hover:text-black">
								<svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
									className="w-5 h-5" viewBox="0 0 24 24">
									<rect width="20" height="20" x="2" y="2" rx="5" ry="5"></rect>
									<path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37zm1.5-4.87h.01"></path>
								</svg>
							</a>
							<a className="ml-3 dark:text-blue-500 hover:text-gray-900 dark:hover:text-black">
								<svg fill="currentColor" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
									stroke-width="0" className="w-5 h-5" viewBox="0 0 24 24">
									<path stroke="none"
										d="M16 8a6 6 0 016 6v7h-4v-7a2 2 0 00-2-2 2 2 0 00-2 2v7h-4v-7a6 6 0 016-6zM2 9h4v12H2z">
									</path>
									<circle cx="4" cy="4" r="2" stroke="none"></circle>
								</svg>
							</a>
						</span>

						<ThemeSwitch />

					</div>
				</div>
			</div>
		</footer>
  )
}

export default Footer
